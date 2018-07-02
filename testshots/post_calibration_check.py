from MDSplus import *
import numpy as np
import sys
import matplotlib.pyplot as plt

"""
s=int(sys.argv[1])
myTree=Tree("spectroscopy",s)
hv_prog=myTree.getNode('gpi_tcv.apd_array.control.hv_prog_1').getData().data()
print('hv_prog='+str(hv_prog))
for i in range (1,5):
    for j in range (1,33):
        if j<16 or j>17:
            if j<10:
                sig=myTree.getNode('gpi_tcv.apd_array.hardware.acq132_'+str(i)+'.input_0'+str(j)).getData().data()
                t=myTree.getNode('gpi_tcv.apd_array.hardware.acq132_'+str(i)+'.input_0'+str(j)).dim_of().data()
            else:
                sig=myTree.getNode('gpi_tcv.apd_array.hardware.acq132_'+str(i)+'.input_'+str(j)).getData().data()
                t=myTree.getNode('gpi_tcv.apd_array.hardware.acq132_'+str(i)+'.input_'+str(j)).dim_of().data()
            print("ACQ132_"+str(i)+", Input "+str(j)+": "+str(np.mean(sig)))
            plt.plot(t,sig)

plt.ylim(0.8,1.3)
plt.ylabel('Signal (V)')
plt.show()

myTree.close() #close the tree
"""

s=1180622500 #old 'old fiber' shots

num_shot=20

hv_prog=[]
for i in range (1,num_shot+1):
    myTree_with_light=Tree("spectroscopy",s+i)
    hv_prog.append(myTree_with_light.getNode('gpi_tcv.apd_array.control.hv_prog_1').getData().data())

min_ind=np.argmin(hv_prog)
max_ind=np.argmax(hv_prog)

myTree_min_light=Tree("spectroscopy",s+1+min_ind)
myTree_max_light=Tree("spectroscopy",s+1+max_ind)
gain_arr_min=myTree_min_light.getNode("gpi_tcv.APD_ARRAY.RESULT.GAIN_ARR").getData().data()
gain_arr_max=myTree_max_light.getNode("gpi_tcv.APD_ARRAY.RESULT.GAIN_ARR").getData().data()
gain_arr_diff=gain_arr_max-gain_arr_min
print(gain_arr_diff)

#s=1180626500 #old 'new fiber' shots
s=1180702500 #recent 'new fiber' shots
num_shot=20

hv_prog=[]
for i in range (1,num_shot+1):
    myTree_with_light=Tree("spectroscopy",s+i)
    hv_prog.append(myTree_with_light.getNode('gpi_tcv.apd_array.control.hv_prog_1').getData().data())

min_ind=np.argmin(hv_prog)
max_ind=np.argmax(hv_prog)

myTree_min_light=Tree("spectroscopy",s+1+min_ind)
myTree_max_light=Tree("spectroscopy",s+1+max_ind)
gain_arr_min=myTree_min_light.getNode("gpi_tcv.APD_ARRAY.RESULT.GAIN_ARR").getData().data()
gain_arr_max=myTree_max_light.getNode("gpi_tcv.APD_ARRAY.RESULT.GAIN_ARR").getData().data()
gain_arr_diff=gain_arr_max-gain_arr_min
print(gain_arr_diff)



s=1180622500 #old 'old fiber' shots
HV_meas_old=[[],[],[],[],[],[],[],[]]
HV_prog_old=[[],[],[],[],[],[],[],[]]
for i in range (1,num_shot+1):
    myTree_with_light=Tree("spectroscopy",s+i)
    HV_meas_arr=200.*myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.HV_MEAS_ARR").getData().data()
    HV_meas_old[0].append(HV_meas_arr[0][0])
    HV_meas_old[1].append(HV_meas_arr[1][5])
    HV_meas_old[2].append(HV_meas_arr[3][0])
    HV_meas_old[3].append(HV_meas_arr[4][5])
    HV_meas_old[4].append(HV_meas_arr[6][0])
    HV_meas_old[5].append(HV_meas_arr[7][5])
    HV_meas_old[6].append(HV_meas_arr[9][0])
    HV_meas_old[7].append(HV_meas_arr[10][5])
    HV_prog_old[0].append(myTree_with_light.getNode("gpi_tcv.APD_ARRAY.CONTROL.HV_PROG_1").getData().data())
    HV_prog_old[1].append(myTree_with_light.getNode("gpi_tcv.APD_ARRAY.CONTROL.HV_PROG_2").getData().data())
    HV_prog_old[2].append(myTree_with_light.getNode("gpi_tcv.APD_ARRAY.CONTROL.HV_PROG_3").getData().data())
    HV_prog_old[3].append(myTree_with_light.getNode("gpi_tcv.APD_ARRAY.CONTROL.HV_PROG_4").getData().data())
    HV_prog_old[4].append(myTree_with_light.getNode("gpi_tcv.APD_ARRAY.CONTROL.HV_PROG_5").getData().data())
    HV_prog_old[5].append(myTree_with_light.getNode("gpi_tcv.APD_ARRAY.CONTROL.HV_PROG_6").getData().data())
    HV_prog_old[6].append(myTree_with_light.getNode("gpi_tcv.APD_ARRAY.CONTROL.HV_PROG_7").getData().data())
    HV_prog_old[7].append(myTree_with_light.getNode("gpi_tcv.APD_ARRAY.CONTROL.HV_PROG_8").getData().data())
    myTree_with_light.close()

