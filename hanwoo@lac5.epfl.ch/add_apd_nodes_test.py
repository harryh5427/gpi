"""

"""
from MDSplus import *
import sys

s=int(sys.argv[1])
model_tree_num=-1
myTree=Tree("spectroscopy",model_tree_num)
myTree.createPulse(s)
myTree=Tree("spectroscopy",s,'Edit')
gpi_root="\SPECTROSCOPY::TOP.GPI_TCV"
myTree.addNode(gpi_root,"structure")
gpi_node=myTree.getNode(gpi_root)
gpi_node.addNode("APD_ARRAY","structure")
node_apd_array=gpi_node.getNode("APD_ARRAY")
node_apd_array.addNode("CONTROL","structure")
node_control=node_apd_array.getNode("CONTROL")
#Add nodes that contain necessary parameters for controlling digitizers
node_control.addNode("DIG_TSTART","numeric") #start time for 132
node_control.addNode("DIG_TSTOP","numeric") #stop time for 132
node_control.addNode("DIG_FREQ","numeric") # sampling frequency of digitizers (unit: MHz)
node_control.addNode("DIG_SAMPS","numeric") # number of samples of digitizers
node_control.getNode("DIG_TSTART").putData(0.)
node_control.getNode("DIG_TSTOP").putData(.9)
node_control.getNode("DIG_FREQ").putData(2.)
node_control.getNode("DIG_SAMPS").putData(myTree.tdiCompile("_tstart = "+gpi_root+".APD_ARRAY.CONTROL:DIG_TSTART, _tstop = "+gpi_root+".APD_ARRAY.CONTROL:DIG_TSTOP, _freq = "+gpi_root+".APD_ARRAY.CONTROL:DIG_FREQ, _nksamp = (_tstop - _tstart) * _freq * 1000E3 / 1024 + .5, _ksamp_int = INT(_nksamp)"))

#Add a hardware structure node
node_apd_array.addNode("HARDWARE","structure")
node_hardware=node_apd_array.getNode("HARDWARE")

#Add a calibration structure node
node_apd_array.addNode("CALIBRATION","structure")
node_calib=node_apd_array.getNode("CALIBRATION")

#Add a result structure node
node_apd_array.addNode("RESULT","structure")
node_result=node_apd_array.getNode("RESULT")

#Add devices under the hardware node
node_hardware.addDevice("ACQ196","acq196")
node_hardware.addDevice("ACQ196AO","acq196ao")
node_hardware.addDevice("DIO2","dio2")
node_hardware.addDevice("ACQ132_1","acq132")
node_hardware.addDevice("ACQ132_2","acq132")
node_hardware.addDevice("ACQ132_3","acq132")
node_hardware.addDevice("ACQ132_4","acq132")

#Add a node for HV measured array
node_result.addNode("HV_MEAS_ARR","numeric")
hv_meas_arr_str="_hv_meas=[MAXVAL("
for i in range (1,9):
    #Add nodes for HV programmed values, 8 for 8 cathodes
    node_control.addNode("HV_PROG_"+str(i),"numeric")
    node_control.getNode("HV_PROG_"+str(i)).putData(3.)
    #Make the ACQ196AO's output nodes to refer the value from HV prog nodes.
#    node_hardware.getNode("ACQ196AO.OUTPUT_0"+str(i)).putData(myTree.tdiCompile("Build_Signal(["+node_control.getNode("HV_PROG_"+str(i)).getFullPath()+","+node_control.getNode("HV_PROG_"+str(i)).getFullPath()+"],*,["+node_control.getNode("DIG_TSTART").getFullPath()+"-1.0,"+node_control.getNode("DIG_TSTOP").getFullPath()+"+1.0])"))
    hv_meas_arr_str=hv_meas_arr_str+node_control.getNode("HV_PROG_"+str(i)).getFullPath()+")"
    if i!=8:
        hv_meas_arr_str=hv_meas_arr_str+",MAXVAL("
    else:
        hv_meas_arr_str=hv_meas_arr_str+"],_hv_meas_arr=["

