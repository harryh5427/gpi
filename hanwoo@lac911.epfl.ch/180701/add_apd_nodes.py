"""
Adds and populates nodes for GPI, in the model tree. Run this before running run_testshots_for_calib.py.
"""
from MDSplus import *

model_tree_num=-1
myTree=Tree("spectroscopy",model_tree_num,'Edit')
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
#node_hardware.addDevice("ENG_ENCODER","")

#Add a node for HV measured array
node_result.addNode("HV_MEAS_ARR","numeric")
hv_meas_arr_str="_hv_meas=[201.*MAXVAL("
for i in range (1,9):
    #Add nodes for HV programmed values, 8 for 8 cathodes
    node_control.addNode("HV_PROG_"+str(i),"numeric")
    #Make the ACQ196AO's output nodes to refer the value from HV prog nodes.
    node_hardware.getNode("ACQ196AO.OUTPUT_0"+str(i)).putData(myTree.tdiCompile("Build_Signal([0.,1.,1.,0.]*"+node_control.getNode("HV_PROG_"+str(i)).getFullPath()+",*,[0.,1.,"+node_control.getNode("DIG_TSTOP").getFullPath()+"-"+node_hardware.getNode("DIO2.CHANNEL_1.TRIGGER_1").getFullPath()+"+1.0,"+node_control.getNode("DIG_TSTOP").getFullPath()+"-"+node_hardware.getNode("DIO2.CHANNEL_1.TRIGGER_1").getFullPath()+"+2.0])"))
    hv_meas_arr_str=hv_meas_arr_str+node_hardware.getNode("ACQ196.INPUT_0"+str(i)).getFullPath()+")"
    if i!=8:
        hv_meas_arr_str=hv_meas_arr_str+",201.*MAXVAL("
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

#Put dummy values for remaining ACQ196AO channels
for i in range (9,17):
    if i<10:
        node_hardware.getNode("ACQ196AO.OUTPUT_0"+str(i)).putData(myTree.tdiCompile(node_hardware.getNode("ACQ196AO.OUTPUT_01").getFullPath()))
    else:
        node_hardware.getNode("ACQ196AO.OUTPUT_"+str(i)).putData(myTree.tdiCompile(node_hardware.getNode("ACQ196AO.OUTPUT_01").getFullPath()))

#Add a filter array, and nodes under it: VALUE and COMMENT
node_control.addNode("FILTER","structure")
node_control.getNode("FILTER").addNode("COMMENT","text")
node_control.getNode("FILTER").addNode("VALUE","text")
node_control.getNode("FILTER.COMMENT").putData("values of filters: DA6563, HEI5876, HEI6670, HEII4686, OPEN")

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
    chan_num=i%30+1
    if chan_num>=16:
        chan_num+=2
    if chan_num<10:
        mean_sig_arr=mean_sig_arr+"MEAN("+node_hardware.getNode("ACQ132_"+str(i/30+1)+".INPUT_0"+str(chan_num)).getFullPath()+")"
    else:
        mean_sig_arr=mean_sig_arr+"MEAN("+node_hardware.getNode("ACQ132_"+str(i/30+1)+".INPUT_"+str(chan_num)).getFullPath()+")"
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
    chan_num=i%30+1
    if chan_num>=16:
        chan_num+=2
    if chan_num<10:
        sig_arr=sig_arr+node_hardware.getNode("ACQ132_"+str(i/30+1)+".INPUT_0"+str(chan_num)).getFullPath()
    else:
        sig_arr=sig_arr+node_hardware.getNode("ACQ132_"+str(i/30+1)+".INPUT_"+str(chan_num)).getFullPath()
    if (i+1)%10==0:
        sig_arr=sig_arr+"]"
    if i!=119:
        sig_arr=sig_arr+","
    else:
        sig_arr=sig_arr+"]"

node_result.getNode("SIG_ARR").putData(myTree.tdiCompile(sig_arr))

#Add a background array
node_calib.addNode("BACK_ARR","numeric")

