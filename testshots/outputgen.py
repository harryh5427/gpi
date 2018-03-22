"""
Generates outpus for \SPECTROSCOPY::TOP.GPI.APD_ARRAY.HARDWARE:ACQ196AO

Harry Han
Mar 22, 2018
"""
from MDSplus import *

myTree=Tree("spectroscopy",-1)

sig=myTree.tdiCompile("Build_Signal(0 : 10. : 1., *, 0 : .1 : .01)")
for i in range (1,17):
    if i < 10:
        Output_node=myTree.getNode("gpi.apd_array.hardware:acq196ao.output_0"+str(i))
    else:
        Output_node=myTree.getNode("gpi.apd_array.hardware:acq196ao.output_"+str(i))
    Output_node.putData(sig)
