import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import os.path
import sys

if (len(sys.argv) < 4):
    print("python3 opinion_avg.py N rule_num n_s bins")
    exit(1)

N = int(sys.argv[1])
rule_num = int(sys.argv[2])
n_s = int(sys.argv[3])
nbins = int(sys.argv[4])
M_max = N

op_dist = np.zeros(n_s)
for n in range(n_s):
    file = "./N{}_L{}_dat/N{}_L{}_image_s{}".format(N, rule_num, N, rule_num, n)
    if os.path.getsize(file) > 0: 
        image = np.loadtxt(file)
        n_samples += 1
        #image = np.loadtxt("./N{}_L{}_dat/N{}_L{}_image_s{}".format(N, rule_num, N, rule_num, n))
				op_dist[n] = np.average(image)

plt.hist(op_dist, bins=nbins, color="black", range = (-1,1))
plt.xticks(np.arange(-1,1.5,0.5),fontsize=13)
plt.yticks(fontsize=13)
plt.title("N={}, L{}, {} MC samples".format(N, rule_num, n_s))
#plt.xticks(x_arr)
plt.xlabel('average opinion', fontsize=15)
plt.show()

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
