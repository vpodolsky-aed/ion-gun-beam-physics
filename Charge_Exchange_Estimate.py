# Charge Exchange Estimate
###### Import Libraries ######
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

k_b=1.380649e-23; #J/k
T_g=300;#K
n_o=1e15; #m^-3
sigma_cex=8e-19 #m^-3
p_coef=np.array([10.0,5.0,1.0,0.5,0.1,0.05,0.01])
p_torr=1e-3*p_coef; #torr
p=101325/760*p_torr; #Pa
n_g=p/(k_b*T_g);#m^-3
# print("n_g=",n_g)
step=0.001
l=np.arange(0,0.1+step,step)
n_x=np.zeros((len(l),len(n_g)))

for i in range(len(l)):
    for j in range(len(n_g)):
        n_x[i][j]=math.exp(-sigma_cex*n_g[j]*l[i])

# Plot the lines
labels=[str(i) for i in p_coef]
lineObjects=plt.plot(l,n_x)
plt.legend(lineObjects,labels,title='Pressures [mTorr]:')
plt.xlabel("Distance From Source [m]")
plt.ylabel("Normalized Ion Density [$m^{-3}$]")
# plt.legend(title='Pressures [mTorr]:')

plt.xlim(0,max(l))
plt.ylim(0,1)
plt.show()