with open("input") as f:
    inp = f.read()


grid = {}
i, j = 0, 0
for c in inp:
    if c == "\n":
        j += 1
        i = 0
    else:
        grid[i+j*1j] = int(c)
        i += 1

n = int(len(grid)**(0.5))

# Part 1
def is_visible(p):
    if (p.imag == 0) or (p.real == 0) or (p.imag == n) or (p.real == n):
        return True
    for dir in [-1, 1, 1j, -1j]:
        trees = [p + dir*k for k in range(1, n) if p+dir*k in grid]
        if all(grid[tree] < grid[p] for tree in trees):
            return True
    return False


print(sum(is_visible(p) for p in grid))

# Part 2
def scenic_core(p):
    res = 1
    for dir in [-1, 1, 1j, -1j]:
        for k in range(1, n):
            p_new = p + dir*k
            if p_new not in grid:
                k -= 1
                break
            if grid[p_new] >= grid[p]:
                break
        res *= k
    return res

print(max(scenic_core(p) for p in grid))