"""

"""
from MDSplus import *
import sys
import numpy as np
import matplotlib.pyplot as plt

s=int(sys.argv[1])
myTree=Tree("spectroscopy",s)
for i in range(1,33):
    if i<10:
        node_sig=myTree.getNode("GPI.APD_ARRAY.HARDWARE:ACQ196.INPUT_0"+str(i))
    else:
        node_sig=myTree.getNode("GPI.APD_ARRAY.HARDWARE:ACQ196.INPUT_"+str(i))
    sig=node_sig.getData().data()
    t=node_sig.dim_of().data()
    print("Input "+str(i)+": "+str(np.mean(sig)))

