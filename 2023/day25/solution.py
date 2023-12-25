import networkx as nx
import matplotlib.pyplot as plt
from math import prod

with open("input") as f:
    inp = f.read().strip().split("\n")


g = nx.Graph()

for line in inp:
    lhs, rhs = line.split(": ")
    rhs = rhs.split(" ")
    for node in rhs:
        g.add_edge(lhs, node)

# We draw the graph to see which edges we need to remove. 
# nx.draw(g, with_labels = True, font_size = 8)
# plt.show()

g.remove_edge("vcq", "lxb")
g.remove_edge("znk", "mmr")
g.remove_edge("ddj", "rnx")
print(prod(map(len, nx.connected_components(g))))

# Alternatively, we can let networkx do it all:
# for edge in nx.minimum_edge_cut(g):
    # g.remove_edge(edge[0], edge[1])

# print(prod(map(len, nx.connected_components(g))))