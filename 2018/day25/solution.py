import networkx as nx
import re
from itertools import combinations

with open("input") as f:
    inp = f.read().strip().split("\n")


def dist(p1, p2):
    return sum(abs(c1 - c2) for c1, c2 in zip(p1, p2))


points = [tuple(map(int, re.findall("-?\d+", line))) for line in inp]
g = nx.Graph()

for p1, p2 in combinations(points, 2):
    g.add_node(p1)
    g.add_node(p2)
    if dist(p1, p2) <= 3:
        g.add_edge(p1, p2)

# Part 1
print(len(list(nx.connected_components(g))))