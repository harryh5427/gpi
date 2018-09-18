from MDSplus import *
import numpy as np
import sys
import time
import matplotlib.pyplot as plt

#start_shot=1180427501 #Shots with pxi connection and pulse
#start_shot=1180430500 #Shots with lemo connection and pulse
#start_shot=1180430601 #Shots with lemo connection and square wave
#start_shot=1180501501 #Shots with pxi trigger connection and square wave and lemo clock connection
#start_shot=1180501601
#start_shot=1180503601 #Shots with pxi connection for clock and trigger, with square wave source
start_shot=int(sys.argv[1])
shots_not_aligned=[]
largest_skip=[]

f=open("sample_skip_test_"+str(start_shot)+".txt","w+")
#print("Shot#    first_mismatch_nskip    last_mismatch_nskip    first_mismatch_cycle    last_mismatch_cycle    first_mismatch_time    last_mismatch_time")
#f.write("Shot#    first_mismatch_nskip    last_mismatch_nskip    first_mismatch_cycle    last_mismatch_cycle    first_mismatch_time    last_mismatch_time\n")
first_mismatch_nskip=[]
last_mismatch_nskip=[]
first_mismatch_cycle=[]
last_mismatch_cycle=[]
first_mismatch_time=[]
last_mismatch_time=[]
match_at_edges_save=[]
edge_times_save=[]
nskip1_100=0
nskip1_gt_nskip0=0
nskip0_gt_nskip1=0
ahead12_100=0
for i in range(0,100):
    down_edge_inds=[[],[],[],[]]
    up_edge_inds=[[],[],[],[]]
    s=start_shot+i
    myTree=Tree("spectroscopy",s)
    match_at_edges=[]
    edge_times=[]
    ahead12=0
    for n in range(1,4+1):
        if n<4:
            node_sig=myTree.getNode("GPI.APD_ARRAY.HARDWARE:DT132_"+str(n)+".INPUT_01")
        else:
            node_sig=myTree.getNode("GPI.INNER_APD.HARDWARE:ACQ132_"+str(n)+".INPUT_01")

        sig=np.array(node_sig.getData().data())
        t=np.array(node_sig.getData().getDimensionAt(0).data())
#        downs_inds=np.where(sig<0.95)[0]
#        ups_inds=np.where(sig>0.05)[0]
        downs_inds=np.where(sig<1.)[0]
        ups_inds=np.where(sig>4.)[0]
        if downs_inds[0]!=0:
            down_edge_inds[n-1].append(downs_inds[0])
        elif ups_inds[0]!=0:
            up_edge_inds[n-1].append(ups_inds[0])
        for j in range(1,len(downs_inds)-1):
            if downs_inds[j+1]-downs_inds[j]>1:
                down_edge_inds[n-1].append(downs_inds[j])
                down_edge_inds[n-1].append(downs_inds[j+1])
        for j in range(1,len(ups_inds)-1):
            if ups_inds[j+1]-ups_inds[j]>1:
                up_edge_inds[n-1].append(ups_inds[j])
                up_edge_inds[n-1].append(ups_inds[j+1])
    edge_inds_1=np.array(sorted(up_edge_inds[0]+down_edge_inds[0]))
    edge_inds_2=np.array(sorted(up_edge_inds[1]+down_edge_inds[1]))
    edge_inds_3=np.array(sorted(up_edge_inds[2]+down_edge_inds[2]))
    edge_inds_4=np.array(sorted(up_edge_inds[3]+down_edge_inds[3]))
    for j in range(1,len(edge_inds_1)):
        temp1=[edge_inds_1[j-1],edge_inds_2[j-1],edge_inds_3[j-1],edge_inds_4[j-1]]
        temp2=[edge_inds_1[j],edge_inds_2[j],edge_inds_3[j],edge_inds_4[j]]
        if np.mean([temp1[0],temp1[1]])<np.mean([temp1[2],temp1[3]]) and np.mean([temp2[0],temp2[1]])<np.mean([temp2[2],temp2[3]]):
            ahead12+=1
        if edge_inds_1[j]-edge_inds_1[j-1]<10:
            match_at_edges.append(min([max(np.diff(temp1)),max(np.diff(temp2))]))
            edge_times.append(t[edge_inds_1[j]])
    match_at_edges_save.append(match_at_edges)
    edge_times_save.append(edge_times)
    nskip1_percentage=100.*match_at_edges.count(1)/len(match_at_edges)
    nskip0_percentage=100.*match_at_edges.count(0)/len(match_at_edges)
    ahead12_percentage=100.*ahead12/2/len(match_at_edges)
    print("Shot "+str(s)+": "+str(round(nskip1_percentage,2))+"% of the edges have n_skip=1, "+str(round(nskip0_percentage,2))+"% of the edges have n_skip=0, ahead12_percentage="+str(ahead12_percentage))
    f.write("Shot "+str(s)+": "+str(round(nskip1_percentage,2))+"% of the edges have n_skip=1, "+str(round(nskip0_percentage,2))+"% of the edges have n_skip=0\n")
    if int(nskip1_percentage)==100:
        nskip1_100+=1
    if int(ahead12_percentage)==100:
        ahead12_100+=1
    elif nskip1_percentage>nskip0_percentage:
        nskip1_gt_nskip0+=1
    else:
        nskip0_gt_nskip1+=1
