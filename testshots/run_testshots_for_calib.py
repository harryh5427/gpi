"""
Takes 100 testshots for calibration. The first 50 shots are taken with APDs illuminated by the labsphere. The second 50 shots are taken without the labsphere.
"""
from MDSplus import *
from MitDevices.acq132 import ACQ132
from MitDevices.acq196 import ACQ196
from MitDevices.acq196ao import ACQ196AO
import time
import datetime
import numpy as np
import random

now=datetime.datetime.now()
num_shot=50
while True:
    data = input("First, "+str(num_shot)+" testshots with APDs illuminated by the labsphere will be taken. Is the labsphere on? (yes=1/no=0):")
    if data==0:
        print("Type 1 if you are ready.")
    elif data==1:
        break

gpi_root="\SPECTROSCOPY::TOP.GPI_TCV"
HV_prog=np.linspace(2.5,4.5,num_shot)
HV_meas=[[],[],[],[],[],[],[],[]]
while True:
    data = input("What is the filter used? values of filters (case insensitive): Da6563, HeI5876, HeI6670, HeII4686, open :").upper()
    if data!='DA6563' and data!='HEI5876' and data!='HEI6670' and data!='HEII4686' and data!='OPEN':
        print("Type a valid value.")
    else:
        break

filter_used=data
modelTree_num=-1
modelTree=Tree("spectroscopy",modelTree_num)

