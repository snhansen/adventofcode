with open("input") as f:
    inp = f.read().strip().split("\n")

grid = {x + y*1j: c for y, line in enumerate(inp) for x, c in enumerate(line)}


def accessible_rolls(grid):
    dirs = [1, -1, 1j, -1j, 1+1j, 1-1j, -1+1j, -1-1j]
    res = []
    for p in grid:
        if grid[p] == ".":
            continue
        rolls = 0
        for dp in dirs:
            if p + dp in grid and grid[p + dp] == "@":
                rolls += 1
        if rolls < 4:
            res.append(p)

    return res


# Part 1
print(len(accessible_rolls(grid)))


# Part 2
def update_grid(grid):
    ps = accessible_rolls(grid)
    for p in ps:
        grid[p] = "."

    return len(ps), grid


ans = 0
while True:
    n, grid = update_grid(grid)
    ans += n
    if n == 0:
        break

print(ans)