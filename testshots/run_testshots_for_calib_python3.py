"""
Takes 2*num_shot testshots for calibration. The first num_shot shots are taken with APDs illuminated by the labsphere. The second num_shot shots are taken without the labsphere. Make sure you have the GPI_TCV node in the model tree. GPI_TCV is generated by running add_apd_nodes.py.
"""
from MDSplus import *
#from MitDevices.acq132 import ACQ132
#from MitDevices.acq196 import ACQ196
#from MitDevices.acq196ao import ACQ196AO
import time
import datetime
import numpy as np
import math
import random
import matplotlib.pyplot as plt

now=datetime.datetime.now()
num_shot=20
"""
while True:
    data = input("First, "+str(num_shot)+" testshots with APDs illuminated by the labsphere will be taken. Is the labsphere on? (yes=1/no=0): ")
    if data==0:
        print("Type 1 if you are ready.")
    elif data==1:
        break
"""
gpi_root="\SPECTROSCOPY::TOP.GPI_TCV"
dead_channels=[78,88,104]
half_dead_channels=[]
HV_prog_pool=np.linspace(3.0,4.1,num_shot)
HV_meas=[[],[],[],[],[],[],[],[]]
HV_prog=[[],[],[],[],[],[],[],[]]
filter_list=['DA6563','HEI5876','HEI6670','HEII4686','OPEN']
"""
while True:
    data = input("What is the filter you use? Values of filters: 0 is Da6563, 1 is HeI5876, 2 is HeI6670, 3 is HeII4686, 4 is open : ")
    if data!=0 and data!=1 and data!=2 and data!=3 and data!=4:
        print("Type a valid value.")
    else:
        break
"""
data=0
filter_used=filter_list[data]
modelTree_num=-1
modelTree=Tree("spectroscopy",modelTree_num)
labsphere_current=0.
labsphere_current=0.199e-6

for i in range (21,num_shot*2+1):
    s=int(str(1)+now.strftime("%y%m%d")+str(500+i))
#    s=1180622500+i #old 'old fiber' shots
#    s=1180626500+i #old 'new fiber' shots
#    s=1180702500+i #recent 'new fiber' shots
    s=1180705500+i #copied old 'new fiber' shots
    print("Current shot number: "+str(s))
