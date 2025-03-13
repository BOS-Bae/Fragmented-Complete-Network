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

total_list = []
 
total_count = check = 0
for i in range(len(c_dist_total)):
	for j in range(len(c_dist_total[0])):
		total_list.append(c_dist_total[i,j])

		total_count += 1
#		if (c_dist_total[i,j] == 1): check += 1
#print(check)
def size_distribution(c_size, M_max):
    dist_arr = np.zeros(int(M_max))
    idx = 0
    for s_val in range(1,int(M_max + 1)):
        for s in c_size:
            if s_val == s: dist_arr[idx] += 1
        idx += 1
    return dist_arr

c_dist_hist = size_distribution(total_list, np.max(total_list))
c_dist_hist /= np.sum(np.arange(1,np.max(total_list)+1,1)*c_dist_hist)
cumul_dist = np.zeros(len(c_dist_hist))

for i in range(len(c_dist_hist)):
    cumul_dist[i] = sum(list(c_dist_hist[i:]))
plt.figure(figsize=(9.5,3.5))
print(c_dist_hist)
plt.plot(range(1, np.max(c_dist_total)+1), cumul_dist, marker='o', color="black")
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.xlabel('k', fontsize=20)
plt.xscale('log')
plt.yscale('log')
plt.show()
