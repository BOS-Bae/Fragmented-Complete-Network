import numpy as np
import matplotlib.pyplot as plt
import sys
 
tot_dat = np.loadtxt("./REF_dist.dat", dtype=str)
tot_dat_r = np.transpose(tot_dat)
c_dist = tot_dat_r[1]
c_dist[:] = c_dist[:].astype(int)

x_data = []
c_data = []
idx = 0
cumul_dist = np.zeros(len(c_dist))

count1 = 0
count2 = 0
ln_x_sum1 = 0
ln_x_sum2 = 0

for i in range(len(c_dist)):
    cumul_dist[i] = sum(list(c_dist[i:]))

np.savetxt("REF_dist.dat", c_dist)
np.savetxt("REF_cumul_dist.dat", cumul_dist)
