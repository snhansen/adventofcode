with open("input") as f:
    inp = f.read().strip().split("\n")

rows = len(inp)
cols = len(inp[0])
grid = {i + j * 1j: int(inp[i][j]) for i in range(rows) for j in range(cols)}

# Part 1
def is_visible(p):
    if (p.imag == 0) or (p.real == 0) or (p.imag == rows) or (p.real == cols):
        return True
    for dir in (-1, 1, 1j, -1j):
        to_check = (p + dir*k for k in range(1, max(rows, cols)) if p + dir*k in grid)
        if all(grid[tree] < grid[p] for tree in to_check):
            return True
    return False


print(sum(is_visible(p) for p in grid))

# Part 2
def scenic_core(p):
    res = 1
    for dir in (-1, 1, 1j, -1j):
        for k in range(1, max(rows, cols)):
            p_new = p + dir*k
            if p_new not in grid:
                k -= 1
                break
            if grid[p_new] >= grid[p]:
                break
        res *= k
    return res

print(max(scenic_core(p) for p in grid))