#    modelTree.createPulse(s) #Copies the model tree
    myTree=Tree("spectroscopy",s)
    
    myTree.getNode(gpi_root+".APD_ARRAY.CONTROL.FILTER.VALUE").putData(filter_used)
    myTree.getNode(gpi_root+".APD_ARRAY.CONTROL.DIG_TSTOP").putData(.1)
    if i<=num_shot:    
        HV_prog_i=random.choice(HV_prog_pool)
        HV_prog_pool=np.delete(HV_prog_pool,np.where(HV_prog_pool==HV_prog_i))
    if i>num_shot:
        myTree_with_light=Tree("spectroscopy",s-num_shot)
        HV_prog_i=myTree_with_light.getNode(gpi_root+".APD_ARRAY.CONTROL.HV_PROG_1").getData().data()
    for j in range (1,9):
        myTree.getNode(gpi_root+".APD_ARRAY.CONTROL.HV_PROG_"+str(j)).putData(myTree.tdiCompile(str(HV_prog_i)))
    """
    #Initialize DIO2 through TCL command, since there is no working python command for DIO2
    #DIO2_ENCDEC does not work for this, neither does DIO4
    myDIO2=myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE:DIO2")
    myTree.tcl('do /meth '+myDIO2.getFullPath()+' init')
    print("Initialized DIO2")
    
    #Take node of each digitizer, and initialize them
    myACQ132_1=myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE:ACQ132_1")
    inst_ACQ132_1=ACQ132(myACQ132_1)
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
    myACQ196AO=myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE:ACQ196AO")
    inst_ACQ196AO=ACQ196AO(myACQ196AO)
    inst_ACQ196AO.init()
    print("Initialized ACQ196AO")
    myACQ196=myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE:ACQ196")
    inst_ACQ196=ACQ196(myACQ196)
    inst_ACQ196.initftp()
    print("Initialized ACQ196")

    #Wait for the initialization
    time.sleep(5)
    
    inst_ACQ132_1.getstate()
    inst_ACQ132_2.getstate()
    inst_ACQ132_3.getstate()
    inst_ACQ132_4.getstate()
    inst_ACQ196AO.getstate()
    inst_ACQ196.getstate()
    #Trigger DIO2 in order to start the data acquisition
    myTree.tcl('do /meth '+myDIO2.getFullPath()+' trigger')
    #myTree.getNode('GPI.APD_ARRAY.HARDWARE:eng_encoder').doMethod("set_event","SPECTROSCOPY_START") #Should work with Trig.mode=event in the device setup of DIO2 - put a spectroscopy start MDSplus event on the CPCI network
    print("Triggered DIO2")
    
    #Wait for shot to end
    time.sleep(15)
    
    inst_ACQ132_1.getstate()
    inst_ACQ132_2.getstate()
    inst_ACQ132_3.getstate()
    inst_ACQ132_4.getstate()
    inst_ACQ196AO.getstate()
    inst_ACQ196.getstate()
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
    """
    if i>num_shot:
        back_arr=myTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.MEAN_SIG_ARR").getData().data()
        myTree_with_light.getNode(gpi_root+".APD_ARRAY.CALIBRATION.BACK_ARR").putData(myTree_with_light.tdiCompile(str(back_arr.tolist())))
        sig_minus_back=back_arr-myTree_with_light.getNode(gpi_root+".APD_ARRAY.CALIBRATION.MEAN_SIG_ARR").getData().data()
        
        #From the logbook entry 1110518, the spectral radiance of the 'old' Labsphere at 6550 A is 0.632 mW/cm^2/ster/micron=0.632 microW/cm^2/ster/nm=0.0632 microW/cm^2/ster/A
#        rad_da=0.0632/1000. #convert uW/cm^2/ster/A to mW/cm^2/ster/A
#        labsphere_current=0.1946e-6 #Amps
        radiance_da_when_luminance_728_foot_lamberts=5.55/1000. #mW/cm^2/ster/nm
        conversion_factor=3.15e-10 #Amps/foot_lamberts
        rad_da=radiance_da_when_luminance_728_foot_lamberts*labsphere_current/conversion_factor/728.
        #The spectral radiance of the 'old' Labsphere at 5876 A is 0.0461 uW/cm^2/ster/A
        rad_hei=0.0461/100. #convert uW/cm^2/ster/A to mW/cm^2/ster/nm
        area_under_transfer_func_da6563=9.606 #unit : nm, from logbook entry 1170125
        area_under_transfer_func_hei5876=2.991 #unit : nm, from logbook entry 1170125
        if filter_used=='DA6563':
            sensitivity=rad_da*area_under_transfer_func_da6563/sig_minus_back
        if filter_used=='HEI5876':
            sensitivity=rad_hei*area_under_transfer_func_hei5876/sig_minus_back
        myTree_with_light.getNode(gpi_root+".APD_ARRAY.CALIBRATION.S_L_"+str(filter_used)).putData(myTree_with_light.tdiCompile(str(sensitivity.tolist()))) #temporarily stores the sensitivity array in the S_LAM node.
        
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
        HV_prog[0].append(myTree_with_light.getNode(gpi_root+".APD_ARRAY.CONTROL.HV_PROG_1").getData().data())
        HV_prog[1].append(myTree_with_light.getNode(gpi_root+".APD_ARRAY.CONTROL.HV_PROG_2").getData().data())
        HV_prog[2].append(myTree_with_light.getNode(gpi_root+".APD_ARRAY.CONTROL.HV_PROG_3").getData().data())
        HV_prog[3].append(myTree_with_light.getNode(gpi_root+".APD_ARRAY.CONTROL.HV_PROG_4").getData().data())
        HV_prog[4].append(myTree_with_light.getNode(gpi_root+".APD_ARRAY.CONTROL.HV_PROG_5").getData().data())
        HV_prog[5].append(myTree_with_light.getNode(gpi_root+".APD_ARRAY.CONTROL.HV_PROG_6").getData().data())
        HV_prog[6].append(myTree_with_light.getNode(gpi_root+".APD_ARRAY.CONTROL.HV_PROG_7").getData().data())
        HV_prog[7].append(myTree_with_light.getNode(gpi_root+".APD_ARRAY.CONTROL.HV_PROG_8").getData().data())
        myTree_with_light.close()
    
    flag=0
    if i==num_shot:
        while True:
            data = input("Type the current from the labsphere in micro-amps: ")
            while True:
                data_2 = input("Is the value "+str(data)+" micro-amps correct? (yes=1/no=0) :")
                if data_2==1:
                    labsphere_current=data*1.e-6
                    flag=1
                    break
            if flag==1:
                break
    
    if i==num_shot:
        while True:
            data = input("Now, "+str(num_shot)+" testshots WITHOUT the labsphere will be taken. Is the labsphere off? (yes=1/no=0) :")
            if data==0:
                print("Type 1 if you are ready.")
            elif data==1:
                break
    
    myTree.close()

