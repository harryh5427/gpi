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
"""
#s=1180626500 #old 'new fiber' shots
#s=1180702500 #recent 'new fiber' shots
s=1180705500 #copied old 'new fiber' shots
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


"""
s=1180622500 #old 'old fiber' shots
HV_meas_old=[[],[],[],[],[],[],[],[]]
HV_prog_old=[[],[],[],[],[],[],[],[]]
for i in range (1,num_shot+1):
    myTree_with_light=Tree("spectroscopy",s+i)
#    HV_meas_arr=200.*myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.HV_MEAS_ARR").getData().data() #s=1180622500 #old 'old fiber' shots
    HV_meas_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.HV_MEAS_ARR").getData().data()
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
"""
#s=1180626500 #old 'new fiber' shots
#s=1180702500 #recent 'new fiber' shots
s=1180705500 #copied old 'new fiber' shots
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
"""
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
"""
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
#s=1180702500 #recent 'new fiber' shots
s=1180705500 #copied old 'new fiber' shots
gain_arr_old_when_hvmeas_380=np.array([])
mean_brt_arr_old_when_hvmeas_380=np.array([])
mean_sb_arr_old_when_hvmeas_380=np.array([])
apprx_hvmeas_old_when_hvmeas_380=np.array([])
gain_arr_old_when_hvmeas_400=np.array([])
mean_brt_arr_old_when_hvmeas_400=np.array([])
mean_sb_arr_old_when_hvmeas_400=np.array([])
apprx_hvmeas_old_when_hvmeas_400=np.array([])
for i in range (0,8):
    ind_hvmeas_380=np.abs(np.array(HV_meas_old[i])-380.).argmin()
    myTree_with_light=Tree("spectroscopy",s+ind_hvmeas_380+1)
    gain_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.GAIN_ARR").getData().data()
#    brt_arr=1.41*7.45*myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.BRT_ARR").getData().data() #old 'new fiber' shots
#    brt_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.BRT_ARR").getData().data()
    sig_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.SIG_ARR").getData().data()
    back_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.CALIBRATION.BACK_ARR").getData().data()
    for j in range(i*15,(i+1)*15):
        gain_arr_old_when_hvmeas_380=np.append(gain_arr_old_when_hvmeas_380,gain_arr[j/10][j%10])
#        mean_brt_arr_old_when_hvmeas_380=np.append(mean_brt_arr_old_when_hvmeas_380,np.mean(brt_arr[j/10][j%10]))
        mean_sb_arr_old_when_hvmeas_380=np.append(mean_sb_arr_old_when_hvmeas_380,back_arr[j/10][j%10]-np.mean(sig_arr[j/10][j%10]))
        apprx_hvmeas_old_when_hvmeas_380=np.append(apprx_hvmeas_old_when_hvmeas_380,np.array(HV_meas_old[i])[ind_hvmeas_380])
    myTree_with_light.close()
    ind_hvmeas_400=np.abs(np.array(HV_meas_old[i])-400.).argmin()
    myTree_with_light=Tree("spectroscopy",s+ind_hvmeas_400+1)
    gain_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.GAIN_ARR").getData().data()
#    brt_arr=1.41*7.45*myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.BRT_ARR").getData().data() #old 'new fiber' shots
#    brt_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.BRT_ARR").getData().data()
    sig_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.SIG_ARR").getData().data()
    back_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.CALIBRATION.BACK_ARR").getData().data()
    for j in range(i*15,(i+1)*15):
        gain_arr_old_when_hvmeas_400=np.append(gain_arr_old_when_hvmeas_400,gain_arr[j/10][j%10])
#        mean_brt_arr_old_when_hvmeas_400=np.append(mean_brt_arr_old_when_hvmeas_400,np.mean(brt_arr[j/10][j%10]))
        mean_sb_arr_old_when_hvmeas_400=np.append(mean_sb_arr_old_when_hvmeas_400,back_arr[j/10][j%10]-np.mean(sig_arr[j/10][j%10]))
        apprx_hvmeas_old_when_hvmeas_400=np.append(apprx_hvmeas_old_when_hvmeas_400,np.array(HV_meas_old[i])[ind_hvmeas_400])
    myTree_with_light.close()

#s=1180626500 #old 'new fiber' shots
#s=1180702500 #recent 'new fiber' shots
s=1180705500 #copied old 'new fiber' shots
gain_arr_new_when_hvmeas_380=np.array([])
mean_brt_arr_new_when_hvmeas_380=np.array([])
mean_sb_arr_new_when_hvmeas_380=np.array([])
apprx_hvmeas_new_when_hvmeas_380=np.array([])
gain_arr_new_when_hvmeas_400=np.array([])
mean_brt_arr_new_when_hvmeas_400=np.array([])
mean_sb_arr_new_when_hvmeas_400=np.array([])
apprx_hvmeas_new_when_hvmeas_400=np.array([])
for i in range (0,8):
    ind_hvmeas_380=np.abs(np.array(HV_meas_new[i])-380.).argmin()
    myTree_with_light=Tree("spectroscopy",s+ind_hvmeas_380+1)
    gain_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.GAIN_ARR").getData().data()
#    brt_arr=1.41*7.45*myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.BRT_ARR").getData().data() #old 'new fiber' shots
#    brt_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.BRT_ARR").getData().data()
    sig_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.SIG_ARR").getData().data()
    back_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.CALIBRATION.BACK_ARR").getData().data()
    for j in range(i*15,(i+1)*15):
        gain_arr_new_when_hvmeas_380=np.append(gain_arr_new_when_hvmeas_380,gain_arr[j/10][j%10])
#        mean_brt_arr_new_when_hvmeas_380=np.append(mean_brt_arr_new_when_hvmeas_380,np.mean(brt_arr[j/10][j%10]))
        mean_sb_arr_new_when_hvmeas_380=np.append(mean_sb_arr_new_when_hvmeas_380,back_arr[j/10][j%10]-np.mean(sig_arr[j/10][j%10]))
        apprx_hvmeas_new_when_hvmeas_380=np.append(apprx_hvmeas_new_when_hvmeas_380,np.array(HV_meas_new[i])[ind_hvmeas_380])
    myTree_with_light.close()
    ind_hvmeas_400=np.abs(np.array(HV_meas_new[i])-400.).argmin()
    myTree_with_light=Tree("spectroscopy",s+ind_hvmeas_400+1)
    gain_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.GAIN_ARR").getData().data()
#    brt_arr=1.41*7.45*myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.BRT_ARR").getData().data() #old 'new fiber' shots
#    brt_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.BRT_ARR").getData().data()
    sig_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.SIG_ARR").getData().data()
    back_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.CALIBRATION.BACK_ARR").getData().data()
    for j in range(i*15,(i+1)*15):
        gain_arr_new_when_hvmeas_400=np.append(gain_arr_new_when_hvmeas_400,gain_arr[j/10][j%10])
#        mean_brt_arr_new_when_hvmeas_400=np.append(mean_brt_arr_new_when_hvmeas_400,np.mean(brt_arr[j/10][j%10]))
        mean_sb_arr_new_when_hvmeas_400=np.append(mean_sb_arr_new_when_hvmeas_400,back_arr[j/10][j%10]-np.mean(sig_arr[j/10][j%10]))
        apprx_hvmeas_new_when_hvmeas_400=np.append(apprx_hvmeas_new_when_hvmeas_400,np.array(HV_meas_new[i])[ind_hvmeas_400])
    myTree_with_light.close()
"""
#s=1180702500 #recent 'new fiber' shots
s=1180705500 #copied old 'new fiber' shots
gain_arr_new_when_hvmeas_400=np.array([])
mean_brt_arr_new_when_hvmeas_400=np.array([])
mean_sb_arr_new_when_hvmeas_400=np.array([])
hvmeas_arr_new_when_hvmeas_400=np.array([])
coef_0th=np.array([])
coef_1st=np.array([])
coef_2nd=np.array([])
coef_3rd=np.array([])
coef_4th=np.array([])
for i in range (0,8):
    myTree_with_light=Tree("spectroscopy",s+np.abs(np.array(HV_meas_new[i])-400.).argmin()+1)
    gain_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.GAIN_ARR").getData().data()
