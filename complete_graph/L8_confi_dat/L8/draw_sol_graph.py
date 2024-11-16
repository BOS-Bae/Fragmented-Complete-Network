import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import sys


def print_coupled_equations(w_connections, M):
    nodes = sorted(set(w_connections[:, 0]) | set(w_connections[:, 1]))
    equations = {node: [] for node in nodes}

    for source, target, weight in w_connections:
        equations[source].append((target, weight))

    for node in nodes:
        terms = equations[node]
        equation_terms = " + ".join(
            [f"({weight}/{M})*a{target}" for target, weight in terms])
        equation = f"a{node} == {equation_terms} &&" if equation_terms else f"a{node} == 0"
        print(equation)
    variables_print = ", ".join([f"a{node}" for node in nodes])
    print(variables_print)


if (len(sys.argv) < 2):
    print("python3 draw_sol_graphy.py N idx spectral_or_spring")
    exit(1)

N = int(sys.argv[1])
idx = int(sys.argv[2])
spectral_or_spring = int(sys.argv[3])

M = N*N

file_path = "./flip_dat/prob-N{}-L8-idx{}.dat".format(N, idx)
weight_connections = np.loadtxt(file_path, dtype=int)
print_coupled_equations(weight_connections, M)

G = nx.DiGraph()

for source, target, weight in weight_connections:
	G.add_edge(source, target, weight=weight)

#edge_labels = { (source, target): f"{weight}/{M}" for source, target, weight in weight_connections}

self_edges = list(nx.selfloop_edges(G))
G.remove_edges_from(self_edges)

if (spectral_or_spring == 0):
	pos = nx.spectral_layout(G)
	
else : pos = nx.spring_layout(G)

nodes_with_no_outgoing_links = [node for node, out_degree in G.out_degree() if out_degree == 0]

node_colors = ['red' if node in nodes_with_no_outgoing_links else 'lightblue' for node in G.nodes]
print(nodes_with_no_outgoing_links)
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_size=200, node_color=node_colors,
        font_size=8, font_weight="bold", arrows=True, arrowsize=10)

#nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()