for i in range (1,9):
    if i%2==1:
        hv_meas_arr_str=hv_meas_arr_str+"replicate([_hv_meas["+str(i-1)+"]],0,10),"
    else:
        hv_meas_arr_str=hv_meas_arr_str+"set_range(10,[replicate([_hv_meas["+str(i-2)+"]],0,5),replicate([_hv_meas["+str(i-1)+"]],0,5)]),replicate([_hv_meas["+str(i-1)+"]],0,10)"
        if i!=8:
            hv_meas_arr_str=hv_meas_arr_str+","
        else:
            hv_meas_arr_str=hv_meas_arr_str+"]"

node_result.getNode("HV_MEAS_ARR").putData(myTree.tdiCompile(hv_meas_arr_str))

#Add a filter array, and nodes under it: VALUE and COMMENT
node_control.addNode("FILTER","structure")
node_control.getNode("FILTER").addNode("COMMENT","text")
node_control.getNode("FILTER").addNode("VALUE","text")
node_control.getNode("FILTER.COMMENT").putData("values of filters: DA6563, HEI5876, HEI6670, HEII4686, OPEN")
node_control.getNode("FILTER.VALUE").putData("HEI5876")

#Add S_LAMBDA arrays for each filter. Brightness = (S_LAMBDA / GAIN_ARR) X (BACK_ARR-SIG_ARR)
node_calib.addNode("S_L_DA6563","numeric")
node_calib.addNode("S_L_HEI5876","numeric")
node_calib.addNode("S_L_HEI6670","numeric")
node_calib.addNode("S_L_HEII4686","numeric")
node_calib.addNode("S_L_OPEN","numeric")

#Add a mean signal array. This is needed just for the calibration.
node_calib.addNode("MEAN_SIG_ARR","numeric")
mean_sig_arr="["
for i in range (0,120):
    if (i+1)%10==1:
        mean_sig_arr=mean_sig_arr+"["
    if i%30+1<10:
        mean_sig_arr=mean_sig_arr+"MEAN("+node_hardware.getNode("ACQ132_"+str(i/30+1)+".INPUT_0"+str(i%30+1)).getFullPath()+")"
    else:
        mean_sig_arr=mean_sig_arr+"MEAN("+node_hardware.getNode("ACQ132_"+str(i/30+1)+".INPUT_"+str(i%30+1)).getFullPath()+")"
    if (i+1)%10==0:
        mean_sig_arr=mean_sig_arr+"]"
    if i!=119:
        mean_sig_arr=mean_sig_arr+","
    else:
        mean_sig_arr=mean_sig_arr+"]"

node_calib.getNode("MEAN_SIG_ARR").putData(myTree.tdiCompile(mean_sig_arr))

#Add a signal array
node_result.addNode("SIG_ARR","signal")
sig_arr="["
for i in range (0,120):
    if (i+1)%10==1:
        sig_arr=sig_arr+"["
    if i%30+1<10:
        sig_arr=sig_arr+"replicate([1.],0,2E6)"
    else:
        sig_arr=sig_arr+"replicate([1.],0,2E6)"
    if (i+1)%10==0:
        sig_arr=sig_arr+"]"
    if i!=119:
        sig_arr=sig_arr+","
    else:
        sig_arr=sig_arr+"]"

node_result.getNode("SIG_ARR").putData(myTree.tdiCompile(sig_arr))

print("sig_arr done")

#Add a background array
node_calib.addNode("BACK_ARR","numeric")

#Add coefficient arrays
node_calib.addNode("COEF_0TH_ARR","numeric")
node_calib.addNode("COEF_1ST_ARR","numeric")
node_calib.addNode("COEF_2ND_ARR","numeric")
node_calib.addNode("COEF_3RD_ARR","numeric")
node_calib.addNode("COEF_4TH_ARR","numeric")

