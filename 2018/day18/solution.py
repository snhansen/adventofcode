from collections import Counter
from itertools import count

with open("input") as f:
    inp = f.read().strip().split("\n")

grid_init = {x + y*1j: c for y, line in enumerate(inp) for x, c in enumerate(line)}


def update(grid):
    dirs = [1, -1, 1j, -1j, 1+1j, 1-1j, -1+1j, -1-1j]
    new_grid = dict(grid)
    for p, c in grid.items():
        adj = Counter([grid[p + dp] for dp in dirs if p + dp in grid])
        if c == "." and adj["|"] >= 3:
            new_grid[p] = "|"
        elif c == "|" and adj["#"] >= 3:
            new_grid[p] = "#"
        elif c == "#" and (adj["#"] == 0 or adj["|"] == 0):
            new_grid[p] = "."
    return new_grid


def resource_value(n):
    grid = dict(grid_init)
    for t in range(n):
        grid = update(grid)
    c = Counter(grid.values())
    return c["#"]*c["|"]


# Part 1
print(resource_value(10))

# Part 2
grid = grid_init
seen = []
for t in count():
    h = "".join(grid.values())
    if h in seen:
        break
    seen.append(h)
    grid = update(grid)

t2 = t
t1 = seen.index(h)
n = 1000000000
m = (n - t1) // (t2 - t1)
print(resource_value(n - m*(t2- t1)))