#s=1180626500 #old 'new fiber' shots
s=1180702500 #recent 'new fiber' shots
HV_meas_new=[[],[],[],[],[],[],[],[]]
HV_prog_new=[[],[],[],[],[],[],[],[]]
for i in range (1,num_shot+1):
    myTree_with_light=Tree("spectroscopy",s+i)
    HV_meas_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.HV_MEAS_ARR").getData().data()
    HV_meas_new[0].append(HV_meas_arr[0][0])
    HV_meas_new[1].append(HV_meas_arr[1][5])
    HV_meas_new[2].append(HV_meas_arr[3][0])
    HV_meas_new[3].append(HV_meas_arr[4][5])
    HV_meas_new[4].append(HV_meas_arr[6][0])
    HV_meas_new[5].append(HV_meas_arr[7][5])
    HV_meas_new[6].append(HV_meas_arr[9][0])
    HV_meas_new[7].append(HV_meas_arr[10][5])
    HV_prog_new[0].append(myTree_with_light.getNode("gpi_tcv.APD_ARRAY.CONTROL.HV_PROG_1").getData().data())
    HV_prog_new[1].append(myTree_with_light.getNode("gpi_tcv.APD_ARRAY.CONTROL.HV_PROG_2").getData().data())
    HV_prog_new[2].append(myTree_with_light.getNode("gpi_tcv.APD_ARRAY.CONTROL.HV_PROG_3").getData().data())
    HV_prog_new[3].append(myTree_with_light.getNode("gpi_tcv.APD_ARRAY.CONTROL.HV_PROG_4").getData().data())
    HV_prog_new[4].append(myTree_with_light.getNode("gpi_tcv.APD_ARRAY.CONTROL.HV_PROG_5").getData().data())
    HV_prog_new[5].append(myTree_with_light.getNode("gpi_tcv.APD_ARRAY.CONTROL.HV_PROG_6").getData().data())
    HV_prog_new[6].append(myTree_with_light.getNode("gpi_tcv.APD_ARRAY.CONTROL.HV_PROG_7").getData().data())
    HV_prog_new[7].append(myTree_with_light.getNode("gpi_tcv.APD_ARRAY.CONTROL.HV_PROG_8").getData().data())
    myTree_with_light.close()

sort_ind_1=np.argsort(HV_prog_old[0])
sort_ind_2=np.argsort(HV_prog_old[1])
sort_ind_3=np.argsort(HV_prog_old[2])
sort_ind_4=np.argsort(HV_prog_old[3])
sort_ind_5=np.argsort(HV_prog_old[4])
sort_ind_6=np.argsort(HV_prog_old[5])
sort_ind_7=np.argsort(HV_prog_old[6])
sort_ind_8=np.argsort(HV_prog_old[7])
HV_prog_old_1_sorted=np.sort(HV_prog_old[0])
HV_prog_old_2_sorted=np.sort(HV_prog_old[1])
HV_prog_old_3_sorted=np.sort(HV_prog_old[2])
HV_prog_old_4_sorted=np.sort(HV_prog_old[3])
HV_prog_old_5_sorted=np.sort(HV_prog_old[4])
HV_prog_old_6_sorted=np.sort(HV_prog_old[5])
HV_prog_old_7_sorted=np.sort(HV_prog_old[6])
HV_prog_old_8_sorted=np.sort(HV_prog_old[7])
HV_meas_old_1_sorted=np.array([])
HV_meas_old_2_sorted=np.array([])
HV_meas_old_3_sorted=np.array([])
HV_meas_old_4_sorted=np.array([])
HV_meas_old_5_sorted=np.array([])
HV_meas_old_6_sorted=np.array([])
HV_meas_old_7_sorted=np.array([])
HV_meas_old_8_sorted=np.array([])
for j in range (0,len(HV_prog_old_1_sorted)):
    HV_meas_old_1_sorted=np.append(HV_meas_old_1_sorted,HV_meas_old[0][sort_ind_1[j]])
    HV_meas_old_2_sorted=np.append(HV_meas_old_2_sorted,HV_meas_old[1][sort_ind_2[j]])
    HV_meas_old_3_sorted=np.append(HV_meas_old_3_sorted,HV_meas_old[2][sort_ind_3[j]])
    HV_meas_old_4_sorted=np.append(HV_meas_old_4_sorted,HV_meas_old[3][sort_ind_4[j]])
    HV_meas_old_5_sorted=np.append(HV_meas_old_5_sorted,HV_meas_old[4][sort_ind_5[j]])
    HV_meas_old_6_sorted=np.append(HV_meas_old_6_sorted,HV_meas_old[5][sort_ind_6[j]])
    HV_meas_old_7_sorted=np.append(HV_meas_old_7_sorted,HV_meas_old[6][sort_ind_7[j]])
    HV_meas_old_8_sorted=np.append(HV_meas_old_8_sorted,HV_meas_old[7][sort_ind_8[j]])