#    brt_arr=1.41*7.45*myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.BRT_ARR").getData().data() #old 'new fiber' shots
    brt_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.BRT_ARR").getData().data()
    sig_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.SIG_ARR").getData().data()
    back_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.CALIBRATION.BACK_ARR").getData().data()
    hvmeas_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.HV_MEAS_ARR").getData().data()
    coef_0th_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.CALIBRATION.COEF_0TH_ARR").getData().data()
    coef_1st_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.CALIBRATION.COEF_1ST_ARR").getData().data()
    coef_2nd_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.CALIBRATION.COEF_2ND_ARR").getData().data()
    coef_3rd_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.CALIBRATION.COEF_3RD_ARR").getData().data()
    coef_4th_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.CALIBRATION.COEF_4TH_ARR").getData().data()
    for j in range(i*15,(i+1)*15):
        gain_arr_new_when_hvmeas_400=np.append(gain_arr_new_when_hvmeas_400,gain_arr[j/10][j%10])
        mean_brt_arr_new_when_hvmeas_400=np.append(mean_brt_arr_new_when_hvmeas_400,np.mean(brt_arr[j/10][j%10]))
        mean_sb_arr_new_when_hvmeas_400=np.append(mean_sb_arr_new_when_hvmeas_400,back_arr[j/10][j%10]-np.mean(sig_arr[j/10][j%10]))
        hvmeas_arr_new_when_hvmeas_400=np.append(hvmeas_arr_new_when_hvmeas_400,hvmeas_arr[j/10][j%10])
        coef_0th=np.append(coef_0th,coef_0th_arr[j/10][j%10])
        coef_1st=np.append(coef_1st,coef_1st_arr[j/10][j%10])
        coef_2nd=np.append(coef_2nd,coef_2nd_arr[j/10][j%10])
        coef_3rd=np.append(coef_3rd,coef_3rd_arr[j/10][j%10])
        coef_4th=np.append(coef_4th,coef_4th_arr[j/10][j%10])
    myTree_with_light.close()

