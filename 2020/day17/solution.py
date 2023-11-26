from collections import defaultdict, Counter
from itertools import product
from copy import deepcopy

with open('input') as f:
    inp = f.read()

grid_inp = defaultdict(lambda: '.')

x, y, z, w = 0, 0, 0, 0
for c in inp:
    if c != '\n':
        grid_inp[(x, y, z, w)] = c
        x += 1
    else:
        x = 0
        y += 1

def update(g, part2 = False):  
    new_g = deepcopy(g)
    if part2: 
        ps = list(set([(x + dx, y + dy, z + dz, w + dw) for x, y, z, w in list(g) for dx, dy, dz, dw in product([-1, 0, 1], repeat = 4)]))
    else:
        ps = list(set([(x + dx, y + dy, z + dz, 0) for x, y, z, _ in list(g) for dx, dy, dz in product([-1, 0, 1], repeat = 3)]))
    for p in ps:
        x, y, z, w = p
        if part2:
            c = Counter(g[(x + dx, y + dy, z + dz, w + dw)] for dx, dy, dz, dw in product([-1, 0, 1], repeat = 4) if (dx, dy, dz, dw) != (0, 0, 0, 0))['#']
        else:
            c = Counter(g[(x + dx, y + dy, z + dz, 0)] for dx, dy, dz in product([-1, 0, 1], repeat = 3) if (dx, dy, dz) != (0, 0, 0))['#']
        if g[p] == '#' and c not in [2, 3]:
            new_g[p] = '.'
        elif g[p] == '.' and c == 3:
            new_g[p] = '#'
        else:
            new_g[p] = g[p]
    return new_g
    
def solve(part2 = False):
    grid = deepcopy(grid_inp)
    for _ in range(6):
        grid = update(grid, part2)

    return Counter([grid[p] for p in grid])['#']

# Part 1
print(solve())

# Part 2
print(solve(True))