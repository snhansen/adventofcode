from collections import defaultdict, Counter
from itertools import product
from copy import deepcopy

with open('input') as f:
    inp = f.read()

# Part 1
grid = defaultdict(lambda: '.')

x, y, z = 0, 0, 0
for c in inp:
    if c != '\n':
        grid[(x, y, z)] = c
        x += 1
    else:
        x = 0
        y += 1

def update(g):  
    new_g = deepcopy(g)
    cs = {}
    ps = list(set([(x + dx, y + dy, z + dz) for x, y, z in list(g) for dx, dy, dz in product([-1, 0, 1], repeat = 3)]))
    for p in ps:
        x, y, z = p
        cs[(x, y, z)] = Counter(g[(x + dx, y + dy, z + dz)] for dx, dy, dz in product([-1, 0, 1], repeat = 3) if (dx, dy, dz) != (0, 0, 0))['#']
        if g[p] == '#' and cs[p] not in [2, 3]:
            new_g[p] = '.'
        elif g[p] == '.' and cs[p] == 3:
            new_g[p] = '#'
        else:
            new_g[p] = g[p]
    return new_g

for _ in range(6):
    grid = update(grid)

print(Counter([grid[p] for p in grid])['#'])

# Part 2
grid = defaultdict(lambda: '.')

x, y, z, w = 0, 0, 0, 0
for c in inp:
    if c != '\n':
        grid[(x, y, z, w)] = c
        x += 1
    else:
        x = 0
        y += 1

def update(g):  
    new_g = deepcopy(g)
    cs = {}
    ps = list(set([(x + dx, y + dy, z + dz, w + dw) for x, y, z, w in list(g) for dx, dy, dz, dw in product([-1, 0, 1], repeat = 4)]))
    for p in ps:
        x, y, z, w = p
        cs[(x, y, z, w)] = Counter(g[(x + dx, y + dy, z + dz, w + dw)] for dx, dy, dz, dw in product([-1, 0, 1], repeat = 4) if (dx, dy, dz, dw) != (0, 0, 0, 0))['#']
        if g[p] == '#' and cs[p] not in [2, 3]:
            new_g[p] = '.'
        elif g[p] == '.' and cs[p] == 3:
            new_g[p] = '#'
        else:
            new_g[p] = g[p]
    return new_g

for _ in range(6):
    grid = update(grid)

print(Counter([grid[p] for p in grid])['#'])