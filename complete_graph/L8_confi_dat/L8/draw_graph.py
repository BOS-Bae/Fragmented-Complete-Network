import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

N = 18 # from 3:1 and error from 3 to 1

nn_arr_list = [[],[1,3],[2,9],[2,1,3],[11,18],[3,12,16],[1,8],[2,9],[],[7,11,13,17],
[10,8,12,14],[16,9,11],[1,17],[2,13,18,8],[9,16,3,14],[11,18],[],[17,11]]

adj = np.zeros([N,N])

idx = 0
for nn_arr in nn_arr_list:
	if (len(nn_arr) > 0):
		for nn in nn_arr:
			nn_idx = nn - 1
			adj[idx, nn_idx] = 1

	idx += 1

G = nx.from_numpy_array(adj, create_using=nx.DiGraph())

pos = nx.spectral_layout(G)
#pos = nx.kamada_kawai_layout(G)

absorbing_states = [1,9,17]
node_colors = ['red' if node in absorbing_states else 'lightblue' for node in G.nodes]

plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_size=700, node_color=node_colors, font_size=10, font_weight="bold", arrows=True)


plt.title("Directed Network Structure with Layout")
plt.show()

