import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import sys

condition = int(sys.argv[1])

if (condition == 1):
	nn_arr_list = [[],[1,3],[],[2,3,5],[3,4]]
elif (condition == 2):
	nn_arr_list = [[],[1,3],[2,9],[2,1,3],[11,18],[3,12,16],[1,8],[2,9],[],[7,11,13,17],[10,8,12,14],[16,9,11],[1,17],[2,13,18,8],[9,16,3,14],[11,18],[],[17,11]]

N = int(max(max(nn_arr) for nn_arr in nn_arr_list if nn_arr))
adj = np.zeros([N,N])

idx = 0
for nn_arr in nn_arr_list:
	if (len(nn_arr) > 0):
		for nn in nn_arr:
			nn_idx = nn - 1
			adj[idx, nn_idx] = 1

	idx += 1

G = nx.from_numpy_array(adj, create_using=nx.DiGraph())
mapping = {i: i + 1 for i in G.nodes}
G = nx.relabel_nodes(G, mapping)

#pos = nx.spectral_layout(G)
pos = nx.spring_layout(G)
#pos = nx.kamada_kawai_layout(G)

nodes_with_no_outgoing_links = [node for node, out_degree in G.out_degree() if out_degree == 0]
node_colors = ['red' if node in nodes_with_no_outgoing_links else 'lightblue' for node in G.nodes]

plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_size=700, node_color=node_colors, font_size=10, font_weight="bold", arrows=True)

plt.show()

