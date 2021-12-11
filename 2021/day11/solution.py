with open('input') as f:
    inp = f.read().strip().split()

grid = {}

for i, x in enumerate(inp):
    for j, y in enumerate(x):
        grid[j + i * 1j] = int(y)

pos = [-1, 1, -1j, 1j, 1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j]


def update_grid(g):
    for x in g:
        g[x] += 1
    seen = set()
    while True:
        to_check = {y for y, v in g.items() if v > 9} - seen
        if not to_check:
            for x in g:
                if g[x] > 9:
                    g[x] = 0
            return len(seen), g
        for x in to_check:
            seen.add(x)
            for p in pos:
                if x + p in g:
                    g[x + p] += 1


# Part 1 and 2
c_tot = 0
i = 0
while True:
    c, grid = update_grid(grid)
    c_tot += c
    i += 1
    if i == 100:
        print(c_tot)
    if c == len(grid):
        print(i)
        break
