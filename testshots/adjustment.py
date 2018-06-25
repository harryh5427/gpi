from MDSplus import *


s=1180622502
myTree=Tree("spectroscopy",s)

node_result=myTree.getNode('gpi_tcv.apd_array.result')
node_control=myTree.getNode('gpi_tcv.apd_array.control')
node_calib=myTree.getNode('gpi_tcv.apd_array.calibration')
node_hardware=myTree.getNode('gpi_tcv.apd_array.hardware')

#Add a node for HV measured array
hv_meas_arr_str="_hv_meas=[200.*MAXVAL("
for i in range (1,9):
    hv_meas_arr_str=hv_meas_arr_str+node_hardware.getNode("ACQ196.INPUT_0"+str(i)).getFullPath()+")"
    if i!=8:
        hv_meas_arr_str=hv_meas_arr_str+",200.*MAXVAL("
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

myTree.close() #close the tree
