"""

"""
from MDSplus import *
import numpy as np
import matplotlib.pyplot as plt

#s=1180503501 #detector 1~12 (numbering: the label on fibers)
#s=1180503502 #detector 13~24 (numbering: the label on fibers)
#s=1180503503 #detector 25~30 (numbering: the label on fibers)
#s=1180509501 #detector 1~12 of Board 26 (numbering: the label on fibers)
#s=1180509502 #detector 13~24 of Board 26 (numbering: the label on fibers)
#s=1180509503 #detector 25~30 of Board 26 (numbering: the label on fibers)
#s=1180509506 #detector 1~12 of Board 24 (numbering: the label on fibers)
#s=1180509507 #detector 13~24 of Board 24 (numbering: the label on fibers)
#s=1180509508 #detector 25~30 of Board 24 (numbering: the label on fibers)
s=[1180509501,1180509506,1180510501]
input_chan=2
plt.xlabel('Time (sec)')
plt.ylabel('HV_MEAS_'+str(input_chan)+' (V)')
line=[]
for i in range(0,len(s)):
    myTree=Tree("spectroscopy",s[i])
    node_sig=myTree.getNode("GPI.APD_ARRAY.HARDWARE:ACQ196.INPUT_0"+str(input_chan))
    sig=node_sig.getData().data()
    t=node_sig.dim_of().data()
    line.append(plt.plot(t,sig))
    print("mean sig of shot "+str(s[i])+": "+str(np.mean(sig)))
print(str(len(line)))
plt.legend(line,('Board 26','Board 24','Board 25'))
plt.xlim(xmax=15.)
plt.show()

