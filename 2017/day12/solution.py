import networkx as nx

with open("input") as f:
    inp = f.read().strip().split("\n")

g = nx.Graph()
for line in inp:
    first, others = line.split(" <-> ")
    for other in others.split(", "):
        g.add_edge(first, other)

# Part 1
comps = list(nx.connected_components(g))
for comp in comps:
    if "0" in comp:
        print(len(comp))
        break

# Part 2
print(len(comps))