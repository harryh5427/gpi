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
        print("Type y if you are ready.")
    elif data==1:
        break
        
gpi_root="\SPECTROSCOPY::TOP.GPI_TCV"
HV_prog=np.linspace(2.5,4.5,num_shot)
HV_meas=[[],[],[],[],[],[],[],[]]
filter_used="DA"

modelTree_num=int(str(1)+now.strftime("%y%m%d")+str(600))
modelTree=Tree("spectroscopy",modelTree_num,'Edit')

for i in range (1,num_shot*2+1):
    s=int(str(1)+now.strftime("%y%m%d")+str(600+i))
    print("Current shot number: "+str(s))



    myTree=Tree("spectroscopy",-1)
    myTree.createPulse(s) #Copies the model tree
    myTree=Tree("spectroscopy",s,'Edit')
    myTree.addNode("\SPECTROSCOPY::TOP.GPI_TCV","structure")
    gpi_root="\SPECTROSCOPY::TOP.GPI_TCV"
    gpi_node=myTree.getNode(gpi_root)
    myTree.addNode(gpi_root+".APD_ARRAY","structure")
    node_apd_array=myTree.getNode(gpi_root+".APD_ARRAY")
    node_apd_array.addNode(".T_START","numeric")
    node_apd_array.addNode(".T_STOP","numeric")
    node_apd_array.addNode(".DIG_FREQ","numeric")
    node_apd_array.addNode(".DIG_SAMPS","numeric")
    node_apd_array.addNode(".HARDWARE","structure")
    node_hardware=myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE")

    node_hardware.addDevice("ACQ196","acq196")
    node_hardware.addDevice("ACQ196AO","acq196ao")
    node_hardware.addDevice("DIO2","dio2")
    node_hardware.addDevice("DT132_1","acq132")
    node_hardware.addDevice("DT132_2","acq132")
    node_hardware.addDevice("DT132_3","acq132")
    node_hardware.addDevice("DT132_4","acq132")

    node_apd_array.addNode("HV_PROG_1","numeric")
    node_apd_array.addNode("HV_PROG_2","numeric")
    node_apd_array.addNode("HV_PROG_3","numeric")
    node_apd_array.addNode("HV_PROG_4","numeric")
    node_apd_array.addNode("HV_PROG_5","numeric")
    node_apd_array.addNode("HV_PROG_6","numeric")
    node_apd_array.addNode("HV_PROG_7","numeric")
    node_apd_array.addNode("HV_PROG_8","numeric")
    node_apd_array.addNode("HV_MEAS_1","numeric")
    node_apd_array.addNode("HV_MEAS_2","numeric")
    node_apd_array.addNode("HV_MEAS_3","numeric")
    node_apd_array.addNode("HV_MEAS_4","numeric")
    node_apd_array.addNode("HV_MEAS_5","numeric")
    node_apd_array.addNode("HV_MEAS_6","numeric")
    node_apd_array.addNode("HV_MEAS_7","numeric")
    node_apd_array.addNode("HV_MEAS_8","numeric")
    node_apd_array.addNode("S_LAMBDA_DA","numeric")
    node_apd_array.addNode("S_LAMBDA_HA","numeric")
    node_apd_array.addNode("S_LAMBDA_HEI","numeric")
    node_apd_array.addNode("COEF_0TH_ARR","numeric")
    node_apd_array.addNode("COEF_1ST_ARR","numeric")
    node_apd_array.addNode("COEF_2ND_ARR","numeric")
    node_apd_array.addNode("COEF_3RD_ARR","numeric")
    node_apd_array.addNode("COEF_4TH_ARR","numeric")
    node_apd_array.addNode("IDEN_ARR_1","numeric")
    node_apd_array.addNode("IDEN_ARR_2","numeric")
    node_apd_array.addNode("IDEN_ARR_3","numeric")
    node_apd_array.addNode("IDEN_ARR_4","numeric")
    node_apd_array.addNode("IDEN_ARR_5","numeric")
    node_apd_array.addNode("IDEN_ARR_6","numeric")
    node_apd_array.addNode("IDEN_ARR_7","numeric")
    node_apd_array.addNode("IDEN_ARR_8","numeric")
    node_apd_array.addNode("GAIN_ARR","numeric")

    myTree.getNode(gpi_root+".APD_ARRAY.HV_PROG_1").putData(myTree.tdiCompile(myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.ACQ196AO.OUTPUT_01").getFullPath()))
    myTree.getNode(gpi_root+".APD_ARRAY.HV_PROG_2").putData(myTree.tdiCompile(myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.ACQ196AO.OUTPUT_02").getFullPath()))
    myTree.getNode(gpi_root+".APD_ARRAY.HV_PROG_3").putData(myTree.tdiCompile(myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.ACQ196AO.OUTPUT_03").getFullPath()))
    myTree.getNode(gpi_root+".APD_ARRAY.HV_PROG_4").putData(myTree.tdiCompile(myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.ACQ196AO.OUTPUT_04").getFullPath()))
    myTree.getNode(gpi_root+".APD_ARRAY.HV_PROG_5").putData(myTree.tdiCompile(myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.ACQ196AO.OUTPUT_05").getFullPath()))
    myTree.getNode(gpi_root+".APD_ARRAY.HV_PROG_6").putData(myTree.tdiCompile(myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.ACQ196AO.OUTPUT_06").getFullPath()))
    myTree.getNode(gpi_root+".APD_ARRAY.HV_PROG_7").putData(myTree.tdiCompile(myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.ACQ196AO.OUTPUT_07").getFullPath()))
    myTree.getNode(gpi_root+".APD_ARRAY.HV_PROG_8").putData(myTree.tdiCompile(myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.ACQ196AO.OUTPUT_08").getFullPath()))
    myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_1").putData(myTree.tdiCompile(myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.ACQ196.INPUT_01").getFullPath()))
    myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_2").putData(myTree.tdiCompile(myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.ACQ196.INPUT_02").getFullPath()))
    myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_3").putData(myTree.tdiCompile(myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.ACQ196.INPUT_03").getFullPath()))
    myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_4").putData(myTree.tdiCompile(myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.ACQ196.INPUT_04").getFullPath()))
    myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_5").putData(myTree.tdiCompile(myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.ACQ196.INPUT_05").getFullPath()))
    myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_6").putData(myTree.tdiCompile(myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.ACQ196.INPUT_06").getFullPath()))
    myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_7").putData(myTree.tdiCompile(myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.ACQ196.INPUT_07").getFullPath()))
    myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_8").putData(myTree.tdiCompile(myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.ACQ196.INPUT_08").getFullPath()))

    myTree.getNode(gpi_root+".APD_ARRAY.IDEN_ARR_1").putData(myTree.tdiCompile("[[1.,1.,1.,1.,1.,1.,1.,1.,1.,1.],[1.,1.,1.,1.,1.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]]"))
    myTree.getNode(gpi_root+".APD_ARRAY.IDEN_ARR_2").putData(myTree.tdiCompile("[[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,1.,1.,1.,1.,1.],[1.,1.,1.,1.,1.,1.,1.,1.,1.,1.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]]"))
    myTree.getNode(gpi_root+".APD_ARRAY.IDEN_ARR_3").putData(myTree.tdiCompile("[[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[1.,1.,1.,1.,1.,1.,1.,1.,1.,1.],[1.,1.,1.,1.,1.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]]"))
    myTree.getNode(gpi_root+".APD_ARRAY.IDEN_ARR_4").putData(myTree.tdiCompile("[[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,1.,1.,1.,1.,1.],[1.,1.,1.,1.,1.,1.,1.,1.,1.,1.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]]"))
    myTree.getNode(gpi_root+".APD_ARRAY.IDEN_ARR_5").putData(myTree.tdiCompile("[[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[1.,1.,1.,1.,1.,1.,1.,1.,1.,1.],[1.,1.,1.,1.,1.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]]"))
    myTree.getNode(gpi_root+".APD_ARRAY.IDEN_ARR_6").putData(myTree.tdiCompile("[[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,1.,1.,1.,1.,1.],[1.,1.,1.,1.,1.,1.,1.,1.,1.,1.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]]"))
    myTree.getNode(gpi_root+".APD_ARRAY.IDEN_ARR_7").putData(myTree.tdiCompile("[[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[1.,1.,1.,1.,1.,1.,1.,1.,1.,1.],[1.,1.,1.,1.,1.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]]"))
    myTree.getNode(gpi_root+".APD_ARRAY.IDEN_ARR_8").putData(myTree.tdiCompile("[[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.,1.,1.,1.,1.,1.],[1.,1.,1.,1.,1.,1.,1.,1.,1.,1.]]"))

    myTree.getNode(gpi_root+".APD_ARRAY.GAIN_ARR").putData(myTree.tdiCompile(myTree.getNode(gpi_root+".APD_ARRAY.IDEN_ARR_1").getFullPath()+"*(50.*exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_1").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_1").getFullPath()+")^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_1").getFullPath()+")^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_1").getFullPath()+")^4)/(exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*(400.)+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*(400.)^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*(400.)^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*(400.)^4)))+"+myTree.getNode(gpi_root+".APD_ARRAY.IDEN_ARR_2").getFullPath()+"*(50.*exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_2").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_2").getFullPath()+")^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_2").getFullPath()+")^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_2").getFullPath()+")^4)/(exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*(400.)+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*(400.)^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*(400.)^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*(400.)^4)))+"+myTree.getNode(gpi_root+".APD_ARRAY.IDEN_ARR_3").getFullPath()+"*(50.*exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_3").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_3").getFullPath()+")^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_3").getFullPath()+")^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_3").getFullPath()+")^4)/(exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*(400.)+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*(400.)^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*(400.)^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*(400.)^4)))+"+myTree.getNode(gpi_root+".APD_ARRAY.IDEN_ARR_4").getFullPath()+"*(50.*exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_4").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_4").getFullPath()+")^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_4").getFullPath()+")^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_4").getFullPath()+")^4)/(exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*(400.)+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*(400.)^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*(400.)^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*(400.)^4)))+"+myTree.getNode(gpi_root+".APD_ARRAY.IDEN_ARR_5").getFullPath()+"*(50.*exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_5").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_5").getFullPath()+")^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_5").getFullPath()+")^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_5").getFullPath()+")^4)/(exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*(400.)+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*(400.)^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*(400.)^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*(400.)^4)))+"+myTree.getNode(gpi_root+".APD_ARRAY.IDEN_ARR_6").getFullPath()+"*(50.*exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_6").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_6").getFullPath()+")^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_6").getFullPath()+")^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_6").getFullPath()+")^4)/(exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*(400.)+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*(400.)^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*(400.)^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*(400.)^4)))+"+myTree.getNode(gpi_root+".APD_ARRAY.IDEN_ARR_7").getFullPath()+"*(50.*exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_7").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_7").getFullPath()+")^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_7").getFullPath()+")^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_7").getFullPath()+")^4)/(exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*(400.)+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*(400.)^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*(400.)^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*(400.)^4)))+"+myTree.getNode(gpi_root+".APD_ARRAY.IDEN_ARR_8").getFullPath()+"*(50.*exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_8").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_8").getFullPath()+")^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_8").getFullPath()+")^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_8").getFullPath()+")^4)/(exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*(400.)+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*(400.)^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*(400.)^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*(400.)^4)))"))

    #myTree.getNode(gpi_root+".APD_ARRAY.GAIN_ARR_1").putData(myTree.tdiCompile("50.*exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_1").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_1").getFullPath()+")^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_1").getFullPath()+")^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*("+myTree.getNode(gpi_root+".APD_ARRAY.HV_MEAS_1").getFullPath()+")^4)/(exp(("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR").getFullPath()+")+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR").getFullPath()+")*(400.)+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR").getFullPath()+")*(400.)^2+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_3RD_ARR").getFullPath()+")*(400.)^3+("+myTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR").getFullPath()+")*(400.)^4))"))

    myTree.getNode(gpi_root+".APD_ARRAY.T_START").putData(0.)
    myTree.getNode(gpi_root+".APD_ARRAY.T_STOP").putData(.9)
    myTree.getNode(gpi_root+".APD_ARRAY.DIG_FREQ").putData(2.)
    myTree.getNode(gpi_root+".APD_ARRAY.DIG_SAMPS").putData(myTree.tdiCompile("_tstart = "+gpi_root+".APD_ARRAY:T_START, _tstop = "+gpi_root+".APD_ARRAY:T_STOP, _freq = "+gpi_root+".APD_ARRAY:DIG_FREQ, _nksamp = (_tstop - _tstart) * _freq * 1000E3 / 1024 + .5, _ksamp_int = INT(_nksamp)"))

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
    myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.ACQ196AO.DI2").putData(0.)
    myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.ACQ196AO.NODE").putData("192.168.0.155")

    myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DIO2.SW_MODE").putData("REMOTE")
    myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DIO2.IP_ADDR").putData("192.168.0.155:8106")
    myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DIO2.CHANNEL_2.COMMENT").putData("trigger for outerwall APD system")
    myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DIO2.CHANNEL_2.CYCLIC").putData("NO")
    myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DIO2.CHANNEL_2.DELAY").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY:T_START - "+gpi_root+".APD_ARRAY.HARDWARE:DIO2.CHANNEL_2:TRIGGER"))
    myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DIO2.CHANNEL_2.DURATION").putData(10E-6)
    myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE.DIO2.CHANNEL_2.EVENT").putData(myTree.tdiCompile("["START             ","SPECTROSCOPY_START"]"))
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






    if i<=num_shot:    
        HV_prog_i=random.choice(HV_prog)
        HV_prog=np.delete(HV_prog,np.where(HV_prog==HV_prog_i))
    if i>num_shot:
        myTree_with_light=Tree("spectroscopy",s-num_shot)
        HV_prog_i=myTree_with_light.getNode(gpi_root+".APD_ARRAY.HV_PROG_1")
    sig=myTree.tdiCompile("Build_Signal(["+str(HV_prog_i)+","+str(HV_prog_i)+","+str(HV_prog_i)+","+str(HV_prog_i)+","+str(HV_prog_i)+","+str(HV_prog_i)+","+str(HV_prog_i)+","+str(HV_prog_i)+","+str(HV_prog_i)+","+str(HV_prog_i)+","+str(HV_prog_i)+"], *, 0 : .1 : .01)")
    for j in range (1,9):