#Add coefficient arrays
node_calib.addNode("COEF_0TH_ARR","numeric")
node_calib.addNode("COEF_1ST_ARR","numeric")
node_calib.addNode("COEF_2ND_ARR","numeric")
node_calib.addNode("COEF_3RD_ARR","numeric")
node_calib.addNode("COEF_4TH_ARR","numeric")

#Add a gain array. Values are an 10 by 12 array, and each component is 50 * exp(polynomial(HV_measured))
node_result.addNode("GAIN_ARR","numeric")
gain_arr="_vr=[409.5,412.8,403.5,392.5,391.1,390.3,421.8,426.2],_vr_arr=["
for i in range (1,9):
    if i%2==1:
        gain_arr=gain_arr+"replicate([_vr["+str(i-1)+"]],0,10),"
    else:
        gain_arr=gain_arr+"set_range(10,[replicate([_vr["+str(i-2)+"]],0,5),replicate([_vr["+str(i-1)+"]],0,5)]),replicate([_vr["+str(i-1)+"]],0,10)"
        if i!=8:
            gain_arr=gain_arr+","
        else:
            gain_arr=gain_arr+"]"

gain_arr=gain_arr+",_c0="+node_calib.getNode("COEF_0TH_ARR").getFullPath()+",_c1="+node_calib.getNode("COEF_1ST_ARR").getFullPath()+",_c2="+node_calib.getNode("COEF_2ND_ARR").getFullPath()+",_c3="+node_calib.getNode("COEF_3RD_ARR").getFullPath()+",_c4="+node_calib.getNode("COEF_4TH_ARR").getFullPath()+",_hv_meas_arr="+node_result.getNode("HV_MEAS_ARR").getFullPath()+",_gain_arr=67.49*exp(_c0+_c1*_hv_meas_arr+_c2*_hv_meas_arr^2+_c3*_hv_meas_arr^3+_c4*_hv_meas_arr^4)/exp(_c0+_c1*_vr_arr+_c2*_vr_arr^2+_c3*_vr_arr^3+_c4*_vr_arr^4)"
node_result.getNode("GAIN_ARR").putData(myTree.tdiCompile(gain_arr))

#Add a brightness array
node_result.addNode("BRT_ARR","signal")
brt_arr="_gain="+node_result.getNode("GAIN_ARR").getFullPath()+",_back="+node_calib.getNode("BACK_ARR").getFullPath()+",_sig_series="+node_result.getNode("SIG_ARR").getFullPath()+","
filter_list=['DA6563','HEI5876','HEI6670','HEII4686','OPEN']
for i in range (0,5):
    brt_arr=brt_arr+"IF(UPCASE("+node_control.getNode("FILTER.VALUE").getFullPath()+")=='"+filter_list[i]+"',_slambda="+node_calib.getNode("S_L_"+filter_list[i]).getFullPath()+"),"

brt_arr=brt_arr+"_back_series=spread([_back],0,size(_sig_series,0)),_sensitivity_series=spread([_slambda/_gain],0,size(_sig_series,0)),_brt_series=(-_sig_series+_back_series)*_sensitivity_series"
node_result.getNode("BRT_ARR").putData(myTree.tdiCompile(brt_arr))

#Add HV_CHECK structure node
node_calib.addNode("HV_CHECK","structure")
node_calib.addNode("HV_CHECK.GAINCOEF_0TH","numeric")
node_calib.addNode("HV_CHECK.GAINCOEF_1ST","numeric")
node_calib.addNode("HV_CHECK.GAINCOEF_2ND","numeric")
node_calib.addNode("HV_CHECK.GAINCOEF_3RD","numeric")
node_calib.addNode("HV_CHECK.GAINCOEF_4TH","numeric")
node_calib.addNode("HV_CHECK.HVCOEF_0TH","numeric")
node_calib.addNode("HV_CHECK.HVCOEF_1ST","numeric")
node_calib.addNode("HV_CHECK.GAIN_GOAL","numeric")
node_calib.addNode("HV_CHECK.HVMEAS_REQ","numeric")
node_calib.addNode("HV_CHECK.HVPROG_REQ","numeric")

