from itertools import combinations
import networkx as nx


with open("input") as f:
    inp = f.read().strip().split("\n")

boxes = [tuple(map(int, line.split(","))) for line in inp]

dists = [
    (sum((x - y) ** 2 for x, y in zip(p1, p2)), p1, p2)
    for p1, p2 in combinations(boxes, 2)
]

dists.sort(key = lambda x: -x[0])

g = nx.Graph()
i = 0
while dists:
    _, p1, p2 = dists.pop()
    g.add_edge(p1, p2)
    comps = list(nx.connected_components(g))
    if (i := i + 1) == 1000:
        sizes = sorted(list(map(len, comps)), reverse = True)
        print(sizes[0]*sizes[1]*sizes[2])
    if len(comps) == 1 and len(g.nodes()) == len(inp):
        print(p1[0]*p2[0])
        break