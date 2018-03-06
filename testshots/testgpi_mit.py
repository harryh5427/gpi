"""
Testshot script for getting GPI equipment ready while still at MIT.

Usage : 
python testgpi_mit.py 1180227500


Harry Han, Feb 27, 2018
"""
from MDSplus import *
from MitDevices.acq132 import ACQ132
import sys

s=int(sys.argv[1])
myTree=Tree("spectroscopy",-1)
myTree.createPulse(s) #Copies the model tree
myTree=Tree("spectroscopy",s)
myDIO2=myTree.getNode("GPI.APD_ARRAY.HARDWARE:DIO2")

myTree.tcl('do /meth '+myDIO2.getFullPath()+' init')
