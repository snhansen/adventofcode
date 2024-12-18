import networkx as nx

with open("input") as f:
    inp = f.read().strip()

bytes = [tuple(map(int, line.split(","))) for line in inp.split("\n")]
N = 70
g = nx.grid_2d_graph(N + 1, N + 1)

for i, node in enumerate(list(g.nodes())):
    if node in bytes[:1024]:
        g.remove_node(node)

# Part 1
print(nx.shortest_path_length(g, (0, 0), (N, N)))

# Part 2
for node in bytes[1024:]:
    g.remove_node(node)
    if not nx.has_path(g, (0, 0), (N, N)):
        print(node)
        break