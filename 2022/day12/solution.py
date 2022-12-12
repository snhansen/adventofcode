from collections import deque

with open("input") as f:
    inp = f.read().strip().split("\n")

rows = len(inp)
cols = len(inp[0])
grid = {j + i*1j: inp[i][j] for i in range(rows) for j in range(cols)}


def solve(part2 = False):
    to_check = deque()
    for p, c in grid.items():
        if c == "S":
            to_check.append((p, ord("a"), 0))
        if part2 and c == "a":
            to_check.append((p, ord("a"), 0))
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


# Part 1
print(solve())

# Part 2
print(solve(True))