print("For "+str(nskip1_100)+"% shots, 1 sample is skipped at all edges.")
print("For "+str(nskip1_gt_nskip0)+"% shots, the number of n_skip=1 edges is greater than the number of n_skip=0 edges.")
print("For "+str(nskip0_gt_nskip1)+"% shots, the number of n_skip=0 edges is greater than the number of n_skip=1 edges.")
print("For "+str(ahead12_100)+"% shots, DT132_1 and 2 is 1 sample ahead of DT132_3 and 4 at all edges.")
f.write("For "+str(nskip1_100)+"% shots, 1 sample is skipped at all edges.\n")
f.write("For "+str(nskip1_gt_nskip0)+"% shots, the number of n_skip=1 edges is greater than the number of n_skip=0 edges.\n")
f.write("For "+str(nskip0_gt_nskip1)+"% shots, the number of n_skip=0 edges is greater than the number of n_skip=1 edges.\n")
np.savez('sample_skip_test_'+str(start_shot),match_at_edges_save,edge_times_save)
"""
    for k in range(0,len(up_leftedge_inds[0])):
        temp_up=[up_leftedge_inds[0][k],up_leftedge_inds[1][k],up_leftedge_inds[2][k],up_leftedge_inds[3][k]]
        if np.any(temp_up!=temp_up[0]):
            break
    if np.mean(temp_down)<np.mean(temp_up):
        temp=temp_down
    else:
        temp=temp_up
    first_mismatch_cycle.append(1+(j+k)/2)
    first_mismatch_nskip.append(max(np.diff(temp)))
    first_mismatch_time.append(t[temp[0]])

    for j in range(len(down_leftedge_inds[0])-1,-1,-1):
        temp_down=[down_leftedge_inds[0][j],down_leftedge_inds[1][j],down_leftedge_inds[2][j],down_leftedge_inds[3][j]]
        if np.any(temp_down!=temp_down[0]):
            break
    for k in range(len(up_leftedge_inds[0])-1,-1,-1):
        temp_up=[up_leftedge_inds[0][k],up_leftedge_inds[1][k],up_leftedge_inds[2][k],up_leftedge_inds[3][k]]
        if np.any(temp_up!=temp_up[0]):
            break
    if np.mean(temp_down)>np.mean(temp_up):
        temp=temp_down
    else:
        temp=temp_up
    last_mismatch_cycle.append(1+(j+k)/2)
    last_mismatch_nskip.append(max(np.diff(temp)))
    last_mismatch_time.append(t[temp[0]])

    print(str(s)+"    "+str(first_mismatch_nskip[i])+"    "+str(last_mismatch_nskip[i])+"    "+str(first_mismatch_cycle[i])+"    "+str(last_mismatch_cycle[i])+"    "+str(first_mismatch_time[i])+"    "+str(last_mismatch_time[i]))
    f.write(str(s)+"    "+str(first_mismatch_nskip[i])+"    "+str(last_mismatch_nskip[i])+"    "+str(first_mismatch_cycle[i])+"    "+str(last_mismatch_cycle[i])+"    "+str(first_mismatch_time[i])+"    "+str(last_mismatch_time[i])+"\n")
    myTree.close()

print(str(first_mismatch_nskip.count(1))+" % has first_mismatch_nskip=1")
print(str(first_mismatch_nskip.count(2))+" % has first_mismatch_nskip=2")
print(str(last_mismatch_nskip.count(1))+" % has last_mismatch_nskip=1")
print(str(last_mismatch_nskip.count(2))+" % has last_mismatch_nskip=2")
print(str(first_mismatch_cycle.count(1))+" % has first_mismatch_cycle=1")
f.write(str(first_mismatch_nskip.count(1))+" % has first_mismatch_nskip=1\n")
f.write(str(first_mismatch_nskip.count(2))+" % has first_mismatch_nskip=2\n")
f.write(str(last_mismatch_nskip.count(1))+" % has last_mismatch_nskip=1\n")
f.write(str(last_mismatch_nskip.count(2))+" % has last_mismatch_nskip=2\n")
f.write(str(first_mismatch_cycle.count(1))+" % has first_mismatch_cycle=1\n")
f.close()
"""
