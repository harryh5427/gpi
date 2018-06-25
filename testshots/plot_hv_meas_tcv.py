from MDSplus import *
import numpy as np
import sys
import matplotlib.pyplot as plt

s=int(sys.argv[1])
num_shot=20
hv_meas=[]
sig_minus_back=[]
for i in range (1,num_shot+1):
    tree_light=Tree("spectroscopy",s+i-1)
    tree_nolight=Tree("spectroscopy",s+num_shot+i-1)
    hv_meas_arr=tree_light.getNode('gpi_tcv.apd_array.result.hv_meas_arr').getData().data()
    hv_meas.append(hv_meas_arr[0][0])
    back=tree_nolight.getNode('gpi_tcv.apd_array.calibration.mean_sig_arr').getData().data()
    sig=tree_light.getNode('gpi_tcv.apd_array.calibration.mean_sig_arr').getData().data()
    sig_minus_back.append(back[0][0]-sig[0][0])

sort_ind=np.argsort(hv_meas)
hv_meas=np.sort(hv_meas)
temp=np.array([])
for i in range (0,len(sig_minus_back)):
    temp=np.append(temp,sig_minus_back[sort_ind[i]])
sig_minus_back=temp
coef=np.polyfit(hv_meas,np.log(sig_minus_back),4)
plt.plot(hv_meas,sig_minus_back)
plt.xlabel('HV_meas (V)')
plt.ylabel('Signal-Background')
plt.show()