_vr=[409.5,412.8,403.5,392.5,391.1,390.3,421.8,426.2]
gain_arr_new_when_hvmeas_400_calculated=gain_arr_new_when_hvmeas_400
gain_arr_new_when_hvmeas_400_calculated[0:15]=67.49*np.exp(coef_0th[0:15]+coef_1st[0:15]*hvmeas_arr_new_when_hvmeas_400[0:15]+coef_2nd[0:15]*np.power(hvmeas_arr_new_when_hvmeas_400[0:15],2)+coef_3rd[0:15]*np.power(hvmeas_arr_new_when_hvmeas_400[0:15],3)+coef_4th[0:15]*np.power(hvmeas_arr_new_when_hvmeas_400[0:15],4))/np.exp(coef_0th[0:15]+coef_1st[0:15]*_vr[0]+coef_2nd[0:15]*np.power(_vr[0],2)+coef_3rd[0:15]*np.power(_vr[0],3)+coef_4th[0:15]*np.power(_vr[0],4))

gain_arr_new_when_hvmeas_400_calculated[15:30]=67.49*np.exp(coef_0th[15:30]+coef_1st[15:30]*hvmeas_arr_new_when_hvmeas_400[15:30]+coef_2nd[15:30]*np.power(hvmeas_arr_new_when_hvmeas_400[15:30],2)+coef_3rd[15:30]*np.power(hvmeas_arr_new_when_hvmeas_400[15:30],3)+coef_4th[15:30]*np.power(hvmeas_arr_new_when_hvmeas_400[15:30],4))/np.exp(coef_0th[15:30]+coef_1st[15:30]*_vr[1]+coef_2nd[15:30]*np.power(_vr[1],2)+coef_3rd[15:30]*np.power(_vr[1],3)+coef_4th[15:30]*np.power(_vr[1],4))

gain_arr_new_when_hvmeas_400_calculated[30:45]=67.49*np.exp(coef_0th[30:45]+coef_1st[30:45]*hvmeas_arr_new_when_hvmeas_400[30:45]+coef_2nd[30:45]*np.power(hvmeas_arr_new_when_hvmeas_400[30:45],2)+coef_3rd[30:45]*np.power(hvmeas_arr_new_when_hvmeas_400[30:45],3)+coef_4th[30:45]*np.power(hvmeas_arr_new_when_hvmeas_400[30:45],4))/np.exp(coef_0th[30:45]+coef_1st[30:45]*_vr[2]+coef_2nd[30:45]*np.power(_vr[2],2)+coef_3rd[30:45]*np.power(_vr[2],3)+coef_4th[30:45]*np.power(_vr[2],4))

