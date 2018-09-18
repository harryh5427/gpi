"""

"""
import numpy as np
import sys
import matplotlib.pyplot as plt

s=int(sys.argv[1])
f=np.load("sample_skip_test_"+str(int(s/100))+"01.npz")
plt.xlabel('Time (sec)')
plt.ylabel('n_skip')
plt.ylim(-0.5,1.5)
plt.plot(f['arr_1'][s%100-1],f['arr_0'][s%100-1],".-")
plt.show()

