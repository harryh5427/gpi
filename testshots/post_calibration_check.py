from MDSplus import *
import numpy as np
import sys
import matplotlib.pyplot as plt

s=int(sys.argv[1])
num_shot=20
gpi_root="\SPECTROSCOPY::TOP.GPI_TCV"

hv_prog=[]
for i in range (1,num_shot+1):
    myTree_with_light=Tree("spectroscopy",s+i)
    hv_prog.append(myTree_with_light.getNode('gpi_tcv.apd_array.control.hv_prog_1').getData().data())

min_ind=np.argmin(hv_prog)
max_ind=np.argmax(hv_prog)

myTree_min_light=Tree("spectroscopy",s+1+min_ind)
myTree_max_light=Tree("spectroscopy",s+1+max_ind)
gain_arr_min=myTree_min_light.getNode(gpi_root+".APD_ARRAY.RESULT.GAIN_ARR").getData().data()
gain_arr_max=myTree_max_light.getNode(gpi_root+".APD_ARRAY.RESULT.GAIN_ARR").getData().data()
gain_arr_diff=gain_arr_max-gain_arr_min
print(gain_arr_diff)

HV_meas=[[],[],[],[],[],[],[],[]]
HV_prog=[[],[],[],[],[],[],[],[]]
for i in range (1,num_shot+1):
    myTree_with_light=Tree("spectroscopy",s+i)
    HV_meas_arr=myTree_with_light.getNode(gpi_root+".APD_ARRAY.RESULT.HV_MEAS_ARR").getData().data()
    HV_meas[0].append(HV_meas_arr[0][0])
    HV_meas[1].append(HV_meas_arr[1][5])
    HV_meas[2].append(HV_meas_arr[3][0])
    HV_meas[3].append(HV_meas_arr[4][5])
    HV_meas[4].append(HV_meas_arr[6][0])
    HV_meas[5].append(HV_meas_arr[7][5])
    HV_meas[6].append(HV_meas_arr[9][0])
    HV_meas[7].append(HV_meas_arr[10][5])
    HV_prog[0].append(myTree_with_light.getNode(gpi_root+".APD_ARRAY.CONTROL.HV_PROG_1").getData().data())
    HV_prog[1].append(myTree_with_light.getNode(gpi_root+".APD_ARRAY.CONTROL.HV_PROG_2").getData().data())
    HV_prog[2].append(myTree_with_light.getNode(gpi_root+".APD_ARRAY.CONTROL.HV_PROG_3").getData().data())
    HV_prog[3].append(myTree_with_light.getNode(gpi_root+".APD_ARRAY.CONTROL.HV_PROG_4").getData().data())
    HV_prog[4].append(myTree_with_light.getNode(gpi_root+".APD_ARRAY.CONTROL.HV_PROG_5").getData().data())
    HV_prog[5].append(myTree_with_light.getNode(gpi_root+".APD_ARRAY.CONTROL.HV_PROG_6").getData().data())
    HV_prog[6].append(myTree_with_light.getNode(gpi_root+".APD_ARRAY.CONTROL.HV_PROG_7").getData().data())
    HV_prog[7].append(myTree_with_light.getNode(gpi_root+".APD_ARRAY.CONTROL.HV_PROG_8").getData().data())
    myTree_with_light.close()

sort_ind_1=np.argsort(HV_prog[0])
sort_ind_2=np.argsort(HV_prog[1])
sort_ind_3=np.argsort(HV_prog[2])
sort_ind_4=np.argsort(HV_prog[3])
sort_ind_5=np.argsort(HV_prog[4])
sort_ind_6=np.argsort(HV_prog[5])
sort_ind_7=np.argsort(HV_prog[6])
sort_ind_8=np.argsort(HV_prog[7])
HV_prog_1_sorted=np.sort(HV_prog[0])
HV_prog_2_sorted=np.sort(HV_prog[1])
HV_prog_3_sorted=np.sort(HV_prog[2])
HV_prog_4_sorted=np.sort(HV_prog[3])
HV_prog_5_sorted=np.sort(HV_prog[4])
HV_prog_6_sorted=np.sort(HV_prog[5])
HV_prog_7_sorted=np.sort(HV_prog[6])
HV_prog_8_sorted=np.sort(HV_prog[7])
HV_meas_1_sorted=np.array([])
HV_meas_2_sorted=np.array([])
HV_meas_3_sorted=np.array([])
HV_meas_4_sorted=np.array([])
HV_meas_5_sorted=np.array([])
HV_meas_6_sorted=np.array([])
HV_meas_7_sorted=np.array([])
HV_meas_8_sorted=np.array([])
for j in range (0,len(HV_prog_1_sorted)):
    HV_meas_1_sorted=np.append(HV_meas_1_sorted,HV_meas[0][sort_ind_1[j]])
    HV_meas_2_sorted=np.append(HV_meas_2_sorted,HV_meas[1][sort_ind_2[j]])
    HV_meas_3_sorted=np.append(HV_meas_3_sorted,HV_meas[2][sort_ind_3[j]])
    HV_meas_4_sorted=np.append(HV_meas_4_sorted,HV_meas[3][sort_ind_4[j]])
    HV_meas_5_sorted=np.append(HV_meas_5_sorted,HV_meas[4][sort_ind_5[j]])
    HV_meas_6_sorted=np.append(HV_meas_6_sorted,HV_meas[5][sort_ind_6[j]])
    HV_meas_7_sorted=np.append(HV_meas_7_sorted,HV_meas[6][sort_ind_7[j]])
    HV_meas_8_sorted=np.append(HV_meas_8_sorted,HV_meas[7][sort_ind_8[j]])

