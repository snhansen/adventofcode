from collections import defaultdict, Counter
from copy import copy

with open("input") as f:
    inp = f.read().strip()

g = defaultdict(lambda: 0)
for y, line in enumerate(inp.split("\n")):
    for x, c in enumerate(line):
        if c == "#":
            g[x+y*1j] = 1

adj = [1, -1, 1j, -1j, 1+1j, 1-1j, -1+1j, -1-1j]
dirs_p = [(-1-1j, -1j, 1-1j), (-1+1j, 1j, 1+1j), (-1-1j, -1, -1+1j), (1-1j, 1, 1+1j)]

# 0 = North, 1 = South, 2 = West, 3 = East.
def update(g, start):
    new_g = copy(g)
    props = {}
    dirs = dirs_p[start:] + dirs_p[:start]
    for p, v in list(g.items()):
        if v == 0:
            continue
        if all(g[p+dp] == 0 for dp in adj):
            continue
        for dps in dirs:
            if all(g[p+dp] == 0 for dp in dps):
                props[p] = p + dps[1]
                break
    counts = Counter(props.values())
    for p, pto in props.items():
        if counts[pto] == 1:
            new_g[p] = 0
            new_g[pto] = 1
    return new_g


# Part 1 and 2
start, i = 0, 0
prev_ps = set([p for p, v in g.items() if v == 1])
while True:
    g = update(g, start)
    start = (start+1)%len(dirs_p)
    new_ps = set([p for p, v in g.items() if v == 1])
    if i == 9:  
        xmin = int(min(p.real for p, v in g.items() if v == 1))
        xmax = int(max(p.real for p, v in g.items() if v == 1))
        ymin = int(min(p.imag for p, v in g.items() if v == 1))
        ymax = int(max(p.imag for p, v in g.items() if v == 1))
        print(sum(g[x+y*1j] == 0 for x in range(xmin, xmax+1) for y in range(ymin, ymax+1)))
    if new_ps == prev_ps:
        print(i+1)
        break
    prev_ps = new_ps
    i += 1