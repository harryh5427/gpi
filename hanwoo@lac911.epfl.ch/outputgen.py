"""
Generates outpus for \SPECTROSCOPY::TOP.GPI.APD_ARRAY.HARDWARE:ACQ196AO

Harry Han
Mar 22, 2018
"""
from MDSplus import *

myTree=Tree("spectroscopy",-1)

#sig=myTree.tdiCompile("Build_Signal(0 : 10. : 1., *, 0 : .1 : .01)")
#sig=myTree.tdiCompile("Build_Signal([3.,3.],*,[-1.,2.])")
HV_prog=4.0
#sig=myTree.tdiCompile("Build_Signal([0.,1.,1.,0.]*"+str(HV_prog)+",*,["+myTree.getNode("gpi.apd_array.hardware.DIO2.CHANNEL_5.TRIGGER_2").getFullPath()+","+myTree.getNode("gpi.apd_array.hardware.DIO2.CHANNEL_5.TRIGGER_2").getFullPath()+"+1.0,"+myTree.getNode("gpi.apd_array.T_STOP").getFullPath()+"+1.0,"+myTree.getNode("gpi.apd_array.T_STOP").getFullPath()+"+2.0])")
#sig=myTree.tdiCompile("Build_Signal([0.,1.,1.,0.]*"+str(HV_prog)+",*,[0.5,1.0,1.5,2.0])")
#sig=myTree.tdiCompile("Build_Signal([0.,0.,0.,0.]*"+str(HV_prog)+",*,[0.5,1.0,1.5,2.0])")
#sig=myTree.tdiCompile("Build_Signal([0.,1.,1.,0.]*"+str(HV_prog)+",*,["+myTree.getNode("gpi.apd_array.hardware.DIO2.CHANNEL_5.TRIGGER_1").getFullPath()+","+myTree.getNode("gpi.apd_array.hardware.DIO2.CHANNEL_5.TRIGGER_1").getFullPath()+"+1.0,"+myTree.getNode("gpi.apd_array.hardware.DIO2.CHANNEL_5.TRIGGER_1").getFullPath()+"+2.0,"+myTree.getNode("gpi.apd_array.hardware.DIO2.CHANNEL_5.TRIGGER_1").getFullPath()+"+3.0])")
#sig=myTree.tdiCompile("Build_Signal([0.,1.,1.,0.]*"+str(HV_prog)+",*,["+myTree.getNode("gpi.apd_array.hardware.DIO2.CHANNEL_5.TRIGGER_2").getFullPath()+","+myTree.getNode("gpi.apd_array.hardware.DIO2.CHANNEL_5.TRIGGER_2").getFullPath()+"+1.0,"+myTree.getNode("gpi.apd_array.T_STOP").getFullPath()+"-1.0,"+myTree.getNode("gpi.apd_array.T_STOP").getFullPath()+"])")


#sig=myTree.tdiCompile("Build_Signal([0.,0.,3.,3.,0.,0.] * 1., *, [0.,.5,1.,1.5,2.,3.])")
#sig=myTree.tdiCompile("Build_Signal([0.,0.,1.,1.,0.,0.]*"+str(HV_prog)+",*,[0.,0.5,1.5,"+myTree.getNode("gpi.apd_array.T_STOP").getFullPath()+"-"+myTree.getNode("gpi.apd_array.hardware.DIO2.CHANNEL_1.TRIGGER").getFullPath()+"+0.5,"+myTree.getNode("gpi.apd_array.T_STOP").getFullPath()+"-"+myTree.getNode("gpi.apd_array.hardware.DIO2.CHANNEL_1.TRIGGER").getFullPath()+"+1.5,+"+myTree.getNode("gpi.apd_array.T_STOP").getFullPath()+"-"+myTree.getNode("gpi.apd_array.hardware.DIO2.CHANNEL_1.TRIGGER").getFullPath()+"+2.0])")
sig=myTree.tdiCompile("Build_Signal([0.,1.,1.,0.]*"+str(HV_prog)+",*,[0.,1,"+myTree.getNode("gpi.apd_array.T_STOP").getFullPath()+"-"+myTree.getNode("gpi.apd_array.hardware.DIO2.CHANNEL_1.TRIGGER_1").getFullPath()+"+1.0,"+myTree.getNode("gpi.apd_array.T_STOP").getFullPath()+"-"+myTree.getNode("gpi.apd_array.hardware.DIO2.CHANNEL_1.TRIGGER_1").getFullPath()+"+2.0])")

for i in range (1,17):
    if i < 10:
        Output_node=myTree.getNode("gpi.apd_array.hardware:acq196ao.output_0"+str(i))
    else:
        Output_node=myTree.getNode("gpi.apd_array.hardware:acq196ao.output_"+str(i))
    Output_node.putData(sig)