gain_arr_new_when_hvmeas_400_calculated[45:60]=67.49*np.exp(coef_0th[45:60]+coef_1st[45:60]*hvmeas_arr_new_when_hvmeas_400[45:60]+coef_2nd[45:60]*np.power(hvmeas_arr_new_when_hvmeas_400[45:60],2)+coef_3rd[45:60]*np.power(hvmeas_arr_new_when_hvmeas_400[45:60],3)+coef_4th[45:60]*np.power(hvmeas_arr_new_when_hvmeas_400[45:60],4))/np.exp(coef_0th[45:60]+coef_1st[45:60]*_vr[3]+coef_2nd[45:60]*np.power(_vr[3],2)+coef_3rd[45:60]*np.power(_vr[3],3)+coef_4th[45:60]*np.power(_vr[3],4))

gain_arr_new_when_hvmeas_400_calculated[60:75]=67.49*np.exp(coef_0th[60:75]+coef_1st[60:75]*hvmeas_arr_new_when_hvmeas_400[60:75]+coef_2nd[60:75]*np.power(hvmeas_arr_new_when_hvmeas_400[60:75],2)+coef_3rd[60:75]*np.power(hvmeas_arr_new_when_hvmeas_400[60:75],3)+coef_4th[60:75]*np.power(hvmeas_arr_new_when_hvmeas_400[60:75],4))/np.exp(coef_0th[60:75]+coef_1st[60:75]*_vr[4]+coef_2nd[60:75]*np.power(_vr[4],2)+coef_3rd[60:75]*np.power(_vr[4],3)+coef_4th[60:75]*np.power(_vr[4],4))

gain_arr_new_when_hvmeas_400_calculated[75:90]=67.49*np.exp(coef_0th[75:90]+coef_1st[75:90]*hvmeas_arr_new_when_hvmeas_400[75:90]+coef_2nd[75:90]*np.power(hvmeas_arr_new_when_hvmeas_400[75:90],2)+coef_3rd[75:90]*np.power(hvmeas_arr_new_when_hvmeas_400[75:90],3)+coef_4th[75:90]*np.power(hvmeas_arr_new_when_hvmeas_400[75:90],4))/np.exp(coef_0th[75:90]+coef_1st[75:90]*_vr[5]+coef_2nd[75:90]*np.power(_vr[5],2)+coef_3rd[75:90]*np.power(_vr[5],3)+coef_4th[75:90]*np.power(_vr[5],4))

gain_arr_new_when_hvmeas_400_calculated[90:105]=67.49*np.exp(coef_0th[90:105]+coef_1st[90:105]*hvmeas_arr_new_when_hvmeas_400[90:105]+coef_2nd[90:105]*np.power(hvmeas_arr_new_when_hvmeas_400[90:105],2)+coef_3rd[90:105]*np.power(hvmeas_arr_new_when_hvmeas_400[90:105],3)+coef_4th[90:105]*np.power(hvmeas_arr_new_when_hvmeas_400[90:105],4))/np.exp(coef_0th[90:105]+coef_1st[90:105]*_vr[6]+coef_2nd[90:105]*np.power(_vr[6],2)+coef_3rd[90:105]*np.power(_vr[6],3)+coef_4th[90:105]*np.power(_vr[6],4))

