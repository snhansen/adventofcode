with open("input") as f:
    inp = f.read().strip().split()

grid = {j+i*1j: inp[i][j] for i in range(len(inp)) for j in range(len(inp[0]))}
start_grid = dict(grid)
n_col = len(inp[0])
n_row = len(inp)


def print_(grid):
    for i in range(n_row):
        print("".join([grid[j+i*1j] for j in range(n_col)]))


def open_spaces(grid, p, dir_):
    ans = 0
    k = 1
    while True:
        new_p = p + k*dir_
        if new_p not in grid.keys():
            return ans
        if grid[new_p] == "#":
            return ans
        ans += int(grid[new_p] == ".")
        k += 1


def tilt(grid, dir_):
    new_grid = {p: (x if x != "O" else ".") for p, x in grid.items()}
    for p, c in grid.items():
        if c != "O":
            continue
        n = open_spaces(grid, p, dir_)
        new_grid[p+n*dir_] = "O"
    return new_grid


def total_load(grid):
    ans = 0
    for p, c in grid.items():
        if c == "O":
            ans += n_row-int(p.imag)
    return ans

# Part 1
print(total_load(tilt(grid, -1j)))

# Part 2
def cycle(grid, n):
    new_grid = dict(grid)
    for _ in range(n):
        for dir_ in dirs:
            new_grid = tilt(new_grid, dir_)
    return new_grid


dirs = [-1j, -1, 1j, 1]
seen = []
seen.append(grid)
while True:
    grid = cycle(grid, 1)
    if grid in seen:
        break
    seen.append(dict(grid))

n_cycles = 1_000_000_000
k = seen.index(grid)
cycle_length = len(seen) - k
m = (n_cycles - k) % cycle_length + k
print(total_load(seen[m]))