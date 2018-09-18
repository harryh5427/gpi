import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline

#Import labsphere spectrum from 2015 calibration
lines = [line.rstrip('\n') for line in open('labsphere_spetrum_2015.txt')]
x_ls_2015=np.array([])
y_ls_2015=np.array([])
for i in range(0,len(lines)):
    x_ls_2015=np.append(x_ls_2015,float(lines[i].split(" ")[0]))
    y_ls_2015=np.append(y_ls_2015,float(lines[i].split(" ")[1]))

#Import 7.18 A labsphere spectrum from 2016 calibration
lines = [line.rstrip('\n') for line in open('labsphere_spetrum_2016_7_18A.txt')]
x_ls_2016_718=np.array([])
y_ls_2016_718=np.array([])
for i in range(0,len(lines)):
    x_ls_2016_718=np.append(x_ls_2016_718,float(lines[i].split(" ")[0]))
    y_ls_2016_718=np.append(y_ls_2016_718,float(lines[i].split(" ")[1]))

#Import 8.15 A labsphere spectrum from 2016 calibration
lines = [line.rstrip('\n') for line in open('labsphere_spetrum_2016_8_15A.txt')]
x_ls_2016_815=np.array([])
y_ls_2016_815=np.array([])
for i in range(0,len(lines)):
    x_ls_2016_815=np.append(x_ls_2016_815,float(lines[i].split(" ")[0]))
    y_ls_2016_815=np.append(y_ls_2016_815,float(lines[i].split(" ")[1]))

#Import transfer function of the OLD Da-6563 filter
lines = [line.rstrip('\n') for line in open('transfer_function_da_6563_old.txt')]
x_da_old=np.array([])
y_da_old=np.array([])
for i in range(0,len(lines)):
    x_da_old=np.append(x_da_old,float(lines[i].split(" ")[0]))
    y_da_old=np.append(y_da_old,float(lines[i].split(" ")[1]))

#Import transfer function of the NEW Da-6563 filter
lines = [line.rstrip('\n') for line in open('transfer_function_da_6563_new.txt')]
x_da_new=np.array([])
y_da_new=np.array([])
for i in range(0,len(lines)):
    x_da_new=np.append(x_da_new,float(lines[i].split(" ")[0]))
    y_da_new=np.append(y_da_new,float(lines[i].split(" ")[1]))

#Import transfer function of the HeI-5876 filter
lines = [line.rstrip('\n') for line in open('transfer_function_hei_5876.txt')]
x_hei=np.array([])
y_hei=np.array([])
for i in range(0,len(lines)):
    x_hei=np.append(x_hei,float(lines[i].split(" ")[0]))
    y_hei=np.append(y_hei,float(lines[i].split(" ")[1]))

brt_ls_2015_da_old=np.trapz(spline(x_ls_2015,y_ls_2015,x_da_old)*y_da_old,x_da_old)
brt_ls_2015_da_new=np.trapz(spline(x_ls_2015,y_ls_2015,x_da_new)*y_da_new,x_da_new)
brt_ls_2015_hei=np.trapz(spline(x_ls_2015,y_ls_2015,x_hei)*y_hei,x_hei)
brt_ls_2016_718_da_old=np.trapz(spline(x_ls_2016_718,y_ls_2016_718,x_da_old)*y_da_old,x_da_old)
brt_ls_2016_718_da_new=np.trapz(spline(x_ls_2016_718,y_ls_2016_718,x_da_new)*y_da_new,x_da_new)
brt_ls_2016_718_hei=np.trapz(spline(x_ls_2016_718,y_ls_2016_718,x_hei)*y_hei,x_hei)
brt_ls_2016_815_da_old=np.trapz(spline(x_ls_2016_815,y_ls_2016_815,x_da_old)*y_da_old,x_da_old)
brt_ls_2016_815_da_new=np.trapz(spline(x_ls_2016_815,y_ls_2016_815,x_da_new)*y_da_new,x_da_new)
brt_ls_2016_815_hei=np.trapz(spline(x_ls_2016_815,y_ls_2016_815,x_hei)*y_hei,x_hei)

