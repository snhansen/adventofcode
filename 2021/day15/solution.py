from heapq import heappop, heappush
from collections import defaultdict

inp = open('input').read().strip().split('\n')

grid = {}
for r, l in enumerate(inp):
    for c, x in enumerate(l):
        grid[c + r*1j] = int(x)

def get_min_risk(g):
    coord = int(len(g)**0.5) - 1
    corner = coord + coord*1j
    start = (0, id(0), 0)
    to_check = [start]
    min_risk = defaultdict(lambda: float('inf'))

    while to_check:
        risk, _, pos = heappop(to_check)
        if pos == corner:
            return risk
        for d in [-1, 1, 1j, -1j]:
            if pos + d in g:
                new_pos = pos + d
                new_risk = risk + g[new_pos]
                if new_risk < min_risk[new_pos]:
                    heappush(to_check, (new_risk , id(new_pos), new_pos))
                    min_risk[new_pos] = new_risk
    

# Part 1
print(get_min_risk(grid))

# Part 2
factor = 5
dim = (int(len(grid)**0.5))

for i in range(factor*dim):
    for j in range(factor*dim):
        if j >= dim or i >= dim:
            grid[i + j*1j] = (grid[(i%dim) + (j%dim)*1j] + i//dim + j//dim)
            while grid[i + j*1j] > 9:
                grid[i + j*1j] -= 9

print(get_min_risk(grid))