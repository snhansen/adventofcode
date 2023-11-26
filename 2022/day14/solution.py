from collections import defaultdict
from copy import copy

with open("input") as f:
    inp = f.read().strip().split("\n")

ls = []
for line in inp:
    ps = []
    for c in line.split(" -> "):
        i, j = list(map(int, c.split(",")))
        ps.append((i,j))
    ls.append(ps)

grid = defaultdict(lambda: ".")
for l in ls:
    for (x1, y1), (x2, y2) in zip(l[:-1], l[1:]):
        for i in range(min(x1, x2), max(x1, x2) + 1):
            for j in range(min(y1, y2), max(y1, y2) + 1):
                grid[i + j*1j] = "#"

reals = [int(p.real) for p in grid if grid[p] != "."]
imags = [int(p.imag) for p in grid if grid[p] != "."]
left = min(reals)
right = max(reals)
bottom = max(imags)

def at_rest(grid, p):
    return grid[p+1j] != "." and grid[p-1+1j] != "." and grid[p+1+1j] != "."


def solve(part2 = False):
    grid_cp = copy(grid)
    if part2:
        max_imags = max(imags)
        for i in range(10000):
            grid_cp[500+i+(max_imags+2)*1j] = "#"
            grid_cp[500-i+(max_imags+2)*1j] = "#"
    c = 0
    while True:
        p = 500
        if part2 and at_rest(grid_cp, p):
            return c + 1
        while not at_rest(grid_cp, p):
            if not part2 and (p.real < left or p.real > right or p.imag > bottom):
                return c
            if grid_cp[p+1j] == ".":
                p = p+1j
            elif grid_cp[p-1+1j] == ".":
                p = p-1+1j
            elif grid_cp[p+1+1j] == ".":
                p = p+1+1j
        grid_cp[p] = "o"
        c += 1


# Part 1
print(solve())

# Part 2
print(solve(True))