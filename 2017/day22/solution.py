from collections import defaultdict

with open("input") as f:
    inp = f.read().strip().split("\n")


# Part 1
grid = defaultdict(lambda: ".")
for i, l in enumerate(inp):
    for j, x in enumerate(l):
        grid[j + i*1j] = x
        
p = (j // 2) + 1j*(i // 2)
dp = -1j
c = 0
for _ in range(10000):
    if grid[p] == "#":
        dp *= 1j
        grid[p] = "."
    else:
        dp *= -1j
        grid[p] = "#"
        c += 1
    p += dp

print(c)

# Part 2
grid = defaultdict(lambda: ".")
for i, l in enumerate(inp):
    for j, x in enumerate(l):
        grid[j + i*1j] = x
        
p = (j // 2) + 1j*(i // 2)
dp = -1j
c = 0
for _ in range(10000000):
    if grid[p] == "#":
        dp *= 1j
        grid[p] = "F"
    elif grid[p] == "F":
        dp *= -1
        grid[p] = "."
    elif grid[p] == "W":
        grid[p] = "#"
        c += 1
    elif grid[p] == ".":
        dp *= -1j
        grid[p] = "W"
    p += dp

print(c)