#        myTree.getNode(gpi_root+".APD_ARRAY.HV_PROG_"+str(j)).putData(HV_prog_i)
        for k in range (1,17):
            if k < 10:
                Output_node=myTree.getNode(gpi_root+".apd_array.hardware:acq196ao.output_0"+str(k))
            else:
                Output_node=myTree.getNode(gpi_root+".apd_array.hardware:acq196ao.output_"+str(k))
            Output_node.putData(sig)

    #Initialize DIO2 through TCL command, since there is no working python command for DIO2
    #DIO2_ENCDEC does not work for this, neither does DIO4
    myDIO2=myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE:DIO2")
    myTree.tcl('do /meth '+myDIO2.getFullPath()+' init')
    print("Initialized DIO2")

    #Take node of each digitizer, and initialize them
#    myACQ132_1=myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE:DT132_1")
#    inst_ACQ132_1=ACQ132(myACQ132_2)
#    inst_ACQ132_1.initftp()
#    print("Initialized ACQ132_1")
#    myACQ132_2=myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE:DT132_2")
#    inst_ACQ132_2=ACQ132(myACQ132_2)
#    inst_ACQ132_2.initftp()
#    print("Initialized ACQ132_2")
    myACQ132_3=myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE:DT132_3")
    inst_ACQ132_3=ACQ132(myACQ132_3)
    inst_ACQ132_3.initftp()
    print("Initialized ACQ132_3")
