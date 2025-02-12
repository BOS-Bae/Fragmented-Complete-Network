import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

N = 100
T = 1000
ns = 50

def count_clusters(A):
    # A : adjacency matrix
		G = nx.from_numpy_array(np.array(A))
		cliques = list(nx.find_cliques(G))
		
		large_clique_count = sum(1 for clique in cliques if len(clique) >= 2)

		return large_clique_count


#check_si = 0
clique_dat = np.zeros([ns, T])
for s in range(ns):
    print(s)
    mat_tot = np.loadtxt("./WB_dat/Image_hyrax_PLS_N100_s{}.dat".format(s))
    idx = 0 
    for t in range(T):
        mat_t = mat_tot[idx:idx+N]
        '''
        for i in range(N):
            if (mat_t[i,i] == 0): check_si += 1
        '''
        idx += N
        clique_dat[s, t] = count_clusters(mat_t)

clique_avg = np.average(clique_dat, 0)
clique_stderr = np.std(clique_dat, 0) / np.sqrt(ns)

plt.plot(range(T), clique_avg, label="find_cliques", marker='.', color="black")
plt.errorbar(range(T), clique_avg, yerr=clique_stderr, color="black")
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel("t",fontsize=16)
plt.ylabel("n_cliques",fontsize=16)
plt.legend()
plt.show()
