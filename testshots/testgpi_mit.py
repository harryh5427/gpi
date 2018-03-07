"""
Testshot script for getting GPI equipment ready while still at MIT.

Usage : 
python testgpi_mit.py 1180227500


Harry Han, Feb 27, 2018
"""
from MDSplus import *
from MitDevices.acq132 import ACQ132
import sys
import time

s=int(sys.argv[1])
myTree=Tree("spectroscopy",-1)
myTree.createPulse(s) #Copies the model tree
myTree=Tree("spectroscopy",s)
myDIO2=myTree.getNode("GPI.APD_ARRAY.HARDWARE:DIO2")

myTree.tcl('do /meth '+myDIO2.getFullPath()+' init')


myACQ132=myTree.getNode("GPI.APD_ARRAY.HARDWARE:DT132_3")
inst_ACQ132=ACQ132(myACQ132)
inst_ACQ132.initftp()


#Wait for the initialization
time.sleep(7)

#Trigger DIO2 in order to start the data acquisition
myTree.tcl('do /meth '+myDIO2.getFullPath()+' trigger')

#Wait for shot to end
time.sleep(7)

#Store data to the MDSplus tree
inst_ACQ132.store()