gain_arr_when_hvmeas_380=np.array([])
mean_brt_arr_when_hvmeas_380=np.array([])
mean_sb_arr_when_hvmeas_380=np.array([])
apprx_hvmeas_when_hvmeas_380=np.array([])
gain_arr_when_hvmeas_400=np.array([])
mean_brt_arr_when_hvmeas_400=np.array([])
mean_sb_arr_when_hvmeas_400=np.array([])
apprx_hvmeas_when_hvmeas_400=np.array([])
for i in range (0,8):
    ind_hvmeas_380=np.abs(np.array(HV_meas[i])-380.).argmin()
    myTree_with_light=Tree("spectroscopy",s+ind_hvmeas_380+1)
    gain_arr=myTree_with_light.getNode(gpi_root+".APD_ARRAY.RESULT.GAIN_ARR").getData().data()
#    brt_arr=myTree_with_light.getNode(gpi_root+".APD_ARRAY.RESULT.BRT_ARR").getData().data()
    sig_arr=myTree_with_light.getNode(gpi_root+".APD_ARRAY.RESULT.SIG_ARR").getData().data()
    back_arr=myTree_with_light.getNode(gpi_root+".APD_ARRAY.CALIBRATION.BACK_ARR").getData().data()
    for j in range(i*15,(i+1)*15):
        gain_arr_when_hvmeas_380=np.append(gain_arr_when_hvmeas_380,gain_arr[j/10][j%10])
#        mean_brt_arr_when_hvmeas_380=np.append(mean_brt_arr_when_hvmeas_380,np.mean(brt_arr[j/10][j%10]))
        mean_sb_arr_when_hvmeas_380=np.append(mean_sb_arr_when_hvmeas_380,back_arr[j/10][j%10]-np.mean(sig_arr[j/10][j%10]))
        apprx_hvmeas_when_hvmeas_380=np.append(apprx_hvmeas_when_hvmeas_380,np.array(HV_meas[i])[ind_hvmeas_380])
    myTree_with_light.close()
    ind_hvmeas_400=np.abs(np.array(HV_meas[i])-400.).argmin()
    myTree_with_light=Tree("spectroscopy",s+ind_hvmeas_400+1)
    gain_arr=myTree_with_light.getNode(gpi_root+".APD_ARRAY.RESULT.GAIN_ARR").getData().data()
#    brt_arr=myTree_with_light.getNode(gpi_root+".APD_ARRAY.RESULT.BRT_ARR").getData().data()
    sig_arr=myTree_with_light.getNode(gpi_root+".APD_ARRAY.RESULT.SIG_ARR").getData().data()
    back_arr=myTree_with_light.getNode(gpi_root+".APD_ARRAY.CALIBRATION.BACK_ARR").getData().data()
    for j in range(i*15,(i+1)*15):
        gain_arr_when_hvmeas_400=np.append(gain_arr_when_hvmeas_400,gain_arr[j/10][j%10])
#        mean_brt_arr_when_hvmeas_400=np.append(mean_brt_arr_when_hvmeas_400,np.mean(brt_arr[j/10][j%10]))
        mean_sb_arr_when_hvmeas_400=np.append(mean_sb_arr_when_hvmeas_400,back_arr[j/10][j%10]-np.mean(sig_arr[j/10][j%10]))
        apprx_hvmeas_when_hvmeas_400=np.append(apprx_hvmeas_when_hvmeas_400,np.array(HV_meas[i])[ind_hvmeas_400])
    myTree_with_light.close()

