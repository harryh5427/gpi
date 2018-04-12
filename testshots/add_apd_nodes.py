"""

"""
from MDSplus import *

model_tree_num=-1
myTree=Tree("spectroscopy",model_tree_num,'Edit')
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

#Add devices under the hardware node
node_hardware.addDevice("ACQ196","acq196")
node_hardware.addDevice("ACQ196AO","acq196ao")
node_hardware.addDevice("DIO2","dio2")
node_hardware.addDevice("DT132_1","acq132")
node_hardware.addDevice("DT132_2","acq132")
node_hardware.addDevice("DT132_3","acq132")
node_hardware.addDevice("DT132_4","acq132")

for i in range (1,9):
    #Add nodes for HV programmed and measured, 8 for 8 cathodes
    node_apd_array.addNode("HV_PROG_"+str(i),"numeric")
    node_apd_array.addNode("HV_MEAS_"+str(i),"numeric")
    #Make the HV prog and meas nodes to refer the value from ACQ196AO and ACQ196.
    node_apd_array.getNode("HV_PROG_"+str(i)).putData(myTree.tdiCompile(node_hardware.getNode("ACQ196AO.OUTPUT_0"+str(i)).getFullPath()))
    node_apd_array.getNode("HV_MEAS_"+str(i)).putData(myTree.tdiCompile(node_hardware.getNode("ACQ196.INPUT_0"+str(i)).getFullPath()))
    
    #Identity arrays. Arrays are 10 by 12 arrays, and an identity array filters entries that correspond to each cathode. For example, IDEN_ARR_1 only filters the entries which drived by HV_MEAS_1. So its first 15 entries has value 1. That means, the value is 1 for the entire first column and the first 5 of the second column.
    node_apd_array.addNode("IDEN_ARR_"+str(i),"numeric")

myTree.getNode(gpi_root+".APD_ARRAY.IDEN_ARR_1").putData(myTree.tdiCompile("[[1.,1.,1.,1.,1.,1.,1.,1.,1.,1.],[1.,1.,1.,1.,1.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]]"))
myTree.getNode(gpi_root+".APD_ARRAY.IDEN_ARR_2").putData(myTree.tdiCompile("[[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,1.,1.,1.,1.,1.],[1.,1.,1.,1.,1.,1.,1.,1.,1.,1.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]]"))
myTree.getNode(gpi_root+".APD_ARRAY.IDEN_ARR_3").putData(myTree.tdiCompile("[[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[1.,1.,1.,1.,1.,1.,1.,1.,1.,1.],[1.,1.,1.,1.,1.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]]"))
myTree.getNode(gpi_root+".APD_ARRAY.IDEN_ARR_4").putData(myTree.tdiCompile("[[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,1.,1.,1.,1.,1.],[1.,1.,1.,1.,1.,1.,1.,1.,1.,1.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]]"))
myTree.getNode(gpi_root+".APD_ARRAY.IDEN_ARR_5").putData(myTree.tdiCompile("[[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[1.,1.,1.,1.,1.,1.,1.,1.,1.,1.],[1.,1.,1.,1.,1.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]]"))
myTree.getNode(gpi_root+".APD_ARRAY.IDEN_ARR_6").putData(myTree.tdiCompile("[[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,1.,1.,1.,1.,1.],[1.,1.,1.,1.,1.,1.,1.,1.,1.,1.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]]"))
myTree.getNode(gpi_root+".APD_ARRAY.IDEN_ARR_7").putData(myTree.tdiCompile("[[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[1.,1.,1.,1.,1.,1.,1.,1.,1.,1.],[1.,1.,1.,1.,1.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]]"))
myTree.getNode(gpi_root+".APD_ARRAY.IDEN_ARR_8").putData(myTree.tdiCompile("[[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,1.,1.,1.,1.,1.],[1.,1.,1.,1.,1.,1.,1.,1.,1.,1.]]"))


#Add S_LAMBDA arrays for each filter. Brightness is obtained by multiplying S_LAMBDA with the inverse GAIN array and .
node_apd_array.addNode("S_LAMBDA_DA","numeric")
node_apd_array.addNode("S_LAMBDA_HA","numeric")
node_apd_array.addNode("S_LAMBDA_HEI","numeric")

#Add background arrays
node_apd_array.addNode("BACK_ARR","numeric")


node_apd_array.addNode("COEF_0TH_ARR","numeric")
node_apd_array.addNode("COEF_1ST_ARR","numeric")
node_apd_array.addNode("COEF_2ND_ARR","numeric")
node_apd_array.addNode("COEF_3RD_ARR","numeric")
node_apd_array.addNode("COEF_4TH_ARR","numeric")