sort_ind_1=np.argsort(HV_prog_new[0])
sort_ind_2=np.argsort(HV_prog_new[1])
sort_ind_3=np.argsort(HV_prog_new[2])
sort_ind_4=np.argsort(HV_prog_new[3])
sort_ind_5=np.argsort(HV_prog_new[4])
sort_ind_6=np.argsort(HV_prog_new[5])
sort_ind_7=np.argsort(HV_prog_new[6])
sort_ind_8=np.argsort(HV_prog_new[7])
HV_prog_new_1_sorted=np.sort(HV_prog_new[0])
HV_prog_new_2_sorted=np.sort(HV_prog_new[1])
HV_prog_new_3_sorted=np.sort(HV_prog_new[2])
HV_prog_new_4_sorted=np.sort(HV_prog_new[3])
HV_prog_new_5_sorted=np.sort(HV_prog_new[4])
HV_prog_new_6_sorted=np.sort(HV_prog_new[5])
HV_prog_new_7_sorted=np.sort(HV_prog_new[6])
HV_prog_new_8_sorted=np.sort(HV_prog_new[7])
HV_meas_new_1_sorted=np.array([])
HV_meas_new_2_sorted=np.array([])
HV_meas_new_3_sorted=np.array([])
HV_meas_new_4_sorted=np.array([])
HV_meas_new_5_sorted=np.array([])
HV_meas_new_6_sorted=np.array([])
HV_meas_new_7_sorted=np.array([])
HV_meas_new_8_sorted=np.array([])
for j in range (0,len(HV_prog_new_1_sorted)):
    HV_meas_new_1_sorted=np.append(HV_meas_new_1_sorted,HV_meas_new[0][sort_ind_1[j]])
    HV_meas_new_2_sorted=np.append(HV_meas_new_2_sorted,HV_meas_new[1][sort_ind_2[j]])
    HV_meas_new_3_sorted=np.append(HV_meas_new_3_sorted,HV_meas_new[2][sort_ind_3[j]])
    HV_meas_new_4_sorted=np.append(HV_meas_new_4_sorted,HV_meas_new[3][sort_ind_4[j]])
    HV_meas_new_5_sorted=np.append(HV_meas_new_5_sorted,HV_meas_new[4][sort_ind_5[j]])
    HV_meas_new_6_sorted=np.append(HV_meas_new_6_sorted,HV_meas_new[5][sort_ind_6[j]])
    HV_meas_new_7_sorted=np.append(HV_meas_new_7_sorted,HV_meas_new[6][sort_ind_7[j]])
    HV_meas_new_8_sorted=np.append(HV_meas_new_8_sorted,HV_meas_new[7][sort_ind_8[j]])


a=8
b=5
"""
s=1180622500 #old 'old fiber' shots
gain_arr_old_when_hvmeas_380=np.array([])
mean_brt_arr_old_when_hvmeas_380=np.array([])
mean_sb_arr_old_when_hvmeas_380=np.array([])
for i in range (0,8):
    myTree_with_light=Tree("spectroscopy",s+np.abs(np.array(HV_meas_old[i])-380.).argmin())
    gain_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.GAIN_ARR").getData().data()
    brt_arr=1.41*4.35*myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.BRT_ARR").getData().data()/1000.
    sig_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.SIG_ARR").getData().data()
    back_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.CALIBRATION.BACK_ARR").getData().data()
    for j in range(i*15,(i+1)*15):
        gain_arr_old_when_hvmeas_380=np.append(gain_arr_old_when_hvmeas_380,gain_arr[j/10][j%10])
        mean_brt_arr_old_when_hvmeas_380=np.append(mean_brt_arr_old_when_hvmeas_380,np.mean(brt_arr[j/10][j%10]))
        mean_sb_arr_old_when_hvmeas_380=np.append(mean_sb_arr_old_when_hvmeas_380,back_arr[j/10][j%10]-np.mean(sig_arr[j/10][j%10]))
    myTree_with_light.close()
"""

#s=1180626500 #old 'new fiber' shots
s=1180702500 #recent 'new fiber' shots
gain_arr_new_when_hvmeas_380=np.array([])
mean_brt_arr_new_when_hvmeas_380=np.array([])
mean_sb_arr_new_when_hvmeas_380=np.array([])
for i in range (0,8):
    myTree_with_light=Tree("spectroscopy",s+np.abs(np.array(HV_meas_new[i])-380.).argmin())
    gain_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.GAIN_ARR").getData().data()
#    brt_arr=1.41*7.45*myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.BRT_ARR").getData().data() #old 'new fiber' shots
    brt_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.BRT_ARR").getData().data()
    sig_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.SIG_ARR").getData().data()
    back_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.CALIBRATION.BACK_ARR").getData().data()
    for j in range(i*15,(i+1)*15):
        gain_arr_new_when_hvmeas_380=np.append(gain_arr_new_when_hvmeas_380,gain_arr[j/10][j%10])
        mean_brt_arr_new_when_hvmeas_380=np.append(mean_brt_arr_new_when_hvmeas_380,np.mean(brt_arr[j/10][j%10]))
        mean_sb_arr_new_when_hvmeas_380=np.append(mean_sb_arr_new_when_hvmeas_380,back_arr[j/10][j%10]-np.mean(sig_arr[j/10][j%10]))
    myTree_with_light.close()