dummy_arr=sig_minus_back #Just to copy the size of the array
for i in range (0,12):
    for j in range (0,10):
        dummy_arr[i][j]=0.

node_model_coef_0th_hv=modelTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.HV_CHECK.HVCOEF_0TH")
node_model_coef_1st_hv=modelTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.HV_CHECK.HVCOEF_1ST")
node_model_coef_0th=modelTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.COEF_0TH_ARR")
node_model_coef_1st=modelTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.COEF_1ST_ARR")
node_model_coef_2nd=modelTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.COEF_2ND_ARR")
node_model_coef_3rd=modelTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.COEF_3RD_ARR")
node_model_coef_4th=modelTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.COEF_4TH_ARR")
node_model_coef_0th_gain=modelTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.HV_CHECK.GAINCOEF_0TH")
node_model_coef_1st_gain=modelTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.HV_CHECK.GAINCOEF_1ST")
node_model_coef_2nd_gain=modelTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.HV_CHECK.GAINCOEF_2ND")
node_model_coef_3rd_gain=modelTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.HV_CHECK.GAINCOEF_3RD")
node_model_coef_4th_gain=modelTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.HV_CHECK.GAINCOEF_4TH")
node_model_s_lambda_arr=modelTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.S_L_"+str(filter_used))
node_model_back_arr=modelTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.BACK_ARR")
"""
node_model_coef_0th_hv.putData(modelTree.tdiCompile(str(dummy_arr.tolist())))
node_model_coef_1st_hv.putData(modelTree.tdiCompile(str(dummy_arr.tolist())))
node_model_coef_0th.putData(modelTree.tdiCompile(str(dummy_arr.tolist())))
node_model_coef_1st.putData(modelTree.tdiCompile(str(dummy_arr.tolist())))
node_model_coef_2nd.putData(modelTree.tdiCompile(str(dummy_arr.tolist())))
node_model_coef_3rd.putData(modelTree.tdiCompile(str(dummy_arr.tolist())))
node_model_coef_4th.putData(modelTree.tdiCompile(str(dummy_arr.tolist())))
node_model_coef_0th_gain.putData(modelTree.tdiCompile(str(dummy_arr.tolist())))
node_model_coef_1st_gain.putData(modelTree.tdiCompile(str(dummy_arr.tolist())))
node_model_coef_2nd_gain.putData(modelTree.tdiCompile(str(dummy_arr.tolist())))
node_model_coef_3rd_gain.putData(modelTree.tdiCompile(str(dummy_arr.tolist())))
node_model_coef_4th_gain.putData(modelTree.tdiCompile(str(dummy_arr.tolist())))
node_model_s_lambda_arr.putData(modelTree.tdiCompile(str(dummy_arr.tolist())))
node_model_back_arr.putData(modelTree.tdiCompile(str(dummy_arr.tolist())))
"""
#Calculates polyfit coefficients, 5 for each detector element, and store the array in the model tree's coefficient nodes. Also, calculates the mean background array and stores it in the model tree's background array node.
for i in range (0,120):
    back=[]
    sig_minus_back=[]
    for j in range (1,num_shot+1):
        myTree_with_light=Tree("spectroscopy",s-2*num_shot+j)
        back_arr=myTree_with_light.getNode(gpi_root+".APD_ARRAY.CALIBRATION.BACK_ARR").getData().data()
        back.append(back_arr[int(i/10)][int(i%10)])
        sig_minus_back_arr=back_arr-myTree_with_light.getNode(gpi_root+".APD_ARRAY.CALIBRATION.MEAN_SIG_ARR").getData().data()
        sig_minus_back.append(sig_minus_back_arr[int(i/10)][int(i%10)])
        myTree_with_light.close()
    
    back_arr=node_model_back_arr.getData().data()
    back_arr[int(i/10)][int(i%10)]=np.mean(back)
    print("Background signal of detector (r,c)=["+str(int(i%10))+"]["+str(int(i/10))+"], Mean: "+str(np.mean(back))+", STD: "+str(np.std(back)))
    node_model_back_arr.putData(back_arr)

    HV_meas_sorted=HV_meas[int(i/15)]
    HV_prog_sorted=HV_prog[int(i/15)]
    HV_meas_sorted=np.sort(HV_meas_sorted)
    sort_ind=np.argsort(HV_prog_sorted)
    HV_prog_sorted=np.sort(HV_prog_sorted)
    temp=np.array([])
    for j in range (0,len(sig_minus_back)):
        temp=np.append(temp,sig_minus_back[sort_ind[j]])
    
    sig_minus_back=temp
    
    coef_hv=np.polyfit(HV_meas_sorted,HV_prog_sorted,1)
    coef_0th_hv_arr=node_model_coef_0th_hv.getData().data()
    coef_1st_hv_arr=node_model_coef_1st_hv.getData().data()
    coef_0th_hv_arr[int(i/10)][int(i%10)]=coef_hv[1]
    coef_1st_hv_arr[int(i/10)][int(i%10)]=coef_hv[0]
    if math.isnan(coef_hv[1]) or math.isinf(coef_hv[1]):
        coef_0th_hv_arr[int(i/10)][int(i%10)]=coef_0th_hv_arr[0][0]
    if math.isnan(coef_hv[0]) or math.isinf(coef_hv[0]):
        coef_1st_hv_arr[int(i/10)][int(i%10)]=coef_1st_hv_arr[0][0]
    node_model_coef_0th_hv.putData(modelTree.tdiCompile(str(coef_0th_hv_arr.tolist())))
    node_model_coef_1st_hv.putData(modelTree.tdiCompile(str(coef_1st_hv_arr.tolist())))
    
    coef=np.polyfit(HV_meas_sorted,np.log(sig_minus_back),4)
    coef_0th_arr=node_model_coef_0th.getData().data()
    coef_1st_arr=node_model_coef_1st.getData().data()
    coef_2nd_arr=node_model_coef_2nd.getData().data()
    coef_3rd_arr=node_model_coef_3rd.getData().data()
    coef_4th_arr=node_model_coef_4th.getData().data()
    coef_0th_arr[int(i/10)][int(i%10)]=coef[4]
    coef_1st_arr[int(i/10)][int(i%10)]=coef[3]
    coef_2nd_arr[int(i/10)][int(i%10)]=coef[2]
    coef_3rd_arr[int(i/10)][int(i%10)]=coef[1]
    coef_4th_arr[int(i/10)][int(i%10)]=coef[0]
    if math.isnan(coef[4]) or math.isinf(coef[4]):
        coef_0th_arr[int(i/10)][int(i%10)]=coef_0th_arr[0][0]
    if math.isnan(coef[3]) or math.isinf(coef[3]):
        coef_1st_arr[int(i/10)][int(i%10)]=coef_1st_arr[0][0]
    if math.isnan(coef[2]) or math.isinf(coef[2]):
        coef_2nd_arr[int(i/10)][int(i%10)]=coef_2nd_arr[0][0]
    if math.isnan(coef[1]) or math.isinf(coef[1]):
        coef_3rd_arr[int(i/10)][int(i%10)]=coef_3rd_arr[0][0]
    if math.isnan(coef[0]) or math.isinf(coef[0]):
        coef_4th_arr[int(i/10)][int(i%10)]=coef_4th_arr[0][0]
    node_model_coef_0th.putData(modelTree.tdiCompile(str(coef_0th_arr.tolist())))
    node_model_coef_1st.putData(modelTree.tdiCompile(str(coef_1st_arr.tolist())))
    node_model_coef_2nd.putData(modelTree.tdiCompile(str(coef_2nd_arr.tolist())))
    node_model_coef_3rd.putData(modelTree.tdiCompile(str(coef_3rd_arr.tolist())))
    node_model_coef_4th.putData(modelTree.tdiCompile(str(coef_4th_arr.tolist())))
    
    coef_0th_gain_arr=node_model_coef_0th.getData().data()
    coef_1st_gain_arr=node_model_coef_1st.getData().data()
    coef_2nd_gain_arr=node_model_coef_2nd.getData().data()
    coef_3rd_gain_arr=node_model_coef_3rd.getData().data()
    coef_4th_gain_arr=node_model_coef_4th.getData().data()
    if i!=104:
        coef_gain=np.polyfit(np.log(sig_minus_back),HV_meas_sorted,4)
        coef_0th_gain_arr[int(i/10)][int(i%10)]=coef_gain[4]
        coef_1st_gain_arr[int(i/10)][int(i%10)]=coef_gain[3]
        coef_2nd_gain_arr[int(i/10)][int(i%10)]=coef_gain[2]
        coef_3rd_gain_arr[int(i/10)][int(i%10)]=coef_gain[1]
        coef_4th_gain_arr[int(i/10)][int(i%10)]=coef_gain[0]
    else:
        coef_gain=[0.,0.,0.,0.,0.]
    if math.isnan(coef_gain[4]) or math.isinf(coef_gain[4]) or i==104:
        coef_0th_gain_arr[int(i/10)][int(i%10)]=coef_0th_gain_arr[0][0]
    if math.isnan(coef_gain[3]) or math.isinf(coef_gain[3]) or i==104:
        coef_1st_gain_arr[int(i/10)][int(i%10)]=coef_1st_gain_arr[0][0]
    if math.isnan(coef_gain[2]) or math.isinf(coef_gain[2]) or i==104:
        coef_2nd_gain_arr[int(i/10)][int(i%10)]=coef_2nd_gain_arr[0][0]
    if math.isnan(coef_gain[1]) or math.isinf(coef_gain[1]) or i==104:
        coef_3rd_gain_arr[int(i/10)][int(i%10)]=coef_3rd_gain_arr[0][0]
    if math.isnan(coef_gain[0]) or math.isinf(coef_gain[0]) or i==104:
        coef_4th_gain_arr[int(i/10)][int(i%10)]=coef_4th_gain_arr[0][0]
    node_model_coef_0th_gain.putData(modelTree.tdiCompile(str(coef_0th_gain_arr.tolist())))
    node_model_coef_1st_gain.putData(modelTree.tdiCompile(str(coef_1st_gain_arr.tolist())))
    node_model_coef_2nd_gain.putData(modelTree.tdiCompile(str(coef_2nd_gain_arr.tolist())))
    node_model_coef_3rd_gain.putData(modelTree.tdiCompile(str(coef_3rd_gain_arr.tolist())))
    node_model_coef_4th_gain.putData(modelTree.tdiCompile(str(coef_4th_gain_arr.tolist())))

