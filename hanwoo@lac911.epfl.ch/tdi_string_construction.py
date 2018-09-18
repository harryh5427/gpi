from MDSplus import *

s=1180413600

myTree=Tree('spectroscopy',s)
gpi_root="\SPECTROSCOPY::TOP.GPI_TCV"
gpi_node=myTree.getNode(gpi_root)
node_apd_array=gpi_node.getNode("APD_ARRAY")
node_calib=node_apd_array.getNode("CALIBRATION")

gain_arr="_c0=node_calib.getNode('COEF_0TH_ARR').getFullPath(), "


_c0=path_to_c0,
_c1=path_to_c1...,

_hv1=mean(path_to_input),
_row_size=10,
_col_size=12,
#Code this part up so it's nice, _hv=[10x12]
_hv=[replicate([_hv1],0,row_size)],set_range(_row_size,[replicate([_hv1],0,_row_size/2),replicate([_hv2],0,_row_size/2)])

_gain_output=50*exp(_c0+_c1*_v_arr+...)




50.0*exp(_c0+_c1*_hv+_c2*_hv**2)

gain_arr+="["
#for i in range (0,120):
for i in range(0,1):
    if (i+1)%10==1:
        gain_arr=gain_arr+"["
    gain_arr=gain_arr+"50.*exp((_c0["+str(i%10)+","+str(i/10)+"])+("+node_calib.getNode("COEF_1ST_ARR").getFullPath()+"["+str(i%10)+","+str(i/10)+"])*("+node_calib.getNode("HV_MEAS_1").getFullPath()+")+("+node_calib.getNode("COEF_2ND_ARR").getFullPath()+"["+str(i%10)+","+str(i/10)+"])*("+node_calib.getNode("HV_MEAS_1").getFullPath()+")^2+("+node_calib.getNode("COEF_3RD_ARR").getFullPath()+"["+str(i%10)+","+str(i/10)+"])*("+node_calib.getNode("HV_MEAS_1").getFullPath()+")^3+("+node_calib.getNode("COEF_4TH_ARR").getFullPath()+"["+str(i%10)+","+str(i/10)+"])*("+node_calib.getNode("HV_MEAS_1").getFullPath()+")^4)/(exp(("+node_calib.getNode("COEF_0TH_ARR").getFullPath()+"["+str(i%10)+","+str(i/10)+"])+("+node_calib.getNode("COEF_1ST_ARR").getFullPath()+"["+str(i%10)+","+str(i/10)+"])*(400.)+("+node_calib.getNode("COEF_2ND_ARR").getFullPath()+"["+str(i%10)+","+str(i/10)+"])*(400.)^2+("+node_calib.getNode("COEF_3RD_ARR").getFullPath()+"["+str(i%10)+","+str(i/10)+"])*(400.)^3+("+node_calib.getNode("COEF_4TH_ARR").getFullPath()+"["+str(i%10)+","+str(i/10)+"])*(400.)^4))"
    if (i+1)%10==0:
        gain_arrr=gain_arr+"]"
    if i!=119:
        gain_arr=gain_arr+","
    else:
        gain_arr=gain_arr+"]"
    print("i="+str(i)+", len(gain_arr)="+str(len(gain_arr))+", len(temp)="+len(temp))