print('Brightness of Labsphere from 2015 calibration with OLD Da filter: '+str(brt_ls_2015_da_old)+' mW/cm2/ster')
print('Brightness of Labsphere from 2015 calibration with NEW Da filter: '+str(brt_ls_2015_da_new)+' mW/cm2/ster')
print('Brightness of Labsphere from 2015 calibration with HeI filter: '+str(brt_ls_2015_hei)+' mW/cm2/ster')
print('Brightness of Labsphere from 2016 calibration (7.18 A) with OLD Da filter: '+str(brt_ls_2016_718_da_old)+' mW/cm2/ster')
print('Brightness of Labsphere from 2016 calibration (7.18 A) with NEW Da filter: '+str(brt_ls_2016_718_da_new)+' mW/cm2/ster')
print('Brightness of Labsphere from 2016 calibration (7.18 A) with HeI filter: '+str(brt_ls_2016_718_hei)+' mW/cm2/ster')
print('Brightness of Labsphere from 2016 calibration (8.15 A) with OLD Da filter: '+str(brt_ls_2016_815_da_old)+' mW/cm2/ster')
print('Brightness of Labsphere from 2016 calibration (8.15 A) with NEW Da filter: '+str(brt_ls_2016_815_da_new)+' mW/cm2/ster')
print('Brightness of Labsphere from 2016 calibration (8.15 A) with HeI filter: '+str(brt_ls_2016_815_hei)+' mW/cm2/ster')

fig1, ax_ls_1 = plt.subplots()
ax_filt_1 = ax_ls_1.twinx()
p1_ls_2015,=ax_ls_1.plot(x_ls_2015,y_ls_2015,'black')
p1_da_old,=ax_filt_1.plot(x_da_old,y_da_old)
p1_da_new,=ax_filt_1.plot(x_da_new,y_da_new)
p1_hei,=ax_filt_1.plot(x_hei,y_hei)
p1_da_line,=ax_filt_1.plot([656.3,656.3],[0.,1.],'k--')
p1_hei_line,=ax_filt_1.plot([587.6,587.6],[0.,1.],'k--')
ax_ls_1.set_xlabel('Wavelength (nm)')
ax_ls_1.set_ylabel('Radiance (mW/cm2/ster/nm)')
ax_ls_1.tick_params('y', colors='black')
ax_filt_1.set_ylabel('Transmission (%)')
ax_filt_1.set_ylim(0.,1.)
ax_ls_1.legend([p1_ls_2015],['Labsphere (2015)'],loc=2)
ax_filt_1.legend([p1_da_old,p1_da_new,p1_hei],['Da (old)','Da (new)','HeI'],loc=4)

fig2, ax_ls_2 = plt.subplots()
ax_filt_2 = ax_ls_2.twinx()
p1_ls_2016_718,=ax_ls_2.plot(x_ls_2016_718,y_ls_2016_718,'black')
p1_da_old,=ax_filt_2.plot(x_da_old,y_da_old)
p1_da_new,=ax_filt_2.plot(x_da_new,y_da_new)
p1_hei,=ax_filt_2.plot(x_hei,y_hei)
p1_da_line,=ax_filt_2.plot([656.3,656.3],[0.,1.],'k--')
p1_hei_line,=ax_filt_2.plot([587.6,587.6],[0.,1.],'k--')
ax_ls_2.set_xlabel('Wavelength (nm)')
ax_ls_2.set_ylabel('Radiance (mW/cm2/ster/nm)')
ax_ls_2.tick_params('y', colors='black')
ax_filt_2.set_ylabel('Transmission (%)')
ax_filt_2.set_ylim(0.,1.)
ax_ls_2.legend([p1_ls_2016_718],['Labsphere (2016,7.18A)'],loc=2)
ax_filt_2.legend([p1_da_old,p1_da_new,p1_hei],['Da (old)','Da (new)','HeI'],loc=4)

fig3, ax_ls_3 = plt.subplots()
ax_filt_3 = ax_ls_3.twinx()
p1_ls_2016_815,=ax_ls_3.plot(x_ls_2016_815,y_ls_2016_815,'black')
p1_da_old,=ax_filt_3.plot(x_da_old,y_da_old)
p1_da_new,=ax_filt_3.plot(x_da_new,y_da_new)
p1_hei,=ax_filt_3.plot(x_hei,y_hei)
p1_da_line,=ax_filt_3.plot([656.3,656.3],[0.,1.],'k--')
p1_hei_line,=ax_filt_3.plot([587.6,587.6],[0.,1.],'k--')
ax_ls_3.set_xlabel('Wavelength (nm)')
ax_ls_3.set_ylabel('Radiance (mW/cm2/ster/nm)')
ax_ls_3.tick_params('y', colors='black')
ax_filt_3.set_ylabel('Transmission (%)')
ax_filt_3.set_ylim(0.,1.)
ax_ls_3.legend([p1_ls_2016_815],['Labsphere (2016,8.15A)'],loc=2)
ax_filt_3.legend([p1_da_old,p1_da_new,p1_hei],['Da (old)','Da (new)','HeI'],loc=4)

plt.show()

