import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import sys

#print("python3 C_k_Japan.py t")
#print("t : 22 ~ 49")
#
#t = int(sys.argv[1])
#t_idx = t - 22

file_path = './Japan-seats-saved.xlsx'
df = pd.read_excel(file_path ,header=None)
data = df.to_numpy()
c_dat = data.astype(int)
c_dist_total = c_dat[:,1:]

def size_distribution(c_size, M_max):
    dist_arr = np.zeros(int(M_max))
    idx = 0
    for s_val in range(1,int(M_max + 1)):
        for s in c_size:
            if s_val == s: dist_arr[idx] += 1
        idx += 1
    return dist_arr

total_mat = []
size_arr = np.arange(1, np.max(c_dist_total)+1, 1)
for c_idx in range(len(c_dist_total)):
	c_dist_hist = size_distribution(c_dist_total[c_idx], np.max(c_dist_total))
	#print(c_dist_total[c_idx])
	val = size_arr*c_dist_hist
	c_dist_hist /= np.sum(val)
	total_mat.append(c_dist_hist)

c_dist_avg = np.average(total_mat, 0)

cumul_dist = np.zeros(len(c_dist_avg))
for i in range(len(c_dist_avg)):
    cumul_dist[i] = sum(list(c_dist_avg[i:]))
plt.figure(figsize=(9.5,3.5))
print(c_dist_avg)
plt.plot(range(1, np.max(c_dist_total)+1), cumul_dist, marker='o', color="black")
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.xlabel('k', fontsize=20)
plt.xscale('log')
plt.yscale('log')
plt.show()
