import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import sys

if (len(sys.argv) < 2):
    print("pytnon3 show_cliques_t.py s_idx t_idx")
    exit(1)

s_idx = int(sys.argv[1])
t_idx = int(sys.argv[2])
N = 100

def count_clusters(A):
    # A : adjacency matrix
		G = nx.from_numpy_array(np.array(A))
		cliques = list(nx.find_cliques(G))
		
		large_clique_count = sum(1 for clique in cliques if len(clique) >= 2)

		return large_clique_count


mat_st = np.loadtxt("./WB_dat/Image_hyrax_PLS_N100_s{}.dat".format(s_idx))
idx = t_idx*N
mat_t = mat_st[idx:idx+N]

n_cliques = count_clusters(mat_t)
G = nx.from_numpy_array(mat_t)

pos = nx.spring_layout(G, seed=35)

fig, ax = plt.subplots(figsize=(6,4))
#nx.draw(G, pos, with_labels=True, node_color='blue', node_size=600, font_size=14, width=0.5)
nx.draw(G, pos, node_color='blue', node_size=50, font_size=14, width=0.5)
ax.set_title("t={}: n_cliques = {}".format(t_idx,n_cliques),fontsize=16)
plt.show()