#    myACQ132_4=myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE:DT132_4")
#    inst_ACQ132_4=ACQ132(myACQ132_4)
#    inst_ACQ132_4.initftp()
#    print("Initialized ACQ132_4")
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
#    inst_ACQ132_1.store()
#    print("Stored data on ACQ132_1")
#    inst_ACQ132_2.store()
#    print("Stored data on ACQ132_2")
    inst_ACQ132_3.store()
    print("Stored data on ACQ132_3")
#    inst_ACQ132_4.store()
#    print("Stored data on ACQ132_4")
    inst_ACQ196.store()
    print("Stored data on ACQ196")
    
    sig_arr=[[],[],[],[],[],[],[],[],[],[],[],[]] #10 by 12 array
    for j in range (1,31):
        if j<10:
            sig_node_1=myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE:DT132_1.INPUT_0"+str(j))
            sig_node_2=myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE:DT132_2.INPUT_0"+str(j))
            sig_node_3=myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE:DT132_3.INPUT_0"+str(j))
            sig_node_4=myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE:DT132_4.INPUT_0"+str(j))
        else:
            sig_node_1=myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE:DT132_1.INPUT_"+str(j))
            sig_node_2=myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE:DT132_2.INPUT_"+str(j))
            sig_node_3=myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE:DT132_3.INPUT_"+str(j))
            sig_node_4=myTree.getNode(gpi_root+".APD_ARRAY.HARDWARE:DT132_4.INPUT_"+str(j))
        sig_arr[(j-1)/10].append(0.) #Col 1,2,3 (30 APDs)
        sig_arr[3+(j-1)/10].append(0.) #Col 4,5,6 (30 APDs)
        sig_arr[6+(j-1)/10].append(np.mean(sig_node_3.getData().data())) #Col 7,8,9 (30 APDs)
        sig_arr[9+(j-1)/10].append(0.) #Col 10,11,12 (30 APDs)
    myTree.getNode(gpi_root+".APD_ARRAY").addNode("SENS_ARR_"+str(filter_used),"numeric") #Temporarily make the nodes for the sensitivity arrays, just for the calibration shots. Will be deleted at the end of the script.
    node_sens_arr=myTree.getNode(gpi_root+".APD_ARRAY.SENS_ARR_"+str(filter_used))
    if i<=num_shot:
        node_sens_arr.putData(sig_arr) #Temporarily store the signal (of the shot with labsphere) in the sens_arr_da node
    if i>num_shot:
        node_sens_arr_with_light=myTree_with_light.getNode(gpi_root+".APD_ARRAY.SENS_ARR_"+str(filter_used))
        sig_minus_back_arr=-node_sens_arr_da_with_light.getData()+sig_arr
        myTree.getNode(gpi_root+".APD_ARRAY").addNode("SIG_MINUS_BACK_ARR","numeric") #Temporarily make the node for the signal-background array, just for the calibration shots. Will be deleted at the end of the script.
        myTree.getNode(gpi_root+".APD_ARRAY.SIG_MINUS_BACK_ARR").putData(sig_minus_back_arr)
        
        
        #From the logbook entry 1110518, the spectral radiance of the 'old' Labsphere at 6550 A is 0.632 mW/cm^2/ster/micron=0.632 microW/cm^2/ster/nm=0.0632 microW/cm^2/ster/A
        rad_da=0.0632/1000. #convert uW/cm^2/ster/A to mW/cm^2/ster/A
        #The spectral radiance of the 'old' Labsphere at 5876 A is 0.0461 uW/cm^2/ster/A
        rad_hei=0.0461/1000. #convert uW/cm^2/ster/A to mW/cm^2/ster/A
        bandpass_da=116.78 #unit : A
        bandpass_hei=114.52 #unit : A
        avg_transf_func_da=1.
        avg_transf_func_hei=1.
        if filter_used=="DA":
            sensitivity=rad_da*avg_transf_func_da*bandpass_da/(sig_minus_back/1000.)
        if filter_used=="HEI":
            sensitivity=rad_hei*avg_transf_func_hei*bandpass_hei/(sig_minus_back/1000.)
        node_sens_arr.putData(sensitivity)
        
        #Save the HV_meas values
        HV_meas[0].append(np.mean(myTree_with_light.getNode(gpi_root+".APD_ARRAY.HV_MEAS_1").getData().data()))
        HV_meas[1].append(np.mean(myTree_with_light.getNode(gpi_root+".APD_ARRAY.HV_MEAS_2").getData().data()))
        HV_meas[2].append(np.mean(myTree_with_light.getNode(gpi_root+".APD_ARRAY.HV_MEAS_3").getData().data()))
        HV_meas[3].append(np.mean(myTree_with_light.getNode(gpi_root+".APD_ARRAY.HV_MEAS_4").getData().data()))
        HV_meas[4].append(np.mean(myTree_with_light.getNode(gpi_root+".APD_ARRAY.HV_MEAS_5").getData().data()))
        HV_meas[5].append(np.mean(myTree_with_light.getNode(gpi_root+".APD_ARRAY.HV_MEAS_6").getData().data()))
        HV_meas[6].append(np.mean(myTree_with_light.getNode(gpi_root+".APD_ARRAY.HV_MEAS_7").getData().data()))
        HV_meas[7].append(np.mean(myTree_with_light.getNode(gpi_root+".APD_ARRAY.HV_MEAS_8").getData().data()))
        
    if i==num_shot:
        while True:
            data = input("Now, "+str(num_shot)+" testshots WITHOUT the labsphere will be taken. Is the labsphere off? (yes=1/no=0):")
            if data==0:
                print("Type y if you are ready.")
            elif data==1:
                break