"""
s=1180622500 #old 'old fiber' shots
gain_00_old=np.array([])
gain_30_old=np.array([])
gain_60_old=np.array([])
brt_00_old=np.array([])
brt_30_old=np.array([])
brt_60_old=np.array([])
sb_00_old=np.array([])
sb_30_old=np.array([])
sb_60_old=np.array([])
gain_arr_old_when_hvprog_3_95=np.array([])
mean_brt_arr_old_when_hvprog_3_95=np.array([])
mean_sb_arr_old_when_hvprog_3_95=np.array([])
for i in range (1,num_shot+1):
    myTree_with_light=Tree("spectroscopy",s+i)
    gain_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.GAIN_ARR").getData().data()
    gain_00_old=np.append(gain_00_old,gain_arr[0][0])
    gain_30_old=np.append(gain_30_old,gain_arr[3][0])
    gain_60_old=np.append(gain_60_old,gain_arr[6][0])
    brt_arr=1.41*4.35*myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.BRT_ARR").getData().data()/1000.
    brt_00_old=np.append(brt_00_old,np.mean(brt_arr[0][0]))
    brt_30_old=np.append(brt_30_old,np.mean(brt_arr[3][0]))
    brt_60_old=np.append(brt_60_old,np.mean(brt_arr[6][0]))
    sig_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.SIG_ARR").getData().data()
    back_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.CALIBRATION.BACK_ARR").getData().data()
    sb_00_old=np.append(sb_00_old,back_arr[0][0]-np.mean(sig_arr[0][0]))
    sb_30_old=np.append(sb_30_old,back_arr[3][0]-np.mean(sig_arr[3][0]))
    sb_60_old=np.append(sb_60_old,back_arr[6][0]-np.mean(sig_arr[6][0]))
    if i==3:
        for j in range(0,12):
            for k in range(0,10):
                gain_arr_old_when_hvprog_3_95=np.append(gain_arr_old_when_hvprog_3_95,gain_arr[j][k])
                mean_brt_arr_old_when_hvprog_3_95=np.append(mean_brt_arr_old_when_hvprog_3_95,np.mean(brt_arr[j][k]))
                mean_sb_arr_old_when_hvprog_3_95=np.append(mean_sb_arr_old_when_hvprog_3_95,back_arr[j][k]-np.mean(sig_arr[j][k]))
    myTree_with_light.close()

#HV_meas_sorted_old=HV_meas_old[(a*10+b)/15]
HV_meas_sorted_old_00=HV_meas_old[(0*10+0)/15]
HV_meas_sorted_old_30=HV_meas_old[(3*10+0)/15]
HV_meas_sorted_old_60=HV_meas_old[(6*10+0)/15]
sort_ind_00=np.argsort(HV_meas_sorted_old_00)
sort_ind_30=np.argsort(HV_meas_sorted_old_30)
sort_ind_60=np.argsort(HV_meas_sorted_old_60)
HV_meas_sorted_old_00=np.sort(HV_meas_sorted_old_00)
HV_meas_sorted_old_30=np.sort(HV_meas_sorted_old_30)
HV_meas_sorted_old_60=np.sort(HV_meas_sorted_old_60)
temp_gain_00=np.array([])
temp_gain_30=np.array([])
temp_gain_60=np.array([])
temp_brt_00=np.array([])
temp_brt_30=np.array([])
temp_brt_60=np.array([])
temp_sb_00=np.array([])
temp_sb_30=np.array([])
temp_sb_60=np.array([])
for j in range (0,len(gain_00_old)):
    temp_gain_00=np.append(temp_gain_00,gain_00_old[sort_ind_00[j]])
    temp_gain_30=np.append(temp_gain_30,gain_30_old[sort_ind_30[j]])
    temp_gain_60=np.append(temp_gain_60,gain_60_old[sort_ind_60[j]])
    temp_brt_00=np.append(temp_brt_00,brt_00_old[sort_ind_00[j]])
    temp_brt_30=np.append(temp_brt_30,brt_30_old[sort_ind_30[j]])
    temp_brt_60=np.append(temp_brt_60,brt_60_old[sort_ind_60[j]])
    temp_sb_00=np.append(temp_sb_00,sb_00_old[sort_ind_00[j]])
    temp_sb_30=np.append(temp_sb_30,sb_30_old[sort_ind_30[j]])
    temp_sb_60=np.append(temp_sb_60,sb_60_old[sort_ind_60[j]])

gain_00_old=temp_gain_00
gain_30_old=temp_gain_30
gain_60_old=temp_gain_60
brt_00_old=temp_brt_00
brt_30_old=temp_brt_30
brt_60_old=temp_brt_60
sb_00_old=temp_sb_00
sb_30_old=temp_sb_30
sb_60_old=temp_sb_60
"""


