from MDSplus import *

modelTree=Tree("spectroscopy",-1)

s_old=1180626500
s=1180705500

for i in range (1,41):
    modelTree.createPulse(s+i)
    myTree=Tree("spectroscopy",s+i)
    myTree.getNode("gpi_tcv.APD_ARRAY.CONTROL.FILTER.VALUE").putData('DA6563')
    for j in range (1,5):
        for k in range (1,33):
            if k<10:
                a=Tree('spectroscopy',s_old+i).getNode('gpi_tcv.apd_array.hardware.acq132_'+str(j)+'.input_0'+str(k)).getData().data().tolist()
                myTree.getNode('gpi_tcv.apd_array.hardware.acq132_'+str(j)+'.input_0'+str(k)).putData(myTree.tdiCompile(str(a[0:2000])))
            else:
                a=Tree('spectroscopy',s_old+i).getNode('gpi_tcv.apd_array.hardware.acq132_'+str(j)+'.input_'+str(k)).getData().data().tolist()
                myTree.getNode('gpi_tcv.apd_array.hardware.acq132_'+str(j)+'.input_'+str(k)).putData(myTree.tdiCompile(str(a[0:2000])))
    for j in range (1,33):
        if j<10:
            a=Tree('spectroscopy',s_old+i).getNode('gpi_tcv.apd_array.hardware.acq196.input_0'+str(j)).getData().data().tolist()
            myTree.getNode('gpi_tcv.apd_array.hardware.acq196.input_0'+str(j)).putData(myTree.tdiCompile(str(max(a))))
        else:
            a=Tree('spectroscopy',s_old+i).getNode('gpi_tcv.apd_array.hardware.acq196.input_'+str(j)).getData().data().tolist()
            myTree.getNode('gpi_tcv.apd_array.hardware.acq196.input_'+str(j)).putData(myTree.tdiCompile(str(max(a))))
    for j in range (1,9):
        a=Tree('spectroscopy',s_old+i).getNode('gpi_tcv.apd_array.control.hv_prog_'+str(j)).getData().data()
        myTree.getNode('gpi_tcv.apd_array.control.hv_prog_'+str(j)).putData(myTree.tdiCompile(str(a)))
    myTree.close() #close the tree

modelTree.close() #close the tree
