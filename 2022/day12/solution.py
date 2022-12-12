from collections import deque

with open("input") as f:
    inp = f.read().strip().split("\n")

rows = len(inp)
cols = len(inp[0])
grid = {j + i*1j: inp[i][j] for i in range(rows) for j in range(cols)}


def solve(grid):
    start = [p for p, c in grid.items() if c == "S"][0]
    to_check = deque()
    to_check.append((start, ord("a"), 0))
    seen = {}
    while to_check:
        p, elev, steps = to_check.popleft()
        if p in seen and seen[p] <= steps:
            continue
        seen[p] = steps
        if grid[p] == "E":
            return steps
        for dp in [1, -1, 1j, -1j]:
            if p + dp not in grid:
                continue
            new_elev = grid[p + dp]
            new_elev = ord(new_elev) if new_elev.islower() else ord("z")
            if elev + 1 >= new_elev:
                to_check.append((p + dp, new_elev, steps + 1))
    return None


# Part 1
ans = solve(grid)
print(ans)

# Part 2
start = [p for p, c in grid.items() if c == "S"][0]
m = ans
for p, c in grid.items():
    if c == "a":
        grid_cp = dict(grid)
        grid_cp[p] = "S"
        grid_cp[start] = "a"
        res = solve(grid_cp)
        if res:
            m = min(m, res)

print(m)