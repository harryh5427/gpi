pro read_hei_filter

restore,file='HeI_filter_func_7209.dat',/verb
ydata=ydata-min(ydata)
area=int_tabulated(xdata,ydata/max(ydata)*76./100.)

openw,lun2,"transfer_function_hei_5876.txt",/get_lun
for i=0,n_elements(xdata)-1 do begin
   printf,lun2,strtrim(xdata[i],2)+" "+strtrim(ydata[i]/max(ydata)*0.76,2)
endfor
close,lun2
free_lun,lun2

end