hvmeas_req="_vr=[409.5,412.8,403.5,392.5,391.1,390.3,421.8,426.2],_vr_arr=["
for i in range (1,9):
    if i%2==1:
        hvmeas_req=hvmeas_req+"replicate([_vr["+str(i-1)+"]],0,10),"
    else:
        hvmeas_req=hvmeas_req+"set_range(10,[replicate([_vr["+str(i-2)+"]],0,5),replicate([_vr["+str(i-1)+"]],0,5)]),replicate([_vr["+str(i-1)+"]],0,10)"
        if i!=8:
            hvmeas_req=hvmeas_req+","
        else:
            hvmeas_req=hvmeas_req+"]"

hvmeas_req=hvmeas_req+",_c0="+node_calib.getNode("COEF_0TH_ARR").getFullPath()+",_c1="+node_calib.getNode("COEF_1ST_ARR").getFullPath()+",_c2="+node_calib.getNode("COEF_2ND_ARR").getFullPath()+",_c3="+node_calib.getNode("COEF_3RD_ARR").getFullPath()+",_c4="+node_calib.getNode("COEF_4TH_ARR").getFullPath()+",_gain_factor=exp(_c0+_c1*_vr_arr+_c2*_vr_arr^2+_c3*_vr_arr^3+_c4*_vr_arr^4)/67.49,_gain_goal="+node_calib.getNode("HV_CHECK.GAIN_GOAL").getFullPath()+",_gain_goal_arr=["
for i in range (1,9):
    if i%2==1:
        hvmeas_req=hvmeas_req+"replicate([_gain_goal["+str(i-1)+"]],0,10),"
    else:
        hvmeas_req=hvmeas_req+"set_range(10,[replicate([_gain_goal["+str(i-2)+"]],0,5),replicate([_gain_goal["+str(i-1)+"]],0,5)]),replicate([_gain_goal["+str(i-1)+"]],0,10)"
        if i!=8:
            hvmeas_req=hvmeas_req+","
        else:
            hvmeas_req=hvmeas_req+"]"

hvmeas_req=hvmeas_req+",_c0g="+node_calib.getNode("HV_CHECK.GAINCOEF_0TH").getFullPath()+",_c1g="+node_calib.getNode("HV_CHECK.GAINCOEF_1ST").getFullPath()+",_c2g="+node_calib.getNode("HV_CHECK.GAINCOEF_2ND").getFullPath()+",_c3g="+node_calib.getNode("HV_CHECK.GAINCOEF_3RD").getFullPath()+",_c4g="+node_calib.getNode("HV_CHECK.GAINCOEF_4TH").getFullPath()+",_hvmeas_req=_c0g+_c1g*log(_gain_goal_arr*_gain_factor)+_c2g*log(_gain_goal_arr*_gain_factor)^2+_c3g*log(_gain_goal_arr*_gain_factor)^3+_c4g*log(_gain_goal_arr*_gain_factor)^4"
hvprog_req="_c0h="+node_calib.getNode("HV_CHECK.HVCOEF_0TH").getFullPath()+",_c1h="+node_calib.getNode("HV_CHECK.HVCOEF_1ST").getFullPath()+",_hvmeas_req="+node_calib.getNode("HV_CHECK.HVMEAS_REQ").getFullPath()+",_hvprog_req=_c0h+_c1h*_hvmeas_req"
node_calib.getNode("HV_CHECK.HVMEAS_REQ").putData(myTree.tdiCompile(hvmeas_req))
node_calib.getNode("HV_CHECK.HVPROG_REQ").putData(myTree.tdiCompile(hvprog_req))