gain_00=np.array([])
gain_30=np.array([])
gain_60=np.array([])
gain_90=np.array([])
brt_00=np.array([])
brt_30=np.array([])
brt_60=np.array([])
brt_90=np.array([])
sb_00=np.array([])
sb_30=np.array([])
sb_60=np.array([])
sb_90=np.array([])
for i in range (1,num_shot+1):
    myTree_with_light=Tree("spectroscopy",s+i)
    gain_arr=myTree_with_light.getNode(gpi_root+".APD_ARRAY.RESULT.GAIN_ARR").getData().data()
    gain_00=np.append(gain_00,gain_arr[0][0])
    gain_30=np.append(gain_30,gain_arr[3][0])
    gain_60=np.append(gain_60,gain_arr[6][0])
    gain_90=np.append(gain_90,gain_arr[9][0])
    brt_arr=myTree_with_light.getNode(gpi_root+".APD_ARRAY.RESULT.BRT_ARR").getData().data()
    brt_00=np.append(brt_00,np.mean(brt_arr[0][0]))
    brt_30=np.append(brt_30,np.mean(brt_arr[3][0]))
    brt_60=np.append(brt_60,np.mean(brt_arr[6][0]))
    brt_90=np.append(brt_90,np.mean(brt_arr[9][0]))
    sig_arr=myTree_with_light.getNode(gpi_root+".APD_ARRAY.RESULT.SIG_ARR").getData().data()
    back_arr=myTree_with_light.getNode(gpi_root+".APD_ARRAY.CALIBRATION.BACK_ARR").getData().data()
    sb_00=np.append(sb_00,back_arr[0][0]-np.mean(sig_arr[0][0]))
    sb_30=np.append(sb_30,back_arr[3][0]-np.mean(sig_arr[3][0]))
    sb_60=np.append(sb_60,back_arr[6][0]-np.mean(sig_arr[6][0]))
    sb_90=np.append(sb_90,back_arr[9][0]-np.mean(sig_arr[9][0]))
    myTree_with_light.close()

#HV_meas_sorted=HV_meas[(a*10+b)/15]
HV_meas_sorted_00=HV_meas[(0*10+0)/15]
HV_meas_sorted_30=HV_meas[(3*10+0)/15]
HV_meas_sorted_60=HV_meas[(6*10+0)/15]
HV_meas_sorted_90=HV_meas[(9*10+0)/15]
sort_ind_00=np.argsort(HV_meas_sorted_00)
sort_ind_30=np.argsort(HV_meas_sorted_30)
sort_ind_60=np.argsort(HV_meas_sorted_60)
sort_ind_90=np.argsort(HV_meas_sorted_90)
HV_meas_sorted_00=np.sort(HV_meas_sorted_00)
HV_meas_sorted_30=np.sort(HV_meas_sorted_30)
HV_meas_sorted_60=np.sort(HV_meas_sorted_60)
HV_meas_sorted_90=np.sort(HV_meas_sorted_90)
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
for j in range (0,len(gain_00)):
    temp_gain_00=np.append(temp_gain_00,gain_00[sort_ind_00[j]])
    temp_gain_30=np.append(temp_gain_30,gain_30[sort_ind_30[j]])
    temp_gain_60=np.append(temp_gain_60,gain_60[sort_ind_60[j]])
    temp_gain_90=np.append(temp_gain_90,gain_90[sort_ind_90[j]])
    temp_brt_00=np.append(temp_brt_00,brt_00[sort_ind_00[j]])
    temp_brt_30=np.append(temp_brt_30,brt_30[sort_ind_30[j]])
    temp_brt_60=np.append(temp_brt_60,brt_60[sort_ind_60[j]])
    temp_brt_90=np.append(temp_brt_90,brt_90[sort_ind_90[j]])
    temp_sb_00=np.append(temp_sb_00,sb_00[sort_ind_00[j]])
    temp_sb_30=np.append(temp_sb_30,sb_30[sort_ind_30[j]])
    temp_sb_60=np.append(temp_sb_60,sb_60[sort_ind_60[j]])
    temp_sb_90=np.append(temp_sb_90,sb_90[sort_ind_90[j]])

gain_00=temp_gain_00
gain_30=temp_gain_30
gain_60=temp_gain_60
gain_90=temp_gain_90
brt_00=temp_brt_00
brt_30=temp_brt_30
brt_60=temp_brt_60
brt_90=temp_brt_90
sb_00=temp_sb_00
sb_30=temp_sb_30
sb_60=temp_sb_60
sb_90=temp_sb_90

plt.figure(1)
line_1,=plt.plot(HV_meas_sorted_00,gain_00,".-")
plt.xlabel('HV_meas (V)')
plt.ylabel('gain_arr[0][0] (from Board 24)')

plt.figure(2)
line_2,=plt.plot(HV_meas_sorted_30,gain_30,".-")
plt.xlabel('HV_meas (V)')
plt.ylabel('gain_arr[3][0] (from Board 25)')

plt.figure(3)
line_3,=plt.plot(HV_meas_sorted_60,gain_60,".-")
plt.xlabel('HV_meas (V)')
plt.ylabel('gain_arr[6][0] (from Board 26)')

plt.figure(4)
line_4,=plt.plot(HV_meas_sorted_90,gain_90,".-")
plt.xlabel('HV_meas (V)')
plt.ylabel('gain_arr[9][0] (from Board 27)')

