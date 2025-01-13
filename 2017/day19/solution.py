with open("input") as f:
    inp = f.read().split("\n")


grid = {j + i*1j: x for i, l in enumerate(inp) for j, x in enumerate(l) if x != " "}

for p, c in grid.items():
    if p.imag == 0 and c == "|":
        start = p

dirs = {1: [1, 1j, -1j], -1: [-1, 1j, -1j], 1j: [1j, -1, 1], -1j: [-1j, -1, 1]}
p = start
dp = 1j
seen = []
while True:
    seen.append(p)
    stop = True
    for new_dp in dirs[dp]:
        new_p = p + new_dp
        if new_p in grid:
            p = new_p
            dp = new_dp
            stop = False
            break
    if stop:
        break

# Part 1
print("".join(grid[p] for p in seen if grid[p].isalpha()))

# Part 2
print(len(seen))