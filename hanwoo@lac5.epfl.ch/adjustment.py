from MDSplus import *

#s=1180702500 #recent 'new fiber' shots
s=1180705500 #copied old 'new fiber' shots

for j in range(1,41):
    myTree=Tree("spectroscopy",s+j)
    node_result=myTree.getNode('gpi_tcv.apd_array.result')
    node_control=myTree.getNode('gpi_tcv.apd_array.control')
    node_calib=myTree.getNode('gpi_tcv.apd_array.calibration')
    node_hardware=myTree.getNode('gpi_tcv.apd_array.hardware')
    node_hvcheck=node_calib.getNode("HV_CHECK")
    
    #Add a gain array. Values are an 10 by 12 array, and each component is 100 * exp(polynomial(HV_measured))
    gain_arr="_c0="+node_calib.getNode("COEF_0TH_ARR").getFullPath()+",_c1="+node_calib.getNode("COEF_1ST_ARR").getFullPath()+",_c2="+node_calib.getNode("COEF_2ND_ARR").getFullPath()+",_c3="+node_calib.getNode("COEF_3RD_ARR").getFullPath()+",_c4="+node_calib.getNode("COEF_4TH_ARR").getFullPath()+",_hv_meas_arr="+node_result.getNode("HV_MEAS_ARR").getFullPath()+",_gain_arr=100.0*exp(_c0+_c1*_hv_meas_arr+_c2*_hv_meas_arr^2+_c3*_hv_meas_arr^3+_c4*_hv_meas_arr^4)"
    node_result.getNode("GAIN_ARR").putData(myTree.tdiCompile(gain_arr))
    
    hvmeas_req="_c0="+node_calib.getNode("COEF_0TH_ARR").getFullPath()+",_c1="+node_calib.getNode("COEF_1ST_ARR").getFullPath()+",_c2="+node_calib.getNode("COEF_2ND_ARR").getFullPath()+",_c3="+node_calib.getNode("COEF_3RD_ARR").getFullPath()+",_c4="+node_calib.getNode("COEF_4TH_ARR").getFullPath()+",_gain_goal="+node_hvcheck.getNode("GAIN_GOAL").getFullPath()+",_gain_goal_arr=["
    for i in range (1,9):
        if i%2==1:
            hvmeas_req=hvmeas_req+"replicate([_gain_goal["+str(i-1)+"]],0,10),"
        else:
            hvmeas_req=hvmeas_req+"set_range(10,[replicate([_gain_goal["+str(i-2)+"]],0,5),replicate([_gain_goal["+str(i-1)+"]],0,5)]),replicate([_gain_goal["+str(i-1)+"]],0,10)"
            if i!=8:
                hvmeas_req=hvmeas_req+","
            else:
                hvmeas_req=hvmeas_req+"]"
    
    hvmeas_req=hvmeas_req+",_c0g="+node_hvcheck.getNode("GAINCOEF_0TH").getFullPath()+",_c1g="+node_hvcheck.getNode("GAINCOEF_1ST").getFullPath()+",_c2g="+node_hvcheck.getNode("GAINCOEF_2ND").getFullPath()+",_c3g="+node_hvcheck.getNode("GAINCOEF_3RD").getFullPath()+",_c4g="+node_hvcheck.getNode("GAINCOEF_4TH").getFullPath()+",_hvmeas_req=_c0g+_c1g*log(_gain_goal_arr/100.0)+_c2g*log(_gain_goal_arr/100.0)^2+_c3g*log(_gain_goal_arr/100.0)^3+_c4g*log(_gain_goal_arr/100.0)^4"
    hvprog_req="_c0h="+node_hvcheck.getNode("HVCOEF_0TH").getFullPath()+",_c1h="+node_hvcheck.getNode("HVCOEF_1ST").getFullPath()+",_hvmeas_req="+node_hvcheck.getNode("HVMEAS_REQ").getFullPath()+",_hvprog_req=_c0h+_c1h*_hvmeas_req"
    node_hvcheck.getNode("HVMEAS_REQ").putData(myTree.tdiCompile(hvmeas_req))
    node_hvcheck.getNode("HVPROG_REQ").putData(myTree.tdiCompile(hvprog_req))

    myTree.close() #close the tree


