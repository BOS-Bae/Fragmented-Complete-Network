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

def adjust_positions(pos, shift_factor):
    adjusted_pos = pos.copy()
    nodes = list(pos.keys())
    for i, node1 in enumerate(nodes):
        for j, node2 in enumerate(nodes):
            if i >= j:
                continue
            dist = np.linalg.norm(np.array(pos[node1]) - np.array(pos[node2]))
            if dist < shift_factor:  
                direction = np.array(pos[node1]) - np.array(pos[node2])
                norm_direction = direction / np.linalg.norm(direction) if np.linalg.norm(direction) > 0 else np.random.rand(2)
                adjusted_pos[node1] += norm_direction * 2 * shift_factor
                adjusted_pos[node2] -= norm_direction * 2 * shift_factor
    return adjusted_pos

adjusted_pos = adjust_positions(pos, 0.02)

edge_labels = nx.get_edge_attributes(G, 'weight')

nodes_with_no_outgoing_links = [node for node, out_degree in G.out_degree() if out_degree == 0]
node_colors = ['blue' if node in nodes_with_no_outgoing_links else 'lightblue' for node in G.nodes]

nx.draw(G, adjusted_pos, with_labels=True, node_size=1800, node_color=node_colors,
        font_size=8, font_color="red", font_weight="bold", arrows=True, arrowsize=10)

plt.show()
