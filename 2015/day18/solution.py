with open('input') as f:
    inp = [x.strip() for x in f.readlines()]

grid = {}
for j, y in enumerate(inp):
    for i, x in enumerate(y):
        grid[complex(i, j)] = int(x == '#')

# Part 1
def update_grid(g):
    new_g = {}
    for p in g:
        lights = 0
        for d1 in [-1, 0, 1]:
            for d2 in [-1j, 0, 1j]:
                if (d1 or d2) and 0<=(p+d1+d2).real<=len(g)**0.5-1 and 0<=(p+d1+d2).imag<=len(g)**0.5-1:
                    lights += g[p+d1+d2]
        if g[p]:
            new_g[p] = 1 if lights in [2, 3] else 0
        else:
            new_g[p] = 1 if lights == 3 else 0
    return new_g


grid_pt1 = dict(grid)
for _ in range(100):
    grid_pt1 = update_grid(grid_pt1)

print(len([p for p in grid if grid_pt1[p] == 1]))

# Part 2
def update_grid_v2(g):
    new_g = {}
    for p in g:
        if p in [0, 99j, 99, 99+99j]:
            new_g[p] = 1
        else:
            lights = 0
            for d1 in [-1, 0, 1]:
                for d2 in [-1j, 0, 1j]:
                    if (d1 or d2) and 0<=(p+d1+d2).real<=len(g)**0.5-1 and 0<=(p+d1+d2).imag<=len(g)**0.5-1:
                        lights += g[p+d1+d2]
            if g[p]:
                new_g[p] = 1 if lights in [2, 3] else 0
            else:
                new_g[p] = 1 if lights == 3 else 0
    return new_g

grid_pt2 = dict(grid)
for p in [0, 99j, 99, 99+99j]:
    grid_pt2[p] == 1

for _ in range(100):
    grid_pt2 = update_grid_v2(grid_pt2)

print(len([p for p in grid if grid_pt2[p] == 1]))

# def print_grid(g):
    # dict = {1: '#', 0: '.'}
    # n = int(len(g)**0.5)
    # for j in range(n):
        # l = []
        # for i in range(n):
            # l.append(dict[g[complex(i, j)]])
        # print(''.join(l))
