from scipy.optimize import curve_fit
from scipy.optimize import minimize
from scipy.special import zeta
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import os.path
import sys

if (len(sys.argv) < 3):
    print("python3 cluster_size_diff.py N n_s")
    exit(1)

N = int(sys.argv[1])
n_s = int(sys.argv[2])

x_arr = range(1,int(M_max+1))
rule_num = 8

def seek_cluster(N, image):
    partition = np.zeros(N)
    partition[0] = 1
    group_idx = 2
    for i in range(N):
        if (partition[i] == 0):
            partition[i] = group_idx
            group_idx += 1
        for j in range(N):
            if (image[i,j] == 1 and partition[i] != 0): partition[j] = partition[i]
    return partition

def cluster_size_info(N,cluster_info):
    cluster_dist = np.zeros(int(max(cluster_info)))
    for i in range(1,int(max(cluster_info)+1)):
        for k in range(N):
            if (cluster_info[k] == i) : cluster_dist[i-1] += 1

    return cluster_dist

def size_distribution(c_size, M_max):
    dist_arr = np.zeros(int(M_max))
    idx = 0
    for s_val in range(1,int(M_max + 1)):
        for s in c_size:
            if s_val == s: dist_arr[idx] += 1
        idx += 1
    return dist_arr

#One click-version function. 
#Whole functions above are made by Minwoo Bae. :)
def get_cluster_size_distribution(N, image):
    cluster_info = seek_cluster(N, image)
    c_size = cluster_size_info(N, cluster_info)
    c_dist_n = size_distribution(c_size, M_max)
    return c_dist_n

c_dist_tot = []

n_samples = 0
not_completed_arr = []
for n in range(n_s):
    file = "./N{}_L{}_dat/N{}_L{}_image_s{}".format(N, rule_num, N, rule_num, n)
    if os.path.getsize(file) > 0: 
        image = np.loadtxt(file)
        n_samples += 1
        c_dist_n = get_cluster_size_distribution(N, image)
        c_dist_tot.append(c_dist_n)
    else :
        not_completed_arr.append(n)

#print(not_completed_arr)

c_dist = np.average(np.array(c_dist_tot),0)
c_dist_err = np.std(np.array(c_dist_tot),0)/np.sqrt(n_samples)

x_data = []
c_data = []
idx = 0
cumul_dist = np.zeros(len(c_dist))

plt.figure(figsize=(10,3.5))
plt.plot(x_arr, c_dist/N, label="L{}, numerical data".format(rule_num), marker = 'o', color='blue')
plt.errorbar(x_arr, c_dist/N, yerr= c_dist_err/N, fmt = 'o', color='blue')
plt.legend(fontsize=17)
plt.xscale('log')
plt.yscale('log')

plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.xlim(0.9, idx+10)
plt.ylim(10**(-6), 1.5)

plt.xlabel('cluster size', fontsize=20)

plt.show()
plt.clf()

plt.figure(figsize=(10,3.5))
plt.plot(x_arr, cumul_dist/N, label="L{}, numerical data, F(M <= X)".format(rule_num), marker = 'o', color='blue')
plt.errorbar(x_arr, cumul_dist/N, yerr= c_dist_err/N, color='blue')
plt.legend(fontsize=17)
plt.xscale('log')
plt.yscale('log')

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlim(0.9, idx+10)
plt.ylim(10**(-6), 1.5)
#plt.title("N={}, M_min={}, {} MC samples".format(N, x_min, n_samples), fontsize=20)
#plt.xticks(x_arr)

#plt.xlabel('k', fontsize=20)
plt.xlabel('cluster size', fontsize=20)
#plt.ylabel('cumulative distribution (c_k)', fontsize=20)
plt.show()
#plt.savefig("L{}_cluster_cumul_dist.png".format(rule_num))