dummy_arr=sig_minus_back_arr #Just to copy the size of the array
for i in range (0,12):
    for j in range (0,10):
        dummy_arr[i][j]=0.
node_coef_0th=modelTree.getNode(gpi_root+".APD_ARRAY.COEF_0TH_ARR")
node_coef_1st=modelTree.getNode(gpi_root+".APD_ARRAY.COEF_1ST_ARR")
node_coef_2nd=modelTree.getNode(gpi_root+".APD_ARRAY.COEF_2ND_ARR")
node_coef_3rd=modelTree.getNode(gpi_root+".APD_ARRAY.COEF_3RT_ARR")
node_coef_4th=modelTree.getNode(gpi_root+".APD_ARRAY.COEF_4TH_ARR")
node_coef_0th.putData(dummy_arr)
node_coef_1st.putData(dummy_arr)
node_coef_2nd.putData(dummy_arr)
node_coef_3rd.putData(dummy_arr)
node_coef_4th.putData(dummy_arr)
node_sens_over_gain_arr=modelTree.getNode(gpi_root+".APD_ARRAY.S_LAMBDA_"+str(filter_used))
node_sens_over_gain_arr.putData(dummy_arr)

for i in range (0,120):
    sig_minus_back=[]
    for j in range (1,num_shot+1):
        yourTree=Tree("spectroscopy",s-num_shot+j)
        sig_minus_back_arr=yourTree.getNode(gpi_root+".APD_ARRAY.SIG_MINUS_BACK_ARR").getData().data()
        sig_minus_back.append(sig_minus_back_arr[i/10][i%10])
    coef=np.polyfit(HV_meas[i/15],np.log(sig_minus_back),4)
    coef_0th_arr=node_coef_0th.getData().data()
    coef_1st_arr=node_coef_1st.getData().data()
    coef_2nd_arr=node_coef_2nd.getData().data()
    coef_3rd_arr=node_coef_3rd.getData().data()
    coef_4th_arr=node_coef_4th.getData().data()
    coef_0th_arr[i/10][i%10]=coef[0]
    coef_1st_arr[i/10][i%10]=coef[1]
    coef_2nd_arr[i/10][i%10]=coef[2]
    coef_3rd_arr[i/10][i%10]=coef[3]
    coef_4th_arr[i/10][i%10]=coef[4]
    node_coef_0th.putData(coef_0th_arr)
    node_coef_1st.putData(coef_1st_arr)
    node_coef_2nd.putData(coef_2nd_arr)
    node_coef_3rd.putData(coef_3rd_arr)
    node_coef_4th.putData(coef_4th_arr)
    
    sens_over_gain=[]
    for j in range (1,num_shot+1):
        yourTree=Tree("spectroscopy",s-num_shot+j)
        sens_arr=yourTree.getNode(gpi_root+".APD_ARRAY.SENS_ARRAY_"+str(filter_used)).getData().data()
        gain_arr=yourTree.getNode(gpi_root+".APD_ARRAY.GAIN_ARR").getData().data()
        sens_over_gain.append(sens_arr[i/10][i%10]/gain_arr[i/10][i%10])
    sens_over_gain_arr=node_sens_over_gain_arr.getData().data()
    sens_over_gain_arr[i/10][i%10]=np.mean(sens_over_gain)
    node_sens_over_gain_arr.putData(sens_over_gain_arr)
    
    #ADD LINES TO DELETE THE SENSITIVITY AND SIG_MINUS_BACK NODES!
    
modelTree.write() #save the edited tree
myTree.write()
modelTree.close() #close the tree
myTree.close()
        