for i in range (1,num_shot*2+1):
    myTree=Tree("spectroscopy",s-2*num_shot+i)
    myTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.BACK_ARR").putData(myTree.tdiCompile(str(node_model_back_arr.getData().data().tolist())))
    myTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.HV_CHECK.HVCOEF_0TH").putData(myTree.tdiCompile(str(node_model_coef_0th_hv.getData().data().tolist())))
    myTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.HV_CHECK.HVCOEF_1ST").putData(myTree.tdiCompile(str(node_model_coef_1st_hv.getData().data().tolist())))
    myTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.COEF_0TH_ARR").putData(myTree.tdiCompile(str(node_model_coef_0th.getData().data().tolist())))
    myTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.COEF_1ST_ARR").putData(myTree.tdiCompile(str(node_model_coef_1st.getData().data().tolist())))
    myTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.COEF_2ND_ARR").putData(myTree.tdiCompile(str(node_model_coef_2nd.getData().data().tolist())))
    myTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.COEF_3RD_ARR").putData(myTree.tdiCompile(str(node_model_coef_3rd.getData().data().tolist())))
    myTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.COEF_4TH_ARR").putData(myTree.tdiCompile(str(node_model_coef_4th.getData().data().tolist())))
    myTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.HV_CHECK.GAINCOEF_0TH").putData(myTree.tdiCompile(str(node_model_coef_0th_gain.getData().data().tolist())))
    myTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.HV_CHECK.GAINCOEF_1ST").putData(myTree.tdiCompile(str(node_model_coef_1st_gain.getData().data().tolist())))
    myTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.HV_CHECK.GAINCOEF_2ND").putData(myTree.tdiCompile(str(node_model_coef_2nd_gain.getData().data().tolist())))
    myTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.HV_CHECK.GAINCOEF_3RD").putData(myTree.tdiCompile(str(node_model_coef_3rd_gain.getData().data().tolist())))
    myTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.HV_CHECK.GAINCOEF_4TH").putData(myTree.tdiCompile(str(node_model_coef_4th_gain.getData().data().tolist())))
    myTree.close()