for i in range (1,num_shot*2+1):
    s=int(str(1)+now.strftime("%y%m%d")+str(500+i))
    print("Current shot number: "+str(s))
    modelTree.createPulse(s) #Copies the model tree
    myTree=Tree("spectroscopy",s)
    myTree.getNode(gpi_root+".APD_ARRAY.CONTROL.FILTER.VALUE").putData(filter_used)
    if i<=num_shot:    
        HV_prog_i=random.choice(HV_prog)
        HV_prog=np.delete(HV_prog,np.where(HV_prog==HV_prog_i))
    if i>num_shot:
        myTree_with_light=Tree("spectroscopy",s-num_shot)
        HV_prog_i=myTree_with_light.getNode(gpi_root+".APD_ARRAY.CONTROL.HV_PROG_1")
    for j in range (1,9):
        myTree.getNode(gpi_root+".APD_ARRAY.CONTROL.HV_PROG_"+str(j)).putData(HV_prog_i)
    
    #Initialize DIO2 through TCL command, since there is no working python command for DIO2
    #DIO2_ENCDEC does not work for this, neither does DIO4
    myDIO2=myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE:DIO2")
    myTree.tcl('do /meth '+myDIO2.getFullPath()+' init')
    print("Initialized DIO2")
    
    #Take node of each digitizer, and initialize them
    myACQ132_1=myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE:ACQ132_1")
    inst_ACQ132_1=ACQ132(myACQ132_2)
    inst_ACQ132_1.initftp()
    print("Initialized ACQ132_1")
    myACQ132_2=myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE:ACQ132_2")
    inst_ACQ132_2=ACQ132(myACQ132_2)
    inst_ACQ132_2.initftp()
    print("Initialized ACQ132_2")
    myACQ132_3=myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE:ACQ132_3")
    inst_ACQ132_3=ACQ132(myACQ132_3)
    inst_ACQ132_3.initftp()
    print("Initialized ACQ132_3")
    myACQ132_4=myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE:ACQ132_4")
    inst_ACQ132_4=ACQ132(myACQ132_4)
    inst_ACQ132_4.initftp()
    print("Initialized ACQ132_4")
    myACQ196=myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE:ACQ196")
    inst_ACQ196=ACQ196(myACQ196)
    inst_ACQ196.initftp()
    print("Initialized ACQ196")
    myACQ196AO=myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE:ACQ196AO")
    inst_ACQ196AO=ACQ196AO(myACQ196AO)
    inst_ACQ196AO.init()
    print("Initialized ACQ196AO")
    
    #Wait for the initialization
    time.sleep(7)
    
    #Trigger DIO2 in order to start the data acquisition
    myTree.tcl('do /meth '+myDIO2.getFullPath()+' trigger')
    #myTree.getNode('GPI.APD_ARRAY.HARDWARE:eng_encoder').doMethod("set_event","SPECTROSCOPY_START") #Should work with Trig.mode=event in the device setup of DIO2 - put a spectroscopy start MDSplus event on the CPCI network
    print("Triggered DIO2")
    
    #Wait for shot to end
    time.sleep(7)
    
    #Store data to the MDSplus tree
    inst_ACQ132_1.store()
    print("Stored data on ACQ132_1")
    inst_ACQ132_2.store()
    print("Stored data on ACQ132_2")
    inst_ACQ132_3.store()
    print("Stored data on ACQ132_3")
    inst_ACQ132_4.store()
    print("Stored data on ACQ132_4")
    inst_ACQ196.store()
    print("Stored data on ACQ196")
    
    if i>num_shot:
        back_arr=myTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.MEAN_SIG_ARR").getData().data()
        myTree_with_light.getNode(gpi_root+".APD_ARRAY.CALIBRATION.BACK_ARR").putData(myTree.tdiCompile(str(back_arr)))
        sig_minus_back=back_arr-myTree_with_light.getNode(gpi_root+".APD_ARRAY.CALIBRATION.MEAN_SIG_ARR").getData().data()
        
        #From the logbook entry 1110518, the spectral radiance of the 'old' Labsphere at 6550 A is 0.632 mW/cm^2/ster/micron=0.632 microW/cm^2/ster/nm=0.0632 microW/cm^2/ster/A
        rad_da=0.0632/1000. #convert uW/cm^2/ster/A to mW/cm^2/ster/A
        #The spectral radiance of the 'old' Labsphere at 5876 A is 0.0461 uW/cm^2/ster/A
        rad_hei=0.0461/1000. #convert uW/cm^2/ster/A to mW/cm^2/ster/A
        bandpass_da=116.78 #unit : A
        bandpass_hei=114.52 #unit : A
        avg_transf_func_da=1.
        avg_transf_func_hei=1.
        if filter_used=='DA6563':
            sensitivity=rad_da*avg_transf_func_da*bandpass_da/(sig_minus_back/1000.)
        if filter_used=='HEI5876':
            sensitivity=rad_hei*avg_transf_func_hei*bandpass_hei/(sig_minus_back/1000.)
        myTree_with_light.getNode(gpi_root+".APD_ARRAY.CALIBRATION.S_LAM_"+str(filter_used)).putData(myTree.tdiCompile(str(sensitivity))) #temporarily stores the sensitivity array in the S_LAM node.
        
        #Record the HV_meas values
        HV_meas_arr=myTree_with_light.getNode(gpi_root+".APD_ARRAY.RESULT.HV_MEAS_ARR").getData().data()
        HV_meas[0].append(HV_meas_arr[0][0])
        HV_meas[1].append(HV_meas_arr[1][5])
        HV_meas[2].append(HV_meas_arr[3][0])
        HV_meas[3].append(HV_meas_arr[4][5])
        HV_meas[4].append(HV_meas_arr[6][0])
        HV_meas[5].append(HV_meas_arr[7][5])
        HV_meas[6].append(HV_meas_arr[9][0])
        HV_meas[7].append(HV_meas_arr[10][5])
    
    if i==num_shot:
        while True:
            data = input("Now, "+str(num_shot)+" testshots WITHOUT the labsphere will be taken. Is the labsphere off? (yes=1/no=0):")
            if data==0:
                print("Type 1 if you are ready.")
            elif data==1:
                break
    myTree.close()

dummy_arr=sig_minus_back_arr #Just to copy the size of the array
for i in range (0:12):
    for j in range (0:10):
        dummy_arr[i][j]=0.
node_model_coef_0th=modelTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.COEF_0TH_ARR")
node_model_coef_1st=modelTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.COEF_1ST_ARR")
node_model_coef_2nd=modelTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.COEF_2ND_ARR")
node_model_coef_3rd=modelTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.COEF_3RT_ARR")
node_model_coef_4th=modelTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.COEF_4TH_ARR")
node_model_coef_0th.putData(myTree.tdiCompile(str(dummy_arr)))
node_model_coef_1st.putData(myTree.tdiCompile(str(dummy_arr)))
node_model_coef_2nd.putData(myTree.tdiCompile(str(dummy_arr)))
node_model_coef_3rd.putData(myTree.tdiCompile(str(dummy_arr)))
node_model_coef_4th.putData(myTree.tdiCompile(str(dummy_arr)))
node_model_sens_over_gain_arr=modelTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.S_LAM_"+str(filter_used))
node_model_sens_over_gain_arr.putData(myTree.tdiCompile(str(dummy_arr)))
node_model_back_arr=modelTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.BACK_ARR")
node_model_back_arr.putData(myTree.tdiCompile(str(dummy_arr)))

