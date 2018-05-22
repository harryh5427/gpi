"""

"""
from MDSplus import *
import numpy as np
import matplotlib.pyplot as plt

myTree=Tree("spectroscopy",1180509505)
plt.xlabel('Time (sec)')
plt.ylabel('Signal (V)')
line=[]
for i in range (1,33):
    if i<10:
        node_sig=myTree.getNode("GPI.APD_ARRAY.HARDWARE:DT132_1.INPUT_0"+str(i))
    else:
        node_sig=myTree.getNode("GPI.APD_ARRAY.HARDWARE:DT132_1.INPUT_"+str(i))
    sig=node_sig.getData().data()
    t=node_sig.dim_of().data()
    line.append(plt.plot(t,sig,label="DT132_"+str(i)))
    print("input_"+str(i)+" : mean(sig)="+str(round(np.mean(sig),4))+" V, std(sig)="+str(round(np.std(sig),4))+" V")

#plt.legend(line,('DT132_1','DT132_2','DT132_3','DT132_4'))
plt.xlim(0.001,0.002)
plt.ylim(-3.,0.5)
plt.show()

