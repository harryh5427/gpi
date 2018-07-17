pro read_old_da_filter

restore,file='Da_filter_func_7206.dat',/verb
area=int_tabulated(xdata,ydata/max(ydata)*0.6407)

openw,lun2,"transfer_function_da_6563_old.txt",/get_lun
for i=0,n_elements(xdata)-1 do begin
   printf,lun2,strtrim(xdata[i],2)+" "+strtrim(ydata[i]/max(ydata)*0.6407,2)
endfor
close,lun2
free_lun,lun2

end
