import networkx as nx

with open("input") as f:
    inp = f.read().strip().split("\n")

grid = {j + i*1j: x for i, l in enumerate(inp) for j, x in enumerate(l)}
dirs = [1, -1, 1j, -1j]

graph = nx.Graph()
for p, c in grid.items():
    graph.add_node(p)
    for dp in dirs:
        if p + dp in grid.keys() and grid[p + dp] == c:
            graph.add_edge(p, p+dp)

regions = list(nx.connected_components(graph))
areas = list(map(len, regions))


def get_perimeter(region):
    res = nx.Graph()
    for p in region:
        for dp in dirs:
            if p + dp not in region:
                res.add_node((p, dp))
    for p, q in res.nodes():
        for dp in dirs:
            if (p + dp, q) in res.nodes():
                res.add_edge((p, q), (p + dp, q))
    return res


# Part 1
perimeters = list(map(get_perimeter, regions))
print(sum(area*len(perimeter.nodes()) for area, perimeter in zip(areas, perimeters)))

# Part 2
sides = [len(list(nx.connected_components(perimeter))) for perimeter in perimeters]
print(sum(area*side for area, side in zip(areas, sides)))