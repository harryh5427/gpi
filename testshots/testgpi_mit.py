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
import sys
import time

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
#myACQ132_2=myTree.getNode("GPI.APD_ARRAY.HARDWARE:DT132_2")
#inst_ACQ132_2=ACQ132(myACQ132_2)
#inst_ACQ132_2.initftp()

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
#inst_ACQ132_3.store()

#print("Stored data on ACQ132_3")

#inst_ACQ132_2.store()

inst_ACQ196.store()
print("Stored data on ACQ196")