gain_arr_new_when_hvmeas_400_calculated[105:120]=67.49*np.exp(coef_0th[105:120]+coef_1st[105:120]*hvmeas_arr_new_when_hvmeas_400[105:120]+coef_2nd[105:120]*np.power(hvmeas_arr_new_when_hvmeas_400[105:120],2)+coef_3rd[105:120]*np.power(hvmeas_arr_new_when_hvmeas_400[105:120],3)+coef_4th[105:120]*np.power(hvmeas_arr_new_when_hvmeas_400[105:120],4))/np.exp(coef_0th[105:120]+coef_1st[105:120]*_vr[7]+coef_2nd[105:120]*np.power(_vr[7],2)+coef_3rd[105:120]*np.power(_vr[7],3)+coef_4th[105:120]*np.power(_vr[7],4))
"""

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

g=0.
sb=0.
for num in range (105,120):
    num=38
    a=int(num/10)
    b=int(num%10)
    gain_ab=np.array([])
    brt_ab=np.array([])
    sb_ab=np.array([])
    for i in range (1,num_shot+1):
        myTree_with_light=Tree("spectroscopy",s+i)
        gain_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.GAIN_ARR").getData().data()
        gain_ab=np.append(gain_ab,gain_arr[a][b])
#        brt_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.BRT_ARR").getData().data()
#        brt_ab=np.append(brt_ab,np.mean(brt_arr[a][b]))
        sig_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.RESULT.SIG_ARR").getData().data()
        back_arr=myTree_with_light.getNode("gpi_tcv.APD_ARRAY.CALIBRATION.BACK_ARR").getData().data()
        sb_ab=np.append(sb_ab,back_arr[a][b]-np.mean(sig_arr[a][b]))
        myTree_with_light.close()
    
    HV_meas_sorted_ab=HV_meas_new[int((a*10+b)/15)]
    sort_ind_ab=np.argsort(HV_meas_sorted_ab)
    HV_meas_sorted_ab=np.sort(HV_meas_sorted_ab)
    temp_gain_ab=np.array([])
#    temp_brt_ab=np.array([])
    temp_sb_ab=np.array([])
    for j in range (0,len(gain_ab)):
        temp_gain_ab=np.append(temp_gain_ab,gain_ab[sort_ind_ab[j]])
#        temp_brt_ab=np.append(temp_brt_00,brt_ab[sort_ind_ab[j]])
        temp_sb_ab=np.append(temp_sb_ab,sb_ab[sort_ind_ab[j]])
    
    gain_ab=temp_gain_ab
#    brt_ab=temp_brt_ab
    sb_ab=temp_sb_ab
    
#    print(str(gain_ab-g))
#    g=gain_ab
    print(str(sb_ab-sb))
    sb=sb_ab
    plt.figure(100)
    line_100,=plt.plot(HV_meas_sorted_ab,gain_ab,".-")
    plt.xlabel('HV_meas (V)')
    plt.ylabel('gain_arr['+str(a)+']['+str(b)+']')
    plt.figure(200)
    line_200,=plt.plot(HV_meas_sorted_ab,sb_ab,".-")
    plt.xlabel('HV_meas (V)')
    plt.ylabel('sb_arr['+str(a)+']['+str(b)+']')

plt.show()
"""
plt.figure(100)
line_1,=plt.plot(HV_meas_sorted_ab,gain_ab,".-")
plt.xlabel('HV_meas (V)')
plt.ylabel('gain_arr['+str(a)+']['+str(b)+']')

#plt.figure(2)
#line_2,=plt.plot(HV_meas_sorted_ab,brt_ab,".-")
#plt.xlabel('HV_meas (V)')
#plt.ylabel('mean brt_arr['+str(a)+']['+str(b)+'] (mW/cm2/ster)')

plt.figure(3)
line_3,=plt.plot(HV_meas_sorted_ab,sb_ab,".-")
plt.xlabel('HV_meas (V)')
plt.ylabel('mean sig_minus_back ['+str(a)+']['+str(b)+'] (V)')

