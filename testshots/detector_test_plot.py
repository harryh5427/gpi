"""

"""
from MDSplus import *
import numpy as np
import sys
import matplotlib.pyplot as plt

s=int(sys.argv[1])
#s=1180503501 #detector 1~12 (numbering: the label on fibers)
#s=1180503502 #detector 13~24 (numbering: the label on fibers)
#s=1180503503 #detector 25~30 (numbering: the label on fibers)
#s=1180509501 #detector 1~12 of Board 26 (numbering: the label on fibers)
#s=1180509502 #detector 13~24 of Board 26 (numbering: the label on fibers)
#s=1180509503 #detector 25~30 of Board 26 (numbering: the label on fibers)
#s=1180509506 #detector 1~12 of Board 24 (numbering: the label on fibers)
#s=1180509507 #detector 13~24 of Board 24 (numbering: the label on fibers)
#s=1180509508 #detector 25~30 of Board 24 (numbering: the label on fibers)
myTree=Tree("spectroscopy",s)
plt.xlabel('Time (sec)')
plt.ylabel('Signal (V)')
line=[]
det_exposed=[]
for i in range (1,16):
    if i<10:
        node_sig=myTree.getNode("GPI.APD_ARRAY.HARDWARE:DT132_1.INPUT_0"+str(i))
    else:
        node_sig=myTree.getNode("GPI.APD_ARRAY.HARDWARE:DT132_1.INPUT_"+str(i))
    sig=node_sig.getData().data()
    t=node_sig.dim_of().data()
    if i!=16 and i!=17:# and np.mean(sig)<0.9:
        line.append(plt.plot(t,sig,label="DT132_"+str(i)))
        det_exposed.append(i)

#plt.legend(line,('DT132_1','DT132_2','DT132_3','DT132_4'))
plt.ylim(-3.,1.)
print("det_exposed: "+str(det_exposed))
plt.show()