dum=-10.
dum_coef_arr_1=[[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum]]
dum=9.
dum_coef_arr_2=[[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum]]
dum=-4.
dum_coef_arr_3=[[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum]]
dum=.9
dum_coef_arr_4=[[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum]]
dum=-.07
dum_coef_arr_5=[[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum]]
node_calib.getNode("COEF_0TH_ARR").putData(myTree.tdiCompile(str(dum_coef_arr_1)))
node_calib.getNode("COEF_1ST_ARR").putData(myTree.tdiCompile(str(dum_coef_arr_2)))
node_calib.getNode("COEF_2ND_ARR").putData(myTree.tdiCompile(str(dum_coef_arr_3)))
node_calib.getNode("COEF_3RD_ARR").putData(myTree.tdiCompile(str(dum_coef_arr_4)))
node_calib.getNode("COEF_4TH_ARR").putData(myTree.tdiCompile(str(dum_coef_arr_5)))

dum=1.
dum_slambda_arr=[[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum]]
node_calib.getNode("S_L_DA6563").putData(myTree.tdiCompile(str(dum_slambda_arr)))
node_calib.getNode("S_L_HEI5876").putData(myTree.tdiCompile(str(dum_slambda_arr)))
node_calib.getNode("S_L_HEI6670").putData(myTree.tdiCompile(str(dum_slambda_arr)))
node_calib.getNode("S_L_HEII4686").putData(myTree.tdiCompile(str(dum_slambda_arr)))
node_calib.getNode("S_L_OPEN").putData(myTree.tdiCompile(str(dum_slambda_arr)))

dum=1.5
dum_back_arr=[[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum],[dum,dum,dum,dum,dum,dum,dum,dum,dum,dum]]
node_calib.getNode("BACK_ARR").putData(myTree.tdiCompile(str(dum_back_arr)))


#Add a gain array. Values are an 10 by 12 array, and each component is 50 * exp(polynomial(HV_measured))
node_result.addNode("GAIN_ARR","numeric")
gain_arr="_c0="+node_calib.getNode("COEF_0TH_ARR").getFullPath()+",_c1="+node_calib.getNode("COEF_1ST_ARR").getFullPath()+",_c2="+node_calib.getNode("COEF_2ND_ARR").getFullPath()+",_c3="+node_calib.getNode("COEF_3RD_ARR").getFullPath()+",_c4="+node_calib.getNode("COEF_4TH_ARR").getFullPath()+",_hv_meas_arr="+node_result.getNode("HV_MEAS_ARR").getFullPath()+",_gain_arr=50.*exp(_c0+_c1*_hv_meas_arr+_c2*_hv_meas_arr^2+_c3*_hv_meas_arr^3+_c4*_hv_meas_arr^4)"
node_result.getNode("GAIN_ARR").putData(myTree.tdiCompile(gain_arr))

#Add a brightness array
node_result.addNode("BRT_ARR","signal")
brt_arr="_gain="+node_result.getNode("GAIN_ARR").getFullPath()+",_back="+node_calib.getNode("BACK_ARR").getFullPath()+",_sig_series="+node_result.getNode("SIG_ARR").getFullPath()+","
filter_list=['DA6563','HEI5876','HEI6670','HEII4686','OPEN']
for i in range (0,5):
    brt_arr=brt_arr+"IF(UPCASE("+node_control.getNode("FILTER.VALUE").getFullPath()+")=='"+filter_list[i]+"',_slambda="+node_calib.getNode("S_L_"+filter_list[i]).getFullPath()+"),"

brt_arr=brt_arr+"_back_series=replicate([_back],2,size(_sig_series,0)),_sensitivity_series=replicate([_slambda/_gain],2,size(_sig_series,0)),_brt_series=(-_sig_series+_back_series)*_sensitivity_series"
node_result.getNode("BRT_ARR").putData(myTree.tdiCompile(brt_arr))

myTree.write() #save the edited tree

print(str(node_result.getNode("BRT_ARR").getData().data()))
myTree.close() #close the tree
