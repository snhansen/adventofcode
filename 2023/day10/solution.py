import networkx as nx
from copy import deepcopy
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from itertools import product

with open("input") as f:
    inp = f.read().strip().split("\n")

n_row = len(inp)
n_col = len(inp[0])
grid = {}

for row, line in enumerate(inp):
    for col, c in enumerate(line):
        grid[col+row*1j] = c
        if c == "S":
            start = col + row*1j


def get_graph(grid, start, start_pipe):
    pipes = {"|": (1j, -1j), "-": (1, -1), "L": (-1j, 1), "J": (-1, -1j), "7": (-1, 1j), "F":  (1j, 1)} 
    g = nx.Graph()
    p, pipe = start, start_pipe
    while True:
        for dp in pipes[pipe]:
            q = p + dp
            if (q.imag < 0) or (q.imag > n_row-1) or (q.real < 0) or (q.real > n_col-1):
                continue
            if q == start and len(g.nodes()) > 2:
                g.add_edge(p, q)
                return g
            if q in g.nodes():
                continue
            g.add_edge(p, q)
            p, pipe = q, grid[q]
            break

# # Part 1
g = get_graph(grid, start, "|")
print(g.number_of_nodes()//2)

# Part 2
loop = deepcopy(g.nodes())

for i, j in product(range(n_col), range(n_row)):
        p = i + j*1j
        if p in loop:
            continue
        for dp in [-1, 1, -1j, 1j]:
            q = p + dp
            if (q.imag < 0) or (q.imag > n_row-1) or (q.real < 0) or (q.real > n_col-1):
                continue
            g.add_node(p)
            if q not in loop:
                g.add_edge(p, q)
  

polygon = Polygon([(int(x.real), int(x.imag)) for x in loop])

res = 0
for comp in nx.connected_components(g):
    p = list(comp)[0]
    p = (int(p.real), int(p.imag))
    if polygon.contains(Point(p)):
        res += len(comp)

print(res)