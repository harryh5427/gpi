"""

"""
from MDSplus import *
import numpy as np
import sys
import matplotlib.pyplot as plt

s=int(sys.argv[1])
myTree=Tree("spectroscopy",s)
plt.xlabel('Time (sec)')
plt.ylabel('Signal (V)')
line=[]
for i in range (1,5):
    if i<4:
        node_sig=myTree.getNode("GPI.APD_ARRAY.HARDWARE:DT132_"+str(i)+".INPUT_01")
    else:
        node_sig=myTree.getNode("GPI.INNER_APD.HARDWARE:ACQ132_"+str(i)+".INPUT_01")
    signal=node_sig.getData().data()
    t=node_sig.dim_of().data()
    line.append(plt.plot(t,signal,".-",label="DT132_"+str(i)))

ind_zero_first=0
ind_zero_last=0
for i in range(0,len(signal)-1):
    if np.mean(signal[0:i])>0.5 and signal[i]<0.5 and t[i]>0.0001:
        ind_zero_first=i
        break
    if np.mean(signal[0:i])<0.8 and signal[i]>0.8 and t[i]>0.0001:
        ind_zero_first=i
        break

for i in range(len(signal)-1,0,-1):
    if np.mean(signal[0:i])>0.5 and signal[i]<0.5 and t[i]>0.0001:
        ind_zero_last=i
        break
    if np.mean(signal[0:i])<0.8 and signal[i]>0.8 and t[i]>0.0001:
        ind_zero_last=i
        break

t_zero=t[ind_zero_first]
width=0.000005
print(str(t_zero))
plt.legend(line,('DT132_1','DT132_2','DT132_3','DT132_4'))
#plt.xlim(t_zero-width,t_zero+width)
#plt.xlim(0.,0.01)

plt.show()