node_apd_array.addNode("GAIN_ARR","numeric")

myTree.getNode(gpi_root+".APD_ARRAY.GAIN_ARR").putData(myTree.tdiCompile(myTree.getNode(gpi_root+".APD_ARRAY.IDEN_ARR_1").getFullPath()+"*(50.*exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_1").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_1").getFullPath()+")^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_1").getFullPath()+")^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_1").getFullPath()+")^4)/(exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*(400.)+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*(400.)^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*(400.)^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*(400.)^4)))+"+myTree.getNode(gpi_root+".APD_ARRAY.IDEN_ARR_2").getFullPath()+"*(50.*exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_2").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_2").getFullPath()+")^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_2").getFullPath()+")^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_2").getFullPath()+")^4)/(exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*(400.)+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*(400.)^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*(400.)^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*(400.)^4)))+"+myTree.getNode(gpi_root+".APD_ARRAY.IDEN_ARR_3").getFullPath()+"*(50.*exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_3").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_3").getFullPath()+")^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_3").getFullPath()+")^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_3").getFullPath()+")^4)/(exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*(400.)+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*(400.)^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*(400.)^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*(400.)^4)))+"+myTree.getNode(gpi_root+".APD_ARRAY.IDEN_ARR_4").getFullPath()+"*(50.*exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_4").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_4").getFullPath()+")^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_4").getFullPath()+")^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_4").getFullPath()+")^4)/(exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*(400.)+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*(400.)^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*(400.)^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*(400.)^4)))+"+myTree.getNode(gpi_root+".APD_ARRAY.IDEN_ARR_5").getFullPath()+"*(50.*exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_5").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_5").getFullPath()+")^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_5").getFullPath()+")^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_5").getFullPath()+")^4)/(exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*(400.)+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*(400.)^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*(400.)^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*(400.)^4)))+"+myTree.getNode(gpi_root+".APD_ARRAY.IDEN_ARR_6").getFullPath()+"*(50.*exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_6").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_6").getFullPath()+")^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_6").getFullPath()+")^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_6").getFullPath()+")^4)/(exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*(400.)+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*(400.)^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*(400.)^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*(400.)^4)))+"+myTree.getNode(gpi_root+".APD_ARRAY.IDEN_ARR_7").getFullPath()+"*(50.*exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_7").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_7").getFullPath()+")^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_7").getFullPath()+")^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_7").getFullPath()+")^4)/(exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*(400.)+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*(400.)^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*(400.)^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*(400.)^4)))+"+myTree.getNode(gpi_root+".APD_ARRAY.IDEN_ARR_8").getFullPath()+"*(50.*exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_8").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_8").getFullPath()+")^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_8").getFullPath()+")^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_8").getFullPath()+")^4)/(exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*(400.)+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*(400.)^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*(400.)^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*(400.)^4)))"))

#myTree.getNode(gpi_root+".APD_ARRAY.GAIN_ARR_1").putData(myTree.tdiCompile("50.*exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_1").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_1").getFullPath()+")^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_1").getFullPath()+")^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_1").getFullPath()+")^4)/(exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*(400.)+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*(400.)^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*(400.)^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*(400.)^4))"))



myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.ACQ196.ACTIVE_CHAN").putData(96)
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.ACQ196.CLOCK_FREQ").putData(200000)
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.ACQ196.COMMENT").putData("GPI 196 note no a-to-d's, only analogue out (ao)")
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.ACQ196.DI3").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY:T_START"))
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.ACQ196.DI3.BUS").putData("fpga pxi")
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.ACQ196.DI3.WIRE").putData("lemo")
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.ACQ196.NODE").putData("192.168.0.155")
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.ACQ196.POST_TRIG").putData(myTree.tdiCompile("INT(("+gpi_root+".APD_ARRAY:T_STOP - "+gpi_root+".APD_ARRAY:T_START) * 200000 / 1024)"))

myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.ACQ196AO.FAWG_DIV").putData(20)
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.ACQ196AO.DI2").putData(myTree.tdiCompile("* : * : 1 / 200000."))
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.ACQ196AO.DI3").putData(0.)
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.ACQ196AO.NODE").putData("192.168.0.155")

myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DIO2.SW_MODE").putData("REMOTE")
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DIO2.IP_ADDR").putData("192.168.0.155:8106")
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DIO2.CHANNEL_2.COMMENT").putData("trigger for outerwall APD system")
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DIO2.CHANNEL_2.CYCLIC").putData("NO")
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DIO2.CHANNEL_2.DELAY").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY:T_START - "+gpi_root+".APD_ARRAY.HARDWARE:DIO2.CHANNEL_2:TRIGGER"))
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DIO2.CHANNEL_2.DURATION").putData(10E-6)
#myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DIO2.CHANNEL_2.EVENT").putData(myTree.tdiCompile("["START             ","SPECTROSCOPY_START"]"))
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DIO2.CHANNEL_2.EVENT").putData(myTree.getNode("gpi.apd_array.hardware.dio2.channel_2.event").getData()) # THIS NEEDS TO BE CORRECTED
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DIO2.CHANNEL_2.FUNCTION").putData("PULSE")
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DIO2.CHANNEL_2.INIT_LEVEL_1").putData("LOW")
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DIO2.CHANNEL_2.INIT_LEVEL_2").putData("HIGH")
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DIO2.CHANNEL_2.TRIGGER").putData(myTree.tdiCompile("\SPECTROSCOPY::TSTART")) # THIS NEEDS TO BE SPECIFIED
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DIO2.CHANNEL_2.TRIGGER_1").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY.HARDWARE:DIO2.CHANNEL_2:TRIGGER + "+gpi_root+".APD_ARRAY.HARDWARE:DIO2.CHANNEL_2:DELAY"))
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DIO2.CHANNEL_2.TRIGGER_2").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY.HARDWARE:DIO2.CHANNEL_2:TRIGGER + "+gpi_root+".APD_ARRAY.HARDWARE:DIO2.CHANNEL_2:DELAY + "+gpi_root+".APD_ARRAY.HARDWARE:DIO2.CHANNEL_2:DURATION"))
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DIO2.CHANNEL_2.TRIG_MODE").putData("SOFTWARE")

myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DT132_1.ACTIVE_CHAN").putData(32)
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DT132_1.CLOCK_FREQ").putData(200000)
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DT132_1.COMMENT").putData("Dtaq 32-channel 2 MSPS digitizer")
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DT132_1.DI0").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY.HARDWARE:DIO2.CHANNEL_1:CLOCK"))
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DT132_1.DI0.BUS").putData("fpga pxi")
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DT132_1.DI0.WIRE").putData("lemo")
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DT132_1.DI1").putData(myTree.tdiCompile("* : * : 1D0 / "+gpi_root+".APD_ARRAY.HARDWARE:DT132_1:CLOCK_FREQ"))
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DT132_1.DI1.BUS").putData("pxi")
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DT132_1.DI1.WIRE").putData("fpga")
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DT132_1.DI3").putData(myTree.tdiCompile("D_FLOAT("+gpi_root+".APD_ARRAY.HARDWARE:DIO2.CHANNEL_2:TRIGGER_2)"))
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DT132_1.DI3.BUS").putData("fpga pxi")
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DT132_1.DI3.WIRE").putData("mezz")
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DT132_1.NODE").putData("192.168.0.40")
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DT132_1.POST_TRIG").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY:DIG_SAMPS"))

myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DT132_2.ACTIVE_CHAN").putData(32)
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DT132_2.CLOCK_FREQ").putData(200000)
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DT132_2.COMMENT").putData("Dtaq 32-channel 2 MSPS digitizer")
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DT132_2.DI3").putData(myTree.tdiCompile("D_FLOAT("+gpi_root+".APD_ARRAY.HARDWARE:DIO2.CHANNEL_2:TRIGGER_2)"))
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DT132_2.DI3.BUS").putData("fpga")
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DT132_2.DI3.WIRE").putData("lemo")
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DT132_2.NODE").putData("192.168.0.41")
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DT132_2.POST_TRIG").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY:DIG_SAMPS"))

myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DT132_3.ACTIVE_CHAN").putData(32)
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DT132_3.CLOCK_FREQ").putData(200000)
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DT132_3.DI0").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY.HARDWARE:DT132_1:DI0"))
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DT132_3.DI0.BUS").putData("none")
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DT132_3.DI0.WIRE").putData("pxi")
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DT132_3.DI3").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY.HARDWARE:DT132_1:DI3"))
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DT132_3.DI3.BUS").putData("fpga")
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DT132_3.DI3.WIRE").putData("lemo")
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DT132_3.NODE").putData("192.168.0.4")
myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DT132_3.POST_TRIG").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY:DIG_SAMPS"))

myTree.write() #save the edited tree
myTree.close() #close the tree
