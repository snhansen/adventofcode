import networkx as nx
from functools import cache

with open("input") as f:
    inp = f.read().strip().split("\n")

g = nx.DiGraph()
for line in inp:
    in_, outs = line.split(": ")
    for out in outs.split():
        g.add_edge(in_, out)

# Part 1
print(len(list(nx.all_simple_paths(g, "you", "out"))))

# Part 2
@cache
def no_paths(fr, to, fft = False, dac = False):
    fft = fft or (fr == "fft")
    dac = dac or (fr == "dac")
    if fr == to:
        return 1 if fft and dac else 0
    return sum(no_paths(neighbor, to, fft, dac) for neighbor in g.neighbors(fr))


print(no_paths("svr", "out"))