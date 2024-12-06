from copy import copy

with open("input") as f:
    inp = f.read().strip().split("\n")

grid = {j + i*1j: inp[i][j] for i in range(len(inp)) for j in range(len(inp[0]))}

for i, x in grid.items():
    if x == "^":
        guard = i
        grid[i] = "."


def move_guard(grid, guard, dir_):
    visited = set()
    while True:
        if (guard, dir_) in visited:
            loop = 1
            break
        visited.add((guard, dir_))
        next_ = guard + dir_
        if next_ not in grid.keys():
            loop = 0
            break
        if grid[next_] == "#":
            dir_ = dir_*1j
        else:
            guard = next_
    return loop, visited

# Part 1
_, path = move_guard(grid, guard, -1j)
path = {x for x, _ in path}
print(len(path))

# Part 2
ans = 0
for p in path:
    grid_alt = dict(grid)
    grid_alt[p] = "#"
    loop, _ = move_guard(grid_alt, guard, -1j)
    ans += loop

print(ans)