node_hardware.getNode("ACQ196.ACTIVE_CHAN").putData(96)
node_hardware.getNode("ACQ196.CLOCK_FREQ").putData(1000)
node_hardware.getNode("ACQ196.CLOCK_DIV").putData(1)
node_hardware.getNode("ACQ196.CLOCK_EDGE").putData("rising")
node_hardware.getNode("ACQ196.CLOCK_OUT").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY:HARDWARE:ACQ196:DI2"))
node_hardware.getNode("ACQ196.CLOCK_SRC").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY:HARDWARE:ACQ196:INT_CLOCK"))
node_hardware.getNode("ACQ196.COMMENT").putData("GPI 196 note no a-to-d's, only analogue out (ao)")
node_hardware.getNode("ACQ196.DI3").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY.HARDWARE:DIO2.CHANNEL_1:TRIGGER_1"))
node_hardware.getNode("ACQ196.DI3.BUS").putData("fpga")
node_hardware.getNode("ACQ196.DI3.WIRE").putData("lemo")
node_hardware.getNode("ACQ196.NODE").putData("192.168.0.194")
node_hardware.getNode("ACQ196.POST_TRIG").putData(myTree.tdiCompile("INT(("+gpi_root+".APD_ARRAY.CONTROL:DIG_TSTOP - "+gpi_root+".APD_ARRAY.HARDWARE:DIO2.CHANNEL_1:TRIGGER_1 + 3.) * "+gpi_root+".APD_ARRAY.HARDWARE:ACQ196:CLOCK_FREQ / 1024)"))
node_hardware.getNode("ACQ196.PRE_TRIG").putData(0)
node_hardware.getNode("ACQ196.TRIG_EDGE").putData("RISING")
node_hardware.getNode("ACQ196.TRIG_SRC").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY:HARDWARE:ACQ196:DI3"))

node_hardware.getNode("ACQ196AO.AO_CLOCK").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY.HARDWARE:ACQ196AO:DI2"))
node_hardware.getNode("ACQ196AO.AO_TRIG").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY.HARDWARE:ACQ196AO:DI3"))
node_hardware.getNode("ACQ196AO.CYCLE_TYPE").putData("ONCE")
node_hardware.getNode("ACQ196AO.FAWG_DIV").putData(20)
node_hardware.getNode("ACQ196AO.DI2").putData(myTree.tdiCompile("* : * : 1 / 1000."))
node_hardware.getNode("ACQ196AO.DI3").putData(0.)
node_hardware.getNode("ACQ196AO.MAX_SAMPLES").putData(16384)
node_hardware.getNode("ACQ196AO.NODE").putData("192.168.0.194")
node_hardware.getNode("ACQ196AO.TRIG_TYPE").putData("HARD_TRIG")

