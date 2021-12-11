with open('input') as f:
    inp = f.read().strip().split()

grid = {}

for i, x in enumerate(inp):
    for j, y in enumerate(x):
        grid[j+i*1j] = int(y)

pos = [-1, 1, -1j, 1j, 1+1j, 1-1j, -1+1j, -1-1j]

def update_grid(g):
    for x in g:
        g[x] += 1
    g_new = dict(g)
    seen = set()
    while True:
        to_check = set(y for y, v in list(g_new.items()) if v > 9) - seen
        if not to_check:
            break
        for x in to_check:
            seen.add(x)
            for p in pos:
                if x+p in g and g_new[x+p] <= 9:  
                    g_new[x+p] += 1

    for x in g_new:
        if g_new[x] > 9:
            g_new[x] = 0

    return len(seen), g_new

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