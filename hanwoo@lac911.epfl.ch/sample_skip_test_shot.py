from MDSplus import *
from MitDevices.acq132 import ACQ132
import numpy as np
import sys
import time
import matplotlib.pyplot as plt

start_shot=int(sys.argv[1])
start_inds=[]
end_inds=[]
shots_not_aligned=[]
for i in range(0,100):
    s=start_shot+i
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

    #Take node of each digitizer, and initialize them
    myACQ132_2=myTree.getNode("GPI.APD_ARRAY.HARDWARE:DT132_2")
    inst_ACQ132_2=ACQ132(myACQ132_2)
    inst_ACQ132_2.initftp()
    print("Initialized ACQ132_2")

    #Take node of each digitizer, and initialize them
    myACQ132_3=myTree.getNode("GPI.APD_ARRAY.HARDWARE:DT132_3")
    inst_ACQ132_3=ACQ132(myACQ132_3)
    inst_ACQ132_3.initftp()
    print("Initialized ACQ132_3")

    myACQ132_4=myTree.getNode("GPI.INNER_APD.HARDWARE:ACQ132_4")
    inst_ACQ132_4=ACQ132(myACQ132_4)
    inst_ACQ132_4.initftp()
    print("Initialized ACQ132_4")

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

