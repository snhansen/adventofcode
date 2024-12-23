import networkx as nx
from itertools import combinations

with open("input") as f:
    inp = f.read().strip().split("\n")


g = nx.Graph()
for line in inp:
    c1, c2 = line.split("-")
    g.add_edge(c1, c2)

# Part 1
cliques = list(nx.find_cliques(g))
three_comp = set()
for clique in cliques:
    if len(clique) < 3:
        continue
    for c1, c2, c3 in combinations(clique, 3):
        if c1.startswith("t") or c2.startswith("t") or c3.startswith("t"):
            three_comp.add(tuple(sorted([c1, c2, c3])))

print(len(three_comp))

# Part 2
max_clique_size = max(map(len, cliques))
for clique in cliques:
    if len(clique) == max_clique_size:
        print(",".join(sorted(clique)))