node_hardware.getNode("DIO2.CLOCK_SOURCE").putData("INTERNAL")
node_hardware.getNode("DIO2.COMMENT").putData("triggers and clocks for APD systems")
node_hardware.getNode("DIO2.SW_MODE").putData("REMOTE")
node_hardware.getNode("DIO2.SYNCH").putData("NO")
node_hardware.getNode("DIO2.IP_ADDR").putData("192.168.0.194:8106")
node_hardware.getNode("DIO2.CHANNEL_1.COMMENT").putData("trigger for ACQ196")
node_hardware.getNode("DIO2.CHANNEL_1.CYCLIC").putData("NO")
node_hardware.getNode("DIO2.CHANNEL_1.DELAY").putData(1.)
node_hardware.getNode("DIO2.CHANNEL_1.DURATION").putData(0.01)
node_hardware.getNode("DIO2.CHANNEL_1.EVENT").putData(myTree.tdiCompile("['START             ','SPECTROSCOPY_START']"))
node_hardware.getNode("DIO2.CHANNEL_1.FREQUENCY_1").putData(1000)
node_hardware.getNode("DIO2.CHANNEL_1.FREQUENCY_2").putData(1000)
node_hardware.getNode("DIO2.CHANNEL_1.FUNCTION").putData("PULSE")
node_hardware.getNode("DIO2.CHANNEL_1.INIT_LEVEL_1").putData("LOW")
node_hardware.getNode("DIO2.CHANNEL_1.INIT_LEVEL_2").putData("HIGH")
node_hardware.getNode("DIO2.CHANNEL_1.TRIGGER").putData(myTree.tdiCompile("\SPECTROSCOPY::TSTART")) # THIS NEEDS TO BE SPECIFIED
node_hardware.getNode("DIO2.CHANNEL_1.TRIGGER_1").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY.HARDWARE:DIO2.CHANNEL_1:TRIGGER + "+gpi_root+".APD_ARRAY.HARDWARE:DIO2.CHANNEL_1:DELAY"))
node_hardware.getNode("DIO2.CHANNEL_1.TRIGGER_2").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY.HARDWARE:DIO2.CHANNEL_1:TRIGGER_1 + "+gpi_root+".APD_ARRAY.HARDWARE:DIO2.CHANNEL_1:DURATION"))
node_hardware.getNode("DIO2.CHANNEL_1.TRIG_MODE").putData("SOFTWARE")
node_hardware.getNode("DIO2.CHANNEL_2.COMMENT").putData("trigger for ACQ132")
node_hardware.getNode("DIO2.CHANNEL_2.CYCLIC").putData("NO")
node_hardware.getNode("DIO2.CHANNEL_2.DELAY").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY.CONTROL:DIG_TSTART - "+gpi_root+".APD_ARRAY.HARDWARE:DIO2.CHANNEL_2:TRIGGER"))
node_hardware.getNode("DIO2.CHANNEL_2.DURATION").putData(0.01)
node_hardware.getNode("DIO2.CHANNEL_2.EVENT").putData(myTree.tdiCompile("['START             ','SPECTROSCOPY_START']"))
node_hardware.getNode("DIO2.CHANNEL_2.FREQUENCY_1").putData(1000)
node_hardware.getNode("DIO2.CHANNEL_2.FREQUENCY_2").putData(1000)
node_hardware.getNode("DIO2.CHANNEL_2.FUNCTION").putData("PULSE")
node_hardware.getNode("DIO2.CHANNEL_2.INIT_LEVEL_1").putData("LOW")
node_hardware.getNode("DIO2.CHANNEL_2.INIT_LEVEL_2").putData("HIGH")
node_hardware.getNode("DIO2.CHANNEL_2.TRIGGER").putData(myTree.tdiCompile("\SPECTROSCOPY::TSTART")) # THIS NEEDS TO BE SPECIFIED
node_hardware.getNode("DIO2.CHANNEL_2.TRIGGER_1").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY.HARDWARE:DIO2.CHANNEL_2:TRIGGER + "+gpi_root+".APD_ARRAY.HARDWARE:DIO2.CHANNEL_2:DELAY"))
node_hardware.getNode("DIO2.CHANNEL_2.TRIGGER_2").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY.HARDWARE:DIO2.CHANNEL_2:TRIGGER + "+gpi_root+".APD_ARRAY.HARDWARE:DIO2.CHANNEL_2:DELAY + "+gpi_root+".APD_ARRAY.HARDWARE:DIO2.CHANNEL_2:DURATION"))
node_hardware.getNode("DIO2.CHANNEL_2.TRIG_MODE").putData("SOFTWARE")
node_hardware.getNode("DIO2.CHANNEL_3.CLOCK").putData(myTree.tdiCompile("* : * : 500E-9"))
node_hardware.getNode("DIO2.CHANNEL_3.COMMENT").putData("clock for outerwall APD system")
node_hardware.getNode("DIO2.CHANNEL_3.CYCLIC").putData("NO")
node_hardware.getNode("DIO2.CHANNEL_3.FREQUENCY_1").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY.CONTROL:DIG_FREQ * 1000E3"))
node_hardware.getNode("DIO2.CHANNEL_3.FREQUENCY_2").putData(1000)
node_hardware.getNode("DIO2.CHANNEL_3.FUNCTION").putData("CLOCK")
node_hardware.getNode("DIO2.CHANNEL_3.INIT_LEVEL_1").putData("LOW")
node_hardware.getNode("DIO2.CHANNEL_3.INIT_LEVEL_2").putData("LOW")
node_hardware.getNode("DIO2.CHANNEL_3.TRIGGER").putData(0)
node_hardware.getNode("DIO2.CHANNEL_3.TRIGGER_1").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY.HARDWARE:DIO2.CHANNEL_3:TRIGGER + "+gpi_root+".APD_ARRAY.HARDWARE:DIO2.CHANNEL_3:DELAY"))
node_hardware.getNode("DIO2.CHANNEL_3.TRIGGER_2").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY.HARDWARE:DIO2.CHANNEL_3:TRIGGER_1 + "+gpi_root+".APD_ARRAY.HARDWARE:DIO2.CHANNEL_3:DURATION"))

