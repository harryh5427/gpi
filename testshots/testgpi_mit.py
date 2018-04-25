"""
Testshot script for getting GPI equipment ready while still at MIT.

Usage : 
python testgpi_mit.py 1180227500


Harry Han, Feb 27, 2018
"""
from MDSplus import *
from MitDevices.acq132 import ACQ132
from MitDevices.acq196 import ACQ196
from MitDevices.acq196ao import ACQ196AO
import numpy as np
import sys
import time
import matplotlib.pyplot as plt

s=int(sys.argv[1])
myTree=Tree("spectroscopy",-1)
myTree.createPulse(s) #Copies the model tree
myTree=Tree("spectroscopy",s)
myDIO2=myTree.getNode("GPI.APD_ARRAY.HARDWARE:DIO2")

#Initialize DIO2 through TCL command, since there is no working python command for DIO2
#DIO2_ENCDEC does not work for this, neither does DIO4
myTree.tcl('do /meth '+myDIO2.getFullPath()+' init')

print("Initialized DIO2")

#Take node of each digitizer, and initialize them
myACQ132_1=myTree.getNode("GPI.APD_ARRAY.HARDWARE:DT132_1")
inst_ACQ132_1=ACQ132(myACQ132_1)
inst_ACQ132_1.initftp()

print("Initialized ACQ132_1")

myACQ132_3=myTree.getNode("GPI.APD_ARRAY.HARDWARE:DT132_3")
inst_ACQ132_3=ACQ132(myACQ132_3)
inst_ACQ132_3.initftp()

print("Initialized ACQ132_3")

myACQ196=myTree.getNode("GPI.APD_ARRAY.HARDWARE:ACQ196")
inst_ACQ196=ACQ196(myACQ196)
inst_ACQ196.initftp()

print("Initialized ACQ196")

myACQ196AO=myTree.getNode("GPI.APD_ARRAY.HARDWARE:ACQ196AO")
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

inst_ACQ132_3.store()
print("Stored data on ACQ132_3")

inst_ACQ196.store()
print("Stored data on ACQ196")

for i in range (1,17):
    if i < 10:
        node_HV_prog=myTree.getNode("GPI.APD_ARRAY.HARDWARE:ACQ196AO.OUTPUT_0"+str(i))
        node_HV_meas=myTree.getNode("GPI.APD_ARRAY.HARDWARE:ACQ196.INPUT_0"+str(i))
    else:
        node_HV_prog=myTree.getNode("GPI.APD_ARRAY.HARDWARE:ACQ196AO.OUTPUT_"+str(i))
        node_HV_meas=myTree.getNode("GPI.APD_ARRAY.HARDWARE:ACQ196.INPUT_"+str(i))
    HV_prog=np.mean(node_HV_prog.getData().data())
    HV_meas=np.mean(node_HV_meas.getData().data())
    print("HV_prog for output "+str(i)+" : "+str(HV_prog))
    print("HV_meas for input "+str(i)+" : "+str(HV_meas))
for i in range (17,33):
    node_HV_meas=myTree.getNode("GPI.APD_ARRAY.HARDWARE:ACQ196.INPUT_"+str(i))
    HV_meas=np.mean(node_HV_meas.getData().data())
    print("HV_meas for input "+str(i)+" : "+str(HV_meas))

for i in range (1,33):
    if i < 10:
        node_sig=myTree.getNode("GPI.APD_ARRAY.HARDWARE:DT132_3.INPUT_0"+str(i))
    else:
        node_sig=myTree.getNode("GPI.APD_ARRAY.HARDWARE:DT132_3.INPUT_"+str(i))
    sig=np.mean(node_sig.getData().data())
    print("Input "+str(i)+": "+str(sig))
    signal=node_sig.getData().data()
    t=node_sig.dim_of().data()
    plt.plot(t,signal)
    plt.xlabel('Time (sec)')
    plt.ylabel('Signal (V)')

plt.show()
    

