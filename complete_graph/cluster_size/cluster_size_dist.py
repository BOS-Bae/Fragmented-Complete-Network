from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import os.path
import sys

if (len(sys.argv) < 3):
    print("python3 cluster_size_diff.py N n_s sl")
    exit(1)

N = int(sys.argv[1])
n_s = int(sys.argv[2])
sl = int(sys.argv[3])
M_max = N

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
def cluster_size_info(cluster_info):
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
    
#To check whether this cluster size distribution has a form of power-law.
def power_curve(m, a,b):
    return a*(np.power(m,b))

c_dist_tot = np.zeros([n_s,M_max])

n_samples = 0
for n in range(n_s):
    file = "./N{}_L{}_dat/N{}_L{}_image_s{}".format(N, rule_num, N, rule_num, n)
    if os.path.getsize(file) > 0: 
        image = np.loadtxt(file)
        n_samples += 1
        #image = np.loadtxt("./N{}_L{}_dat/N{}_L{}_image_s{}".format(N, rule_num, N, rule_num, n))
        cluster_info = seek_cluster(N, image)
        c_size = cluster_size_info(cluster_info)
        c_dist_n = size_distribution(c_size, M_max)
        c_dist_tot[n] = c_dist_n

c_dist = np.average(c_dist_tot,0)
cumul_dist = np.zeros(len(c_dist))
for i in range(len(c_dist)):
    cumul_dist[i] = sum(list(c_dist[i:]))
    #cumul_dist[i] = sum(list(c_dist[:i+1]))

c_dist_err = np.std(c_dist_tot,0)/np.sqrt(n_samples)

x_arr = range(1,int(M_max+1))
#popt, pcov = curve_fit(power_curve, x_arr[sl:] ,c_dist[sl:])
popt1, pcov1 = curve_fit(power_curve, x_arr[sl:] ,c_dist[sl:])
popt2, pcov2 = curve_fit(power_curve, x_arr[sl:] ,cumul_dist[sl:])
fit_curve1 = power_curve(x_arr, *popt1)
fit_curve2 = power_curve(x_arr, *popt2)

plt.plot(x_arr, c_dist, label="numerical data", marker = 'o', color='blue')
plt.errorbar(x_arr, c_dist, yerr= c_dist_err, color='blue')
plt.plot(x_arr, fit_curve1, label="{:.1f}m^{:.2f}".format(popt1[0], popt1[1]), marker = 'o', color='lightseagreen')
plt.legend(fontsize=13)
plt.xscale('log')
plt.yscale('log')
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.title("N={}, L{}, {} MC samples".format(N, rule_num, n_samples))
#plt.xticks(x_arr)
plt.xlabel('M', fontsize=15)
plt.ylabel('frequency', fontsize=15)
#plt.show()
plt.savefig("L{}_cluster_dist.png".format(rule_num))
plt.clf()

plt.plot(x_arr, cumul_dist, label="numerical data, F(m <= X)", marker = 'o', color='blue')
plt.errorbar(x_arr, cumul_dist, yerr= c_dist_err, color='blue')
plt.plot(x_arr, fit_curve2, label="{:.1f}m^{:.2f}".format(popt2[0], popt2[1]), marker = 'o', color='lightseagreen')
plt.legend(fontsize=13)
plt.xscale('log')
plt.yscale('log')
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.title("N={}, L{}, {} MC samples".format(N, rule_num, n_samples))
#plt.xticks(x_arr)
plt.xlabel('M', fontsize=15)
plt.ylabel('cumulative frequency', fontsize=15)
#plt.show()
plt.savefig("L{}_cluster_cumul_dist.png".format(rule_num))

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
