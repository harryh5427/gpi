from MDSplus import *
import numpy as np
import sys
import matplotlib.pyplot as plt

s1=1180613519
s2=1180613520
s3=1180613523 #right after the power cycling
s=s2
myTree=Tree("spectroscopy",s)

HV_prog=myTree.getNode("GPI.APD_ARRAY.HARDWARE:ACQ196AO.OUTPUT_01").getData().data()
t_prog=myTree.getNode("GPI.APD_ARRAY.HARDWARE:ACQ196AO.OUTPUT_01").dim_of().data()
HV_meas=myTree.getNode("GPI.APD_ARRAY.HARDWARE:ACQ196.INPUT_01").getData().data()
t_meas=myTree.getNode("GPI.APD_ARRAY.HARDWARE:ACQ196.INPUT_01").dim_of().data()
dig1=myTree.getNode("GPI.APD_ARRAY.HARDWARE:DT132_1.INPUT_01").getData().data()
t1=myTree.getNode("GPI.APD_ARRAY.HARDWARE:DT132_1.INPUT_01").dim_of().data()

plt.plot(t_prog,HV_prog,".-")
plt.plot(t_meas,HV_meas,".-")
plt.plot(t1,dig1,".-")
plt.show()