#s=1180626500 #old 'new fiber' shots
s=1180702500 #recent 'new fiber' shots
gain_00_new=np.array([])
gain_30_new=np.array([])
gain_60_new=np.array([])
gain_90_new=np.array([])
brt_00_new=np.array([])
brt_30_new=np.array([])
brt_60_new=np.array([])
brt_90_new=np.array([])
sb_00_new=np.array([])
sb_30_new=np.array([])
sb_60_new=np.array([])
sb_90_new=np.array([])
gain_arr_new_when_hvprog_3_95=np.array([])
mean_brt_arr_new_when_hvprog_3_95=np.array([])
mean_sb_arr_new_when_hvprog_3_95=np.array([])
for i in range (1,num_shot+1):
    myTree_with_light=Tree("spectroscopy",s+i)
    gain_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.GAIN_ARR").getData().data()
    gain_00_new=np.append(gain_00_new,gain_arr[0][0])
    gain_30_new=np.append(gain_30_new,gain_arr[3][0])
    gain_60_new=np.append(gain_60_new,gain_arr[6][0])
    gain_90_new=np.append(gain_90_new,gain_arr[9][0])
#    brt_arr=1.41*7.45*myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.BRT_ARR").getData().data() #old 'new fiber' shots
    brt_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.BRT_ARR").getData().data()
    brt_00_new=np.append(brt_00_new,np.mean(brt_arr[0][0]))
    brt_30_new=np.append(brt_30_new,np.mean(brt_arr[3][0]))
    brt_60_new=np.append(brt_60_new,np.mean(brt_arr[6][0]))
    brt_90_new=np.append(brt_90_new,np.mean(brt_arr[9][0]))
    sig_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.SIG_ARR").getData().data()
    back_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.CALIBRATION.BACK_ARR").getData().data()
    sb_00_new=np.append(sb_00_new,back_arr[0][0]-np.mean(sig_arr[0][0]))
    sb_30_new=np.append(sb_30_new,back_arr[3][0]-np.mean(sig_arr[3][0]))
    sb_60_new=np.append(sb_60_new,back_arr[6][0]-np.mean(sig_arr[6][0]))
    sb_90_new=np.append(sb_90_new,back_arr[9][0]-np.mean(sig_arr[9][0]))
    if i==5:
        for j in range(0,12):
            for k in range(0,10):
                gain_arr_new_when_hvprog_3_95=np.append(gain_arr_new_when_hvprog_3_95,gain_arr[j][k])
                mean_brt_arr_new_when_hvprog_3_95=np.append(mean_brt_arr_new_when_hvprog_3_95,np.mean(brt_arr[j][k]))
                mean_sb_arr_new_when_hvprog_3_95=np.append(mean_sb_arr_new_when_hvprog_3_95,back_arr[j][k]-np.mean(sig_arr[j][k]))
    myTree_with_light.close()

#HV_meas_sorted_new=HV_meas_new[(a*10+b)/15]
HV_meas_sorted_new_00=HV_meas_new[(0*10+0)/15]
HV_meas_sorted_new_30=HV_meas_new[(3*10+0)/15]
HV_meas_sorted_new_60=HV_meas_new[(6*10+0)/15]
HV_meas_sorted_new_90=HV_meas_new[(9*10+0)/15]
sort_ind_00=np.argsort(HV_meas_sorted_new_00)
sort_ind_30=np.argsort(HV_meas_sorted_new_30)
sort_ind_60=np.argsort(HV_meas_sorted_new_60)
sort_ind_90=np.argsort(HV_meas_sorted_new_90)
HV_meas_sorted_new_00=np.sort(HV_meas_sorted_new_00)
HV_meas_sorted_new_30=np.sort(HV_meas_sorted_new_30)
HV_meas_sorted_new_60=np.sort(HV_meas_sorted_new_60)
HV_meas_sorted_new_90=np.sort(HV_meas_sorted_new_90)
temp_gain_00=np.array([])
temp_gain_30=np.array([])
temp_gain_60=np.array([])
temp_gain_90=np.array([])
temp_brt_00=np.array([])
temp_brt_30=np.array([])
temp_brt_60=np.array([])
temp_brt_90=np.array([])
temp_sb_00=np.array([])
temp_sb_30=np.array([])
temp_sb_60=np.array([])
temp_sb_90=np.array([])
for j in range (0,len(gain_00_new)):
    temp_gain_00=np.append(temp_gain_00,gain_00_new[sort_ind_00[j]])
    temp_gain_30=np.append(temp_gain_30,gain_30_new[sort_ind_30[j]])
    temp_gain_60=np.append(temp_gain_60,gain_60_new[sort_ind_60[j]])
    temp_gain_90=np.append(temp_gain_90,gain_90_new[sort_ind_90[j]])
    temp_brt_00=np.append(temp_brt_00,brt_00_new[sort_ind_00[j]])
    temp_brt_30=np.append(temp_brt_30,brt_30_new[sort_ind_30[j]])
    temp_brt_60=np.append(temp_brt_60,brt_60_new[sort_ind_60[j]])
    temp_brt_90=np.append(temp_brt_90,brt_90_new[sort_ind_90[j]])
    temp_sb_00=np.append(temp_sb_00,sb_00_new[sort_ind_00[j]])
    temp_sb_30=np.append(temp_sb_30,sb_30_new[sort_ind_30[j]])
    temp_sb_60=np.append(temp_sb_60,sb_60_new[sort_ind_60[j]])
    temp_sb_90=np.append(temp_sb_90,sb_90_new[sort_ind_90[j]])