node_hardware.getNode("ACQ132_1.ACTIVE_CHAN").putData(32)
node_hardware.getNode("ACQ132_1.CLOCK_EDGE").putData("rising")
node_hardware.getNode("ACQ132_1.CLOCK_FREQ").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY.HARDWARE:DIO2.CHANNEL_3:FREQUENCY_1"))
node_hardware.getNode("ACQ132_1.CLOCK_SRC").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY.HARDWARE:DT132_1:DI0"))
node_hardware.getNode("ACQ132_1.COMMENT").putData("Dtaq 32-channel 2 MSPS digitizer")
node_hardware.getNode("ACQ132_1.DI0").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY.HARDWARE:DIO2.CHANNEL_3:CLOCK"))
node_hardware.getNode("ACQ132_1.DI0.BUS").putData("fpga pxi")
node_hardware.getNode("ACQ132_1.DI0.WIRE").putData("lemo")
node_hardware.getNode("ACQ132_1.DI1").putData(myTree.tdiCompile("* : * : 1D0 / "+gpi_root+".APD_ARRAY.HARDWARE:ACQ132_1:CLOCK_FREQ"))
node_hardware.getNode("ACQ132_1.DI1.BUS").putData("pxi")
node_hardware.getNode("ACQ132_1.DI1.WIRE").putData("fpga")
node_hardware.getNode("ACQ132_1.DI3").putData(myTree.tdiCompile("D_FLOAT("+gpi_root+".APD_ARRAY.HARDWARE:DIO2.CHANNEL_2:TRIGGER_2)"))
node_hardware.getNode("ACQ132_1.DI3.BUS").putData("fpga pxi")
node_hardware.getNode("ACQ132_1.DI3.WIRE").putData("lemo")
node_hardware.getNode("ACQ132_1.NODE").putData("192.168.0.4")
node_hardware.getNode("ACQ132_1.POST_TRIG").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY.CONTROL:DIG_SAMPS"))
node_hardware.getNode("ACQ132_1.TRIG_SRC").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY.HARDWARE:ACQ132_1:DI3"))

for i in range (2,5):
    node_hardware.getNode("ACQ132_"+str(i)+".ACTIVE_CHAN").putData(32)
    node_hardware.getNode("ACQ132_"+str(i)+".CLOCK_EDGE").putData("rising")
    node_hardware.getNode("ACQ132_"+str(i)+".CLOCK_FREQ").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY.HARDWARE:ACQ132_1:CLOCK_FREQ"))
    node_hardware.getNode("ACQ132_"+str(i)+".CLOCK_SRC").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY.HARDWARE:DT132_"+str(i)+":DI0"))
    node_hardware.getNode("ACQ132_"+str(i)+".COMMENT").putData("Dtaq 32-channel 2 MSPS digitizer")
    node_hardware.getNode("ACQ132_"+str(i)+".DI0").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY.HARDWARE:ACQ132_1:DI0"))
    node_hardware.getNode("ACQ132_"+str(i)+".DI0.BUS").putData("fpga")
    node_hardware.getNode("ACQ132_"+str(i)+".DI0.WIRE").putData("pxi")
    node_hardware.getNode("ACQ132_"+str(i)+".DI3").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY.HARDWARE:ACQ132_1:DI3"))
    node_hardware.getNode("ACQ132_"+str(i)+".DI3.BUS").putData("fpga")
    node_hardware.getNode("ACQ132_"+str(i)+".DI3.WIRE").putData("pxi")
    node_hardware.getNode("ACQ132_"+str(i)+".NODE").putData("192.168.0.4"+str(i-2))
    node_hardware.getNode("ACQ132_"+str(i)+".POST_TRIG").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY.CONTROL:DIG_SAMPS"))
    node_hardware.getNode("ACQ132_"+str(i)+".TRIG_SRC").putData(myTree.tdiCompile(gpi_root+".APD_ARRAY.HARDWARE:ACQ132_"+str(i)+":DI3"))


myTree.write() #save the edited tree
myTree.close() #close the tree
