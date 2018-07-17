import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('AM-97452.png')

boundaries=[([0, 0, 50], [50, 56, 200])]
for (lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
    # find the colors within the specified boundaries and apply the mask
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)

coord = np.argwhere(output>100)

x=np.array([])
y=np.array([])
for i in range(0,len(coord)):
    x=np.append(x,coord[i][1])
    y=np.append(y,1600-coord[i][0])

sort_ind=np.argsort(x)
x_sorted=np.sort(x)
y_sorted=np.array([])
for i in range(0,len(sort_ind)):
    y_sorted=np.append(y_sorted,y[sort_ind[i]])

upper_bound=np.max(np.argwhere(x_sorted<=1700))
x_sorted=x_sorted[1:upper_bound]
y_sorted=y_sorted[1:upper_bound]
y_sorted=y_sorted-np.min(y_sorted)
y_sorted=y_sorted/np.max(y_sorted)*64.07/100.

def lin_interp(x, y, i, half):
    return x[i] + (x[i+1] - x[i]) * ((half - y[i]) / (y[i+1] - y[i]))

def half_max_x(x, y):
    half = max(y)/2.0
    signs = np.sign(np.add(y, -half))
    zero_crossings = (signs[0:-2] != signs[1:-1])
    zero_crossings_i = np.where(zero_crossings)[0]
    return [lin_interp(x, y, zero_crossings_i[0], half),
            lin_interp(x, y, zero_crossings_i[1], half)]

hmx = half_max_x(x_sorted,y_sorted)
x_sorted=(x_sorted-hmx[0])/(hmx[1]-hmx[0])*(661.764-652.160)+652.160

area=np.trapz(y_sorted,x_sorted)
print('Area under the curve = '+str(area))

file=open("transfer_function_da_6563_new.txt","w")
for i in range(0,len(x_sorted)):
    file.write(str(x_sorted[i])+" "+str(y_sorted[i])+"\n")

file.close()

plt.plot(x_sorted,y_sorted)
plt.xlabel('Wavelength (nm)')
plt.ylabel('Transmission')
plt.show()