gain_00_new=temp_gain_00
gain_30_new=temp_gain_30
gain_60_new=temp_gain_60
gain_90_new=temp_gain_90
brt_00_new=temp_brt_00
brt_30_new=temp_brt_30
brt_60_new=temp_brt_60
brt_90_new=temp_brt_90
sb_00_new=temp_sb_00
sb_30_new=temp_sb_30
sb_60_new=temp_sb_60
sb_90_new=temp_sb_90


plt.figure(1)
line_1_new,=plt.plot(HV_meas_sorted_new_00,gain_00_new,".-")
#line_1_old,=plt.plot(HV_meas_sorted_old_00,gain_00_old,".-")
plt.xlabel('HV_meas (V)')
plt.ylabel('gain_arr[0][0] (from Board 24)')
#plt.legend([line_1_new,line_1_old],['New_fiber','Old_fiber'])

plt.figure(2)
line_2_new,=plt.plot(HV_meas_sorted_new_30,gain_30_new,".-")
#line_2_old,=plt.plot(HV_meas_sorted_old_30,gain_30_old,".-")
plt.xlabel('HV_meas (V)')
plt.ylabel('gain_arr[3][0] (from Board 25)')
#plt.legend([line_2_new,line_2_old],['New_fiber','Old_fiber'])

plt.figure(3)
line_3_new,=plt.plot(HV_meas_sorted_new_60,gain_60_new,".-")
#line_3_old,=plt.plot(HV_meas_sorted_old_60,gain_60_old,".-")
plt.xlabel('HV_meas (V)')
plt.ylabel('gain_arr[6][0] (from Board 26)')
#plt.legend([line_3_new,line_3_old],['New_fiber','Old_fiber'])

plt.figure(4)
line_4_new,=plt.plot(HV_meas_sorted_new_90,gain_90_new,".-")
plt.xlabel('HV_meas (V)')
plt.ylabel('gain_arr[9][0] (from Board 27)')
#plt.legend([line_4_new],['New_fiber'])

plt.figure(5)
line_5_new,=plt.plot(HV_meas_sorted_new_00,brt_00_new,".-")
#line_5_old,=plt.plot(HV_meas_sorted_old_00,brt_00_old,".-")
plt.xlabel('HV_meas (V)')
plt.ylabel('mean brt_arr[0][0] (mW/cm2/ster) (from Board 24)')
#plt.legend([line_5_new,line_5_old],['New_fiber','Old_fiber'])

plt.figure(6)
line_6_new,=plt.plot(HV_meas_sorted_new_30,brt_30_new,".-")
#line_6_old,=plt.plot(HV_meas_sorted_old_30,brt_30_old,".-")
plt.xlabel('HV_meas (V)')
plt.ylabel('mean brt_arr[3][0] (mW/cm2/ster) (from Board 25)')
#plt.legend([line_6_new,line_6_old],['New_fiber','Old_fiber'])

plt.figure(7)
line_7_new,=plt.plot(HV_meas_sorted_new_60,brt_60_new,".-")
#line_7_old,=plt.plot(HV_meas_sorted_old_60,brt_60_old,".-")
plt.xlabel('HV_meas (V)')
plt.ylabel('mean brt_arr[6][0] (mW/cm2/ster) (from Board 26)')
#plt.legend([line_7_new,line_7_old],['New_fiber','Old_fiber'])

plt.figure(8)
line_8_new,=plt.plot(HV_meas_sorted_new_90,brt_90_new,".-")
plt.xlabel('HV_meas (V)')
plt.ylabel('mean brt_arr[9][0] (mW/cm2/ster) (from Board 27)')
#plt.legend([line_8_new],['New_fiber'])


plt.figure(9)
line_9_new,=plt.plot(HV_meas_sorted_new_00,sb_00_new,".-")
#line_9_old,=plt.plot(HV_meas_sorted_old_00,sb_00_old,".-")
plt.xlabel('HV_meas (V)')
plt.ylabel('mean sig_minus_back [0][0] (V) (from Board 24)')
#plt.legend([line_9_new,line_9_old],['New_fiber','Old_fiber'])

plt.figure(10)
line_10_new,=plt.plot(HV_meas_sorted_new_30,sb_30_new,".-")
#line_10_old,=plt.plot(HV_meas_sorted_old_30,sb_30_old,".-")
plt.xlabel('HV_meas (V)')
plt.ylabel('mean sig_minus_back [3][0] (V) (from Board 25)')
#plt.legend([line_10_new,line_10_old],['New_fiber','Old_fiber'])

plt.figure(11)
line_11_new,=plt.plot(HV_meas_sorted_new_60,sb_60_new,".-")
#line_11_old,=plt.plot(HV_meas_sorted_old_60,sb_60_old,".-")
plt.xlabel('HV_meas (V)')
plt.ylabel('mean sig_minus_back [6][0] (V) (from Board 26)')
#plt.legend([line_11_new,line_11_old],['New_fiber','Old_fiber'])