#Calculates polyfit coefficients, 5 for each detector element, and store the array in the model tree's coefficient nodes. Also, calculates the mean background array and stores it in the model tree's background array node.
for i in range (0,120):
    back=[]
    sig_minus_back=[]
    for j in range (1,num_shot+1):
        yourTree=Tree("spectroscopy",s-2*num_shot+j)
        back_arr=yourTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.BACK_ARR").getData().data()
        back.append(back_arr[i/10][i%10])
        sig_minus_back_arr=back_arr-yourTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.MEAN_SIG_ARR").getData().data()
        sig_minus_back.append(sig_minus_back_arr[i/10][i%10])
        yourTree.close()
    back_arr=node_model_back_arr.getData().data()
    back_arr[i/10][i%10]=np.mean(back)
    print("Background signal of detector (r,c)=["+str(i%10)+"]["+str(i/10)+"], Mean: "+str(np.mean(back))+", STD: "+str(np.std(back)))
    node_model_back_arr.putData(myTree.tdiCompile(str(back_arr)))
    coef=np.polyfit(HV_meas[i/15],np.log(sig_minus_back),4)
    coef_0th_arr=node_model_coef_0th.getData().data()
    coef_1st_arr=node_model_coef_1st.getData().data()
    coef_2nd_arr=node_model_coef_2nd.getData().data()
    coef_3rd_arr=node_model_coef_3rd.getData().data()
    coef_4th_arr=node_model_coef_4th.getData().data()
    coef_0th_arr[i/10][i%10]=coef[0]
    coef_1st_arr[i/10][i%10]=coef[1]
    coef_2nd_arr[i/10][i%10]=coef[2]
    coef_3rd_arr[i/10][i%10]=coef[3]
    coef_4th_arr[i/10][i%10]=coef[4]
    node_model_coef_0th.putData(myTree.tdiCompile(str(coef_0th_arr)))
    node_model_coef_1st.putData(myTree.tdiCompile(str(coef_1st_arr)))
    node_model_coef_2nd.putData(myTree.tdiCompile(str(coef_2nd_arr)))
    node_model_coef_3rd.putData(myTree.tdiCompile(str(coef_3rd_arr)))
    node_model_coef_4th.putData(myTree.tdiCompile(str(coef_4th_arr)))

for i in range (0,120):
    sens_over_gain=[]
    for j in range (1,num_shot+1):
        yourTree=Tree("spectroscopy",s-2*num_shot+j)
        yourTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.COEF_0TH_ARR").putData(tdiCompile(str(node_model_coef_0th.getData().data())))
        yourTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.COEF_1ST_ARR").putData(tdiCompile(str(node_model_coef_1st.getData().data())))
        yourTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.COEF_2ND_ARR").putData(tdiCompile(str(node_model_coef_2nd.getData().data())))
        yourTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.COEF_3RD_ARR").putData(tdiCompile(str(node_model_coef_3rd.getData().data())))
        yourTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.COEF_4TH_ARR").putData(tdiCompile(str(node_model_coef_4th.getData().data())))
        sens_arr=yourTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.S_LAM_"+str(filter_used)).getData().data()
        yourTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.S_LAM_"+str(filter_used)).deleteData() #Delete the sensitivity array which was temporarily stored in this node.
        gain_arr=yourTree.getNode(gpi_root+".APD_ARRAY.RESULT.GAIN_ARR").getData().data()
        sens_over_gain.append(sens_arr[i/10][i%10]/gain_arr[i/10][i%10])
        yourTree.close()
    sens_over_gain_arr=node_model_sens_over_gain_arr.getData().data()
    sens_over_gain_arr[i/10][i%10]=np.mean(sens_over_gain)
    print("S_LAMBDA of detector (r,c)=["+str(i%10)+"]["+str(i/10)+"], Mean: "+str(np.mean(sens_over_gain))+", STD: "+str(np.std(sens_over_gain)))
    node_model_sens_over_gain_arr.putData(myTree.tdiCompile(str(sens_over_gain_arr)))

modelTree.close() #close the tree