plt.show()
"""




#s=1180626500 #old 'new fiber' shots
#s=1180702500 #recent 'new fiber' shots
s=1180705500 #copied old 'new fiber' shots
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
plt.figure(181)
line_18_new,=plt.plot(chan_new,apprx_hvmeas_new_when_hvmeas_380,".-")
#line_18_old,=plt.plot(chan_old,gain_arr_old_when_hvmeas_380[0:90],".-")
plt.xlabel('Channel number (arbitrary)')
plt.ylabel('Apprx HV_meas when HV_meas~380V')
#plt.legend([line_18_new,line_18_old],['New_fiber','Old_fiber'])

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
#plt.legend([line_20_new,line_20_old],['New_fiber','Old_fiber'])

plt.figure(182)
line_18_new,=plt.plot(chan_new,apprx_hvmeas_new_when_hvmeas_400,".-")
#line_18_old,=plt.plot(chan_old,gain_arr_old_when_hvmeas_380[0:90],".-")
plt.xlabel('Channel number (arbitrary)')
plt.ylabel('Apprx HV_meas when HV_meas~400V')
#plt.legend([line_18_new,line_18_old],['New_fiber','Old_fiber'])

plt.figure(183)
line_18_new,=plt.plot(chan_new,gain_arr_new_when_hvmeas_400,".-")
#line_18_old,=plt.plot(chan_old,gain_arr_old_when_hvmeas_380[0:90],".-")
plt.xlabel('Channel number (arbitrary)')
plt.ylabel('Gain when HV_meas~400V')
#plt.legend([line_18_new,line_18_old],['New_fiber','Old_fiber'])

plt.figure(184)
line_20_new,=plt.plot(chan_new,mean_sb_arr_new_when_hvmeas_400,".-")
#line_20_old,=plt.plot(chan_old,mean_sb_arr_old_when_hvmeas_380[0:90],".-")
plt.xlabel('Channel number (arbitrary)')
plt.ylabel('Mean sig_minus_back (V) when HV_meas~400V')
#plt.legend([line_20_new,line_20_old],['New_fiber','Old_fiber'])

plt.figure(21)
line_21_new,=plt.plot(HV_prog_new_1_sorted,HV_meas_new_1_sorted,".-")
line_21_old,=plt.plot(HV_prog_old_1_sorted,HV_meas_old_1_sorted,".-")
plt.xlabel('HV_prog (V), Side 1 of Board 24')
plt.ylabel('HV_meas (V), Side 1 of Board 24')
plt.legend([line_21_new,line_21_old],['New_fiber','Old_fiber'])

plt.figure(22)
line_22_new,=plt.plot(HV_prog_new_2_sorted,HV_meas_new_2_sorted,".-")
line_22_old,=plt.plot(HV_prog_old_2_sorted,HV_meas_old_2_sorted,".-")
plt.xlabel('HV_prog (V), Side 2 of Board 24')
plt.ylabel('HV_meas (V), Side 2 of Board 24')
plt.legend([line_22_new,line_22_old],['New_fiber','Old_fiber'])

plt.figure(23)
line_23_new,=plt.plot(HV_prog_new_3_sorted,HV_meas_new_3_sorted,".-")
line_23_old,=plt.plot(HV_prog_old_3_sorted,HV_meas_old_3_sorted,".-")
plt.xlabel('HV_prog (V), Side 1 of Board 25')
plt.ylabel('HV_meas (V), Side 1 of Board 25')
plt.legend([line_23_new,line_23_old],['New_fiber','Old_fiber'])

plt.figure(24)
line_24_new,=plt.plot(HV_prog_new_4_sorted,HV_meas_new_4_sorted,".-")
line_24_old,=plt.plot(HV_prog_old_4_sorted,HV_meas_old_4_sorted,".-")
plt.xlabel('HV_prog (V), Side 2 of Board 25')
plt.ylabel('HV_meas (V), Side 2 of Board 25')
plt.legend([line_24_new,line_24_old],['New_fiber','Old_fiber'])

plt.figure(25)
line_25_new,=plt.plot(HV_prog_new_5_sorted,HV_meas_new_5_sorted,".-")
line_25_old,=plt.plot(HV_prog_old_5_sorted,HV_meas_old_5_sorted,".-")
plt.xlabel('HV_prog (V), Side 1 of Board 26')
plt.ylabel('HV_meas (V), Side 1 of Board 26')
plt.legend([line_25_new,line_25_old],['New_fiber','Old_fiber'])

plt.figure(26)
line_26_new,=plt.plot(HV_prog_new_6_sorted,HV_meas_new_6_sorted,".-")
line_26_old,=plt.plot(HV_prog_old_6_sorted,HV_meas_old_6_sorted,".-")
plt.xlabel('HV_prog (V), Side 2 of Board 26')
plt.ylabel('HV_meas (V), Side 2 of Board 26')
plt.legend([line_26_new,line_26_old],['New_fiber','Old_fiber'])

plt.figure(27)
line_27_new,=plt.plot(HV_prog_new_7_sorted,HV_meas_new_7_sorted,".-")
line_27_old,=plt.plot(HV_prog_old_7_sorted,HV_meas_old_7_sorted,".-")
plt.xlabel('HV_prog (V), Side 1 of Board 27')
plt.ylabel('HV_meas (V), Side 1 of Board 27')
plt.legend([line_27_new,line_27_old],['New_fiber','Old_fiber'])

plt.figure(28)
line_28_new,=plt.plot(HV_prog_new_8_sorted,HV_meas_new_8_sorted,".-")
line_28_old,=plt.plot(HV_prog_old_8_sorted,HV_meas_old_8_sorted,".-")
plt.xlabel('HV_prog (V), Side 2 of Board 27')
plt.ylabel('HV_meas (V), Side 2 of Board 27')
plt.legend([line_28_new,line_28_old],['New_fiber','Old_fiber'])

plt.show()


