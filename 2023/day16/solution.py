with open("input") as f:
    inp = f.read().strip().split("\n")

grid = {j + i*1j: inp[i][j] for i in range(len(inp)) for j in range(len(inp[0]))}
angles = {
    1: {"-": (1,), "|": (1j, -1j), "/": (-1j,), "\\": (1j,)},
    1j: {"-": (1j, -1j), "|": (1,), "/": (1j,), "\\": (-1j,) },
    -1: {"-": (1,), "|": (1j, -1j), "/": (-1j,), "\\": (1j,) },
    -1j: {"-": (1j, -1j), "|": (1,), "/": (1j,), "\\": (-1j,) }
}


def n_energized(start, dir_):
    seen = set()
    to_check = []
    to_check.append((start, dir_))

    while to_check:
        p, dir_ = to_check.pop(0)
        #print(f"Position {p} in direction {dir_}")
        if p not in grid:
            continue
        if (p, dir_) in seen:
            continue
        seen.add((p, dir_))
        if grid[p] == ".":
            to_check.append((p+dir_, dir_))
        else:
            #print(f"Angles to check: {angles[dir_][grid[p]]}")
            for angle in angles[dir_][grid[p]]:
                new_dir = dir_*angle
                to_check.append((p + new_dir, new_dir))


    return len(set(p for (p, _) in seen))


# Part 1
print(n_energized(0, 1))

# Part 2
m = 0
for i in range(len(inp[0])):
    m = max(m, n_energized(i, 1j))
    m = max(m, n_energized(i + len(inp)*1j, -1j))
for j in range(len(inp)):
    m = max(m, n_energized(j*1j, 1))
    m = max(m, n_energized(len(inp[0]) + j*1j, -11))

print(m)