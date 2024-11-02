from scipy.optimize import curve_fit
from scipy.optimize import minimize
from scipy.special import zeta
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import os.path
import sys

if (len(sys.argv) < 6):
    print("python3 err_sample_cluster_size_dist.py N n_run ns fit_i fit_f e_idx")
    exit(1)

N = int(sys.argv[1])
n_run = int(sys.argv[2])
ns = int(sys.argv[3])
sl = int(sys.argv[4])
sl_f = int(sys.argv[5])
e_idx = int(sys.argv[6])
M_max = N
x_arr = range(1,int(M_max+1))
x_min = x_arr[sl]
rule_num = 8

#To seek cluster information from image matrix
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

#To get cluster size from cluster information
def cluster_size_info(N,cluster_info):
    cluster_dist = np.zeros(int(max(cluster_info)))
    for i in range(1,int(max(cluster_info)+1)):
        for k in range(N):
            if (cluster_info[k] == i) : cluster_dist[i-1] += 1

    return cluster_dist

#To obtain cluster size 'distribution' from cluster sizes
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

#To check whether this cluster size distribution has a form of power-law.
def power_curve(m, a,b):
    return a*(np.power(m,b))

#Check_mat1 = np.array([[-1,1,-1,-1,-1,-1,-1],[1,1,-1,-1,-1,-1,-1],
#             [-1,-1,1,1,1,-1,-1],[-1,-1,1,1,1,-1,-1],[-1,-1,1,1,1,-1,-1],
#             [-1,-1,-1,-1,-1,1,-1],[-1,-1,-1,-1,-1,-1,-1]])
#c1_info = seek_cluster(len(Check_mat1), Check_mat1)
#c1_size = cluster_size_info(len(Check_mat1), c1_info)
#c1_dist_n = size_distribution(c1_size, len(Check_mat1))
#
#Check_mat2 = np.array([[1,1,-1,-1,-1,-1,-1],[1,1,-1,-1,-1,-1,-1],
#             [-1,-1,1,1,1,-1,-1],[-1,-1,1,1,1,-1,-1],[-1,-1,1,1,1,-1,-1],
#             [-1,-1,-1,-1,-1,1,-1],[-1,-1,-1,-1,-1,-1,1]])
#c2_info = seek_cluster(len(Check_mat1), Check_mat2)
#c2_size = cluster_size_info(len(Check_mat2), c2_info)
#c2_dist_n = size_distribution(c2_size, len(Check_mat2))
#
#print(c1_size)
#print(c1_dist_n ,"\n")
#print(c2_size)
#print(c2_dist_n)

c_dist_tot = []


n_samples = 0
each_idx_list = [int(0), int(n_run/4), int(2*n_run/4), int(3*n_run/4), int(n_run-1)]

total_dat = np.zeros(ns)
each_idx = each_idx_list[e_idx]
for n in range(ns):
    not_completed_arr = []
    file = "./N{}_L{}_dat_err/N{}_L{}_image_n{}_s{}".format(N, rule_num, N, rule_num, n_run, n)
    n_row_i = 0 + N*each_idx
    n_row_f = N + N*each_idx
    image = np.loadtxt(file)
    image_each = image[int(n_row_i):int(n_row_f)]
    c_dist = get_cluster_size_distribution(N, image_each)

    x_arr = range(1,int(M_max+1))
    x_data = []
    c_data = []
    idx = 0
    cumul_dist = np.zeros(len(c_dist))
    
    if (c_dist[x_min] == 0):
        print("x_min is not good value : y value is zero.")
        exit(1)
    
    count1 = 0
    count2 = 0
    ln_x_sum1 = 0
    ln_x_sum2 = 0
    
    for i in range(sl,sl_f):
        cumul_dist[i] = sum(list(c_dist[i:]))
        if (c_dist[i] != 0):
            idx = x_arr[i]
            x_data.append(x_arr[i])
            c_data.append(c_dist[i])
            count1 += 1
            ln_x_sum1 += np.log(x_arr[i])
    
    for i in range(len(cumul_dist)):
        if (cumul_dist[i] != 0):
            count2 += 1
            ln_x_sum2 += np.log(x_arr[i])
    
    def loss_fn_1(a):
        return -(-count1*np.log(zeta(a,x_min)) - a*ln_x_sum1)
    
    def loss_fn_2(a):
        return -(-count2*np.log(zeta(a,x_min)) - a*ln_x_sum2)
    
    init_condition = 1.05
    res1 = minimize(loss_fn_1, x0 = [init_condition])
    res2 = minimize(loss_fn_2, x0 = [init_condition])
    
    a1 = res1.x; alpha1 = a1[0]
    #a2 = res2.x; alpha2 = a2[0]
    alpha2 = alpha1 - 1
    
    total_dat[n] = alpha1

