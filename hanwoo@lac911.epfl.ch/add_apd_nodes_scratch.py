"""

"""
from MDSplus import *

s=1180413603
model_tree_num=-1
myTree=Tree("spectroscopy",-1)
myTree.createPulse(s)
myTree=Tree('spectroscopy',s,'edit')
gpi_root="\SPECTROSCOPY::TOP.GPI_TCV"
myTree.addNode(gpi_root,"structure")
gpi_node=myTree.getNode(gpi_root)
gpi_node.addNode("APD_ARRAY","structure")
node_apd_array=gpi_node.getNode("APD_ARRAY")
#Add nodes that contain necessary parameters for controlling digitizers
node_apd_array.addNode("T_START","numeric") #start time for 132's and 196
node_apd_array.addNode("T_STOP","numeric") #stop time for 132's and 196
node_apd_array.addNode("DIG_FREQ","numeric") # sampling frequency of digitizers (unit: MHz)
node_apd_array.addNode("DIG_SAMPS","numeric") # number of samples of digitizers
myTree.getNode(gpi_root+".APD_ARRAY.T_START").putData(0.)
myTree.getNode(gpi_root+".APD_ARRAY.T_STOP").putData(.9)
myTree.getNode(gpi_root+".APD_ARRAY.DIG_FREQ").putData(2.)
myTree.getNode(gpi_root+".APD_ARRAY.DIG_SAMPS").putData(myTree.tdiCompile("_tstart = "+gpi_root+".APD_ARRAY:T_START, _tstop = "+gpi_root+".APD_ARRAY:T_STOP, _freq = "+gpi_root+".APD_ARRAY:DIG_FREQ, _nksamp = (_tstop - _tstart) * _freq * 1000E3 / 1024 + .5, _ksamp_int = INT(_nksamp)"))

#Add a hardware structure node
node_apd_array.addNode("HARDWARE","structure")
node_hardware=node_apd_array.getNode("HARDWARE")

#Add a calibration structure node
node_apd_array.addNode("CALIBRATION","structure")
node_calib=node_apd_array.getNode("CALIBRATION")

#Add devices under the hardware node
node_hardware.addDevice("ACQ196","acq196")
node_hardware.addDevice("ACQ196AO","acq196ao")
node_hardware.addDevice("DIO2","dio2")
node_hardware.addDevice("ACQ132_1","acq132")
node_hardware.addDevice("ACQ132_2","acq132")
node_hardware.addDevice("ACQ132_3","acq132")
node_hardware.addDevice("ACQ132_4","acq132")


for i in range (1,9):
    #Add nodes for HV programmed and measured, 8 for 8 cathodes
    node_calib.addNode("HV_PROG_"+str(i),"numeric")
    node_calib.addNode("HV_MEAS_"+str(i),"numeric")
    #Make the HV prog and meas nodes to refer the value from ACQ196AO and ACQ196.
    #node_hardware.getNode("ACQ196AO.OUTPUT_0"+str(i)).putData(myTree.tdiCompile("Build_Signal(["+node_calib.getNode("HV_PROG_"+str(i)).getFullPath()+","+node_calib.getNode("HV_PROG_"+str(i)).getFullPath()+"], *, "+node_apd_array.getNode("T_START").getFullPath()+"-0.5 : "+node_apd_array.getNode("T_STOP").getFullPath()+"+0.5)"))
#    node_calib.getNode("HV_MEAS_"+str(i)).putData(myTree.tdiCompile(node_hardware.getNode("ACQ196.INPUT_0"+str(i)).getFullPath()))
    #Identity arrays. Arrays are 10 by 12 arrays, and an identity array filters entries that correspond to each cathode. For example, IDEN_ARR_1 only filters the entries which drived by HV_MEAS_1. So its first 15 entries has value 1. That means, the value is 1 for the entire first column and the first 5 of the second column.
    node_calib.addNode("IDEN_ARR_"+str(i),"numeric")
    iden_arr=[[float(i==1)]*5+[float(i==1)]*5,[float(i==1)]*5+[float(i==2)]*5,[float(i==2)]*5+[float(i==2)]*5,[float(i==3)]*5+[float(i==3)]*5,[float(i==3)]*5+[float(i==4)]*5,[float(i==4)]*5+[float(i==4)]*5,[float(i==5)]*5+[float(i==5)]*5,[float(i==5)]*5+[float(i==6)]*5,[float(i==6)]*5+[float(i==6)]*5,[float(i==7)]*5+[float(i==7)]*5,[float(i==7)]*5+[float(i==8)]*5,[float(i==8)]*5+[float(i==8)]*5]
    #node_calib.getNode("IDEN_ARR_"+str(i)).putData(iden_arr)


#Add S_LAMBDA arrays for each filter. Brightness is obtained by multiplying S_LAMBDA with the inverse GAIN array and .
node_calib.addNode("S_LAMBDA_DA","numeric")
node_calib.addNode("S_LAMBDA_HA","numeric")
node_calib.addNode("S_LAMBDA_HEI","numeric")

#Add mean signal arrays. This is needed just for the calibration.
node_calib.addNode("MEAN_SIG_ARR","numeric")
mean_sig_arr="["
for i in range (0,120):
    if (i+1)%10==1:
        mean_sig_arr=mean_sig_arr+"["
    if i%30+1<10:
        mean_sig_arr=mean_sig_arr+"MEAN("+node_hardware.getNode("ACQ132_"+str(i/30+1)+".INPUT_0"+str(i%30+1)).getFullPath()+")"
    else:
        mean_sig_arr=mean_sig_arr+"MEAN("+node_hardware.getNode("ACQ132_"+str(i/30+1)+".INPUT_"+str(i%30+1)).getFullPath()+")"
    if (i+1)%10==0:
        mean_sig_arr=mean_sig_arr+"]"
    if i!=119:
        mean_sig_arr=mean_sig_arr+","
    else:
        mean_sig_arr=mean_sig_arr+"]"

node_calib.getNode("MEAN_SIG_ARR").putData(myTree.tdiCompile(mean_sig_arr))

#Add background arrays
node_calib.addNode("BACK_ARR","numeric")

#Add coefficient arrays
node_calib.addNode("COEF_0TH_ARR","numeric")
node_calib.addNode("COEF_1ST_ARR","numeric")
node_calib.addNode("COEF_2ND_ARR","numeric")
node_calib.addNode("COEF_3RD_ARR","numeric")
node_calib.addNode("COEF_4TH_ARR","numeric")

#Add gain arrays. Values are an 10 by 12 array, and each component is 50 * exp(polynomial(HV_measured))/exp(polynomial(400)) so that it gives 50 V when HV_meas=400 V.
node_calib.addNode("GAIN_ARR","numeric")

myTree.write()
myTree.close()
print('Done adding nodes')