plt.figure(12)
line_12_new,=plt.plot(HV_meas_sorted_new_90,sb_90_new,".-")
plt.xlabel('HV_meas (V)')
plt.ylabel('mean sig_minus_back [9][0] (V) (from Board 27)')
#plt.legend([line_12_new],['New_fiber'])

chan_new=np.arange(120)
chan_old=np.arange(90)

plt.figure(13)
line_13_new,=plt.plot(chan_new,gain_arr_new_when_hvprog_3_95,".-")
#line_13_old,=plt.plot(chan_old,gain_arr_old_when_hvprog_3_95[0:90],".-")
plt.xlabel('Channel number (arbitrary)')
plt.ylabel('Gain when HV_prog=3.95V')
#plt.legend([line_13_new,line_13_old],['New_fiber','Old_fiber'])

#for i in range(0,120):
#    if mean_brt_arr_old_when_hvprog_3_95[i]<-1.:
#        mean_brt_arr_old_when_hvprog_3_95[i]=mean_brt_arr_old_when_hvprog_3_95[0]

plt.figure(14)
line_14_new,=plt.plot(chan_new,mean_brt_arr_new_when_hvprog_3_95,".-")
#line_14_old,=plt.plot(chan_old,mean_brt_arr_old_when_hvprog_3_95[0:90],".-")
plt.xlabel('Channel number (arbitrary)')
plt.ylabel('Mean Brt (mW/cm2/ster) when HV_prog=3.95V')
#plt.legend([line_14_new,line_14_old],['New_fiber','Old_fiber'])

plt.figure(15)
line_15_new,=plt.plot(chan_new,mean_sb_arr_new_when_hvprog_3_95,".-")
#line_15_old,=plt.plot(chan_old,mean_sb_arr_old_when_hvprog_3_95[0:90],".-")
plt.xlabel('Channel number (arbitrary)')
plt.ylabel('Mean sig_minus_back (V) when HV_prog=3.95V')
#plt.legend([line_15_new,line_15_old],['New_fiber','Old_fiber'])

plt.figure(16)
line_16_new_1,=plt.plot(HV_prog_new_1_sorted,HV_meas_new_1_sorted,".-")
line_16_new_2,=plt.plot(HV_prog_new_2_sorted,HV_meas_new_2_sorted,".-")
line_16_new_3,=plt.plot(HV_prog_new_3_sorted,HV_meas_new_3_sorted,".-")
line_16_new_4,=plt.plot(HV_prog_new_4_sorted,HV_meas_new_4_sorted,".-")
line_16_new_5,=plt.plot(HV_prog_new_5_sorted,HV_meas_new_5_sorted,".-")
line_16_new_6,=plt.plot(HV_prog_new_6_sorted,HV_meas_new_6_sorted,".-")
line_16_new_7,=plt.plot(HV_prog_new_7_sorted,HV_meas_new_7_sorted,".-")
line_16_new_8,=plt.plot(HV_prog_new_8_sorted,HV_meas_new_8_sorted,".-")
plt.xlabel('HV_prog_NEW (V)')
plt.ylabel('HV_meas_NEW (V)')
plt.xlim(2.8,5.)
plt.legend([line_16_new_1,line_16_new_2,line_16_new_3,line_16_new_4,line_16_new_5,line_16_new_6,line_16_new_7,line_16_new_8],['Side 1 of Board 24','Side 2 of Board 24','Side 1 of Board 25','Side 2 of Board 25','Side 1 of Board 26','Side 2 of Board 26','Side 1 of Board 27','Side 2 of Board 27'])
"""
plt.figure(17)
line_17_old_1,=plt.plot(HV_prog_old_1_sorted,HV_meas_old_1_sorted,".-")
line_17_old_2,=plt.plot(HV_prog_old_2_sorted,HV_meas_old_2_sorted,".-")
line_17_old_3,=plt.plot(HV_prog_old_3_sorted,HV_meas_old_3_sorted,".-")
line_17_old_4,=plt.plot(HV_prog_old_4_sorted,HV_meas_old_4_sorted,".-")
line_17_old_5,=plt.plot(HV_prog_old_5_sorted,HV_meas_old_5_sorted,".-")
line_17_old_6,=plt.plot(HV_prog_old_6_sorted,HV_meas_old_6_sorted,".-")
line_17_old_7,=plt.plot(HV_prog_old_7_sorted,HV_meas_old_7_sorted,".-")
line_17_old_8,=plt.plot(HV_prog_old_8_sorted,HV_meas_old_8_sorted,".-")
plt.xlabel('HV_prog_OLD (V)')
plt.ylabel('HV_meas_OLD (V)')
plt.xlim(2.8,6.)
plt.legend([line_17_old_1,line_17_old_2,line_17_old_3,line_17_old_4,line_17_old_5,line_17_old_6,line_17_old_7,line_17_old_8],['Side 1 of Board 24','Side 2 of Board 24','Side 1 of Board 25','Side 2 of Board 25','Side 1 of Board 26','Side 2 of Board 26','Side 1 of Board 27','Side 2 of Board 27'])
"""
plt.figure(18)
line_18_new,=plt.plot(chan_new,gain_arr_new_when_hvmeas_380,".-")
#line_18_old,=plt.plot(chan_old,gain_arr_old_when_hvmeas_380[0:90],".-")
plt.xlabel('Channel number (arbitrary)')
plt.ylabel('Gain when HV_meas~380V')
#plt.legend([line_18_new,line_18_old],['New_fiber','Old_fiber'])