each_idx = each_idx_list[e_idx]
plt.plot(range(ns), total_dat[int(e_idx),:], marker='o', label = "N={}, n={}".format(N, each_idx))
plt.legend(fontsize=14)
plt.xlabel('index (MC sample)', fontsize=15)
plt.ylabel('fitting result (exponent)', fontsize=15)
plt.savefig("./power_fit_N{}_n{}.png".format(N, each_idx))
plt.clf()

    #normalization_check = sum(np.arange(1,N+1,1)*c_dist)/N
    #M_value_check = sum(c_dist)/N
    #print("sum_m m*c_m = ", normalization_check)
    #print("\sum_m c_m = ", M_value_check)
    
    #print("M_sl = ", x_data[sl])
    #print("M_sl_cumul = ", x_arr[x_data[sl]-1])
    #print(x_data)
    #print(c_data)
    
    #popt1, pcov1 = curve_fit(power_curve, x_data[sl:] ,c_data[sl:])
    #popt2, pcov2 = curve_fit(power_curve, x_arr[int(x_data[sl]-1):] ,cumul_dist[int(x_data[sl]-1):])
    #fit_curve1 = power_curve(x_arr, *popt1)
    #fit_curve2 = power_curve(x_arr, *popt2)
    
    #C1 = np.sum(c_dist[sl : ])/zeta(alpha1, x_min)
    #print(C1/N)
    #print(c_dist[0]/N)
    #C2 = np.sum(c_dist[sl : ])*np.power((1/x_min), -alpha2)

'''
plus=0
negative=0

for i in range(N):
    image[i,i] = 0
    for j in range(N):
        if image[i,j] == 1:
            plus+=1
        elif image[i,j] == -1:
            negative+=1
        
print("plus(%)=",plus/(N*N))
print("negative(%)=",negative/(N*N))

fig,ax=plt.subplots()
im=ax.imshow(image,cmap='gray')
plt.title("N={}, L{} rule".format(N, rule_num))
plt.show()

G=nx.Graph()

for i in range(N):
    for j in range(N):
        if image[i,j]==1:
            G.add_edge("{}".format(i),"{}".format(j),weight=1)
        elif image[i,j]==-1:
            G.add_edge("{}".format(i),"{}".format(j),weight=-1)
            
eplus = [(u,v) for (u,v,d) in G.edges(data=True) if d["weight"]==1]
eminus = [(u,v) for (u,v,d) in G.edges(data=True) if d["weight"]==-1]

#pos = nx.spring_layout(G)
pos = nx.spectral_layout(G)
colors = [cluster_info[int(node)] for node in G.nodes()]
G.remove_edges_from(eminus)

nx.draw_networkx(G, pos, node_color=colors, cmap=plt.get_cmap('jet'), with_labels=True, node_size=500, edge_color='gray')

#nx.draw_networkx_edges(G,pos=pos,edgelist=eplus,width=5,alpha=0.5,edge_color="b")
#nx.draw_networkx(G,pos)

plt.axis("off")
plt.tight_layout()
plt.title("N={}, L{} rule".format(N, rule_num))
plt.show()
'''