for i in range (0,120):
    s_lambda=[]
    for j in range (1,num_shot+1):
        myTree_with_light=Tree("spectroscopy",s-2*num_shot+j)
        sens_arr=myTree_with_light.getNode(gpi_root+".APD_ARRAY.CALIBRATION.S_L_"+str(filter_used)).getData().data()
        gain_arr=myTree_with_light.getNode(gpi_root+".APD_ARRAY.RESULT.GAIN_ARR").getData().data()
        s_lambda.append(sens_arr[int(i/10)][int(i%10)]*gain_arr[int(i/10)][int(i%10)])
        myTree_with_light.close()
    s_lambda_arr=node_model_s_lambda_arr.getData().data()
    s_lambda_arr[int(i/10)][int(i%10)]=np.mean(s_lambda)
    if math.isnan(np.mean(s_lambda)) or math.isinf(np.mean(s_lambda)):
        s_lambda_arr[int(i/10)][int(i%10)]=s_lambda_arr[0][0]
    print("S_LAMBDA of detector (r,c)=["+str(int(i%10))+"]["+str(int(i/10))+"], Mean: "+str(np.mean(s_lambda))+", STD: "+str(np.std(s_lambda)))
    node_model_s_lambda_arr.putData(modelTree.tdiCompile(str(s_lambda_arr.tolist())))

for i in range (1,num_shot*2+1):
    myTree=Tree("spectroscopy",s-2*num_shot+i)
    myTree.getNode(gpi_root+".APD_ARRAY.CALIBRATION.S_L_"+str(filter_used)).putData(myTree.tdiCompile(str(node_model_s_lambda_arr.getData().data().tolist())))
    myTree.close()

modelTree.close() #close the tree

gain_00=[]
for i in range (1,num_shot+1):
    myTree_with_light=Tree("spectroscopy",s-2*num_shot+i)
    gain_arr=myTree_with_light.getNode(gpi_root+".APD_ARRAY.RESULT.GAIN_ARR").getData().data()
    gain_00.append(gain_arr[0][0])

HV_meas_sorted=HV_meas[int(0/15)]
sort_ind=np.argsort(HV_meas_sorted)
HV_meas_sorted=np.sort(HV_meas_sorted)
temp=np.array([])
for j in range (0,len(gain_00)):
    temp=np.append(temp,gain_00[sort_ind[j]])
"""
gain_00=temp
plt.plot(HV_meas_sorted,gain_00,".-")
plt.xlabel('HV_meas (V)')
plt.ylabel('gain_arr[0][0]')
plt.show()
"""