plt.figure(19)
line_19_new,=plt.plot(chan_new,mean_brt_arr_new_when_hvmeas_380,".-")
#line_19_old,=plt.plot(chan_old,mean_brt_arr_old_when_hvmeas_380[0:90],".-")
plt.xlabel('Channel number (arbitrary)')
plt.ylabel('Mean Brt (mW/cm2/ster) when HV_meas~380V')
#plt.legend([line_19_new,line_19_old],['New_fiber','Old_fiber'])

plt.figure(20)
line_20_new,=plt.plot(chan_new,mean_sb_arr_new_when_hvmeas_380,".-")
#line_20_old,=plt.plot(chan_old,mean_sb_arr_old_when_hvmeas_380[0:90],".-")
plt.xlabel('Channel number (arbitrary)')
plt.ylabel('Mean sig_minus_back (V) when HV_meas~380V')
p#lt.legend([line_20_new,line_20_old],['New_fiber','Old_fiber'])

plt.figure(21)
line_21_new,=plt.plot(HV_prog_new_1_sorted,HV_meas_new_1_sorted,".-")
#line_21_old,=plt.plot(HV_prog_old_1_sorted,HV_meas_old_1_sorted,".-")
plt.xlabel('HV_prog (V), Side 1 of Board 24')
plt.ylabel('HV_meas (V), Side 1 of Board 24')
#plt.legend([line_21_new,line_21_old],['New_fiber','Old_fiber'])

plt.figure(22)
line_22_new,=plt.plot(HV_prog_new_2_sorted,HV_meas_new_2_sorted,".-")
#line_22_old,=plt.plot(HV_prog_old_2_sorted,HV_meas_old_2_sorted,".-")
plt.xlabel('HV_prog (V), Side 2 of Board 24')
plt.ylabel('HV_meas (V), Side 2 of Board 24')
#plt.legend([line_22_new,line_22_old],['New_fiber','Old_fiber'])

plt.figure(23)
line_23_new,=plt.plot(HV_prog_new_3_sorted,HV_meas_new_3_sorted,".-")
#line_23_old,=plt.plot(HV_prog_old_3_sorted,HV_meas_old_3_sorted,".-")
plt.xlabel('HV_prog (V), Side 1 of Board 25')
plt.ylabel('HV_meas (V), Side 1 of Board 25')
#plt.legend([line_23_new,line_23_old],['New_fiber','Old_fiber'])

plt.figure(24)
line_24_new,=plt.plot(HV_prog_new_4_sorted,HV_meas_new_4_sorted,".-")
#line_24_old,=plt.plot(HV_prog_old_4_sorted,HV_meas_old_4_sorted,".-")
plt.xlabel('HV_prog (V), Side 2 of Board 25')
plt.ylabel('HV_meas (V), Side 2 of Board 25')
#plt.legend([line_24_new,line_24_old],['New_fiber','Old_fiber'])

plt.figure(25)
line_25_new,=plt.plot(HV_prog_new_5_sorted,HV_meas_new_5_sorted,".-")
#line_25_old,=plt.plot(HV_prog_old_5_sorted,HV_meas_old_5_sorted,".-")
plt.xlabel('HV_prog (V), Side 1 of Board 26')
plt.ylabel('HV_meas (V), Side 1 of Board 26')
#plt.legend([line_25_new,line_25_old],['New_fiber','Old_fiber'])

plt.figure(26)
line_26_new,=plt.plot(HV_prog_new_6_sorted,HV_meas_new_6_sorted,".-")
#line_26_old,=plt.plot(HV_prog_old_6_sorted,HV_meas_old_6_sorted,".-")
plt.xlabel('HV_prog (V), Side 2 of Board 26')
plt.ylabel('HV_meas (V), Side 2 of Board 26')
#plt.legend([line_26_new,line_26_old],['New_fiber','Old_fiber'])

plt.figure(27)
line_27_new,=plt.plot(HV_prog_new_7_sorted,HV_meas_new_7_sorted,".-")
#line_27_old,=plt.plot(HV_prog_old_7_sorted,HV_meas_old_7_sorted,".-")
plt.xlabel('HV_prog (V), Side 1 of Board 27')
plt.ylabel('HV_meas (V), Side 1 of Board 27')
#plt.legend([line_27_new,line_27_old],['New_fiber','Old_fiber'])

plt.figure(28)
line_28_new,=plt.plot(HV_prog_new_8_sorted,HV_meas_new_8_sorted,".-")
#line_28_old,=plt.plot(HV_prog_old_8_sorted,HV_meas_old_8_sorted,".-")
plt.xlabel('HV_prog (V), Side 2 of Board 27')
plt.ylabel('HV_meas (V), Side 2 of Board 27')
#plt.legend([line_28_new,line_28_old],['New_fiber','Old_fiber'])

plt.show()