plt.figure(5)
line_5,=plt.plot(HV_meas_sorted_00,brt_00,".-")
plt.xlabel('HV_meas (V)')
plt.ylabel('mean brt_arr[0][0] (mW/cm2/ster) (from Board 24)')

plt.figure(6)
line_6,=plt.plot(HV_meas_sorted_30,brt_30,".-")
plt.xlabel('HV_meas (V)')
plt.ylabel('mean brt_arr[3][0] (mW/cm2/ster) (from Board 25)')

plt.figure(7)
line_7,=plt.plot(HV_meas_sorted_60,brt_60,".-")
plt.xlabel('HV_meas (V)')
plt.ylabel('mean brt_arr[6][0] (mW/cm2/ster) (from Board 26)')

plt.figure(8)
line_8,=plt.plot(HV_meas_sorted_90,brt_90,".-")
plt.xlabel('HV_meas (V)')
plt.ylabel('mean brt_arr[9][0] (mW/cm2/ster) (from Board 27)')

plt.figure(9)
line_9,=plt.plot(HV_meas_sorted_00,sb_00,".-")
plt.xlabel('HV_meas (V)')
plt.ylabel('mean sig_minus_back [0][0] (V) (from Board 24)')

plt.figure(10)
line_10,=plt.plot(HV_meas_sorted_30,sb_30,".-")
plt.xlabel('HV_meas (V)')
plt.ylabel('mean sig_minus_back [3][0] (V) (from Board 25)')

plt.figure(11)
line_11,=plt.plot(HV_meas_sorted_60,sb_60,".-")
plt.xlabel('HV_meas (V)')
plt.ylabel('mean sig_minus_back [6][0] (V) (from Board 26)')

plt.figure(12)
line_12,=plt.plot(HV_meas_sorted_90,sb_90,".-")
plt.xlabel('HV_meas (V)')
plt.ylabel('mean sig_minus_back [9][0] (V) (from Board 27)')

chan=np.arange(120)

plt.figure(13)
line_13_1,=plt.plot(HV_prog_1_sorted,HV_meas_1_sorted,".-")
line_13_2,=plt.plot(HV_prog_2_sorted,HV_meas_2_sorted,".-")
line_13_3,=plt.plot(HV_prog_3_sorted,HV_meas_3_sorted,".-")
line_13_4,=plt.plot(HV_prog_4_sorted,HV_meas_4_sorted,".-")
line_13_5,=plt.plot(HV_prog_5_sorted,HV_meas_5_sorted,".-")
line_13_6,=plt.plot(HV_prog_6_sorted,HV_meas_6_sorted,".-")
line_13_7,=plt.plot(HV_prog_7_sorted,HV_meas_7_sorted,".-")
line_13_8,=plt.plot(HV_prog_8_sorted,HV_meas_8_sorted,".-")
plt.xlabel('HV_prog (V)')
plt.ylabel('HV_meas (V)')
plt.xlim(2.8,5.)
plt.legend([line_13_1,line_13_2,line_13_3,line_13_4,line_13_5,line_13_6,line_13_7,line_13_8],['Side 1 of Board 24','Side 2 of Board 24','Side 1 of Board 25','Side 2 of Board 25','Side 1 of Board 26','Side 2 of Board 26','Side 1 of Board 27','Side 2 of Board 27'])

plt.figure(14)
line_14,=plt.plot(chan,apprx_hvmeas_when_hvmeas_380,".-")
plt.xlabel('Channel number (arbitrary)')
plt.ylabel('HV_meas when HV_meas~380V')

plt.figure(15)
line_15,=plt.plot(chan,gain_arr_when_hvmeas_380,".-")
plt.xlabel('Channel number (arbitrary)')
plt.ylabel('Gain when HV_meas~380V')

plt.figure(16)
line_16,=plt.plot(chan,mean_sb_arr_when_hvmeas_380,".-")
plt.xlabel('Channel number (arbitrary)')
plt.ylabel('Mean sig_minus_back (V) when HV_meas~380V')

plt.figure(17)
line_17,=plt.plot(chan,apprx_hvmeas_when_hvmeas_400,".-")
plt.xlabel('Channel number (arbitrary)')
plt.ylabel('HV_meas when HV_meas~400V')

plt.figure(18)
line_18,=plt.plot(chan,gain_arr_when_hvmeas_400,".-")
plt.xlabel('Channel number (arbitrary)')
plt.ylabel('Gain when HV_meas~400V')

plt.figure(19)
line_19,=plt.plot(chan,mean_sb_arr_when_hvmeas_400,".-")
plt.xlabel('Channel number (arbitrary)')
plt.ylabel('Mean sig_minus_back (V) when HV_meas~400V')

plt.show()


