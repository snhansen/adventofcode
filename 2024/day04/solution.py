with open("input") as f:
    inp = f.read().strip().split("\n")

grid = {j + i*1j: inp[i][j] for i in range(len(inp)) for j in range(len(inp[0]))}


def get_substr(p, dir_, length):
    res = grid[p]
    for dp in range(length-1):
        if (p + (dp+1)*dir_) not in grid.keys():
            return False
        res += grid[p + (dp+1)*dir_]
    return res


# Part 1
dirs = [1, -1, 1j, -1j, 1+1j, 1-1j, -1+1j, -1-1j]
print(sum(get_substr(p, dir_, 4) == "XMAS" for dir_ in dirs for p in grid.keys()))

# Part 2
def is_crossmas(p):
    if grid[p] != "A":
        return False
    dirs = {-1-1j: 1+1j, 1+1j: -1-1j, -1+1j: 1-1j, 1-1j: -1+1j}
    n_mas = 0
    for dir_, opp in dirs.items():
        if p+dir_ not in grid.keys():
            return False
        n_mas += get_substr(p+dir_, opp, 3) == "MAS"
        if n_mas == 2:
            return True
    return False

print(sum(is_crossmas(p) for p in grid.keys()))