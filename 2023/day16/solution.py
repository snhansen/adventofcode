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
        p, dir_ = to_check.pop()
        if p not in grid:
            continue
        if (p, dir_) in seen:
            continue
        seen.add((p, dir_))
        if grid[p] == ".":
            to_check.append((p+dir_, dir_))
        else:
            for angle in angles[dir_][grid[p]]:
                new_dir = dir_*angle
                to_check.append((p + new_dir, new_dir))


    return len(set(p for (p, _) in seen))


# Part 1
print(n_energized(0, 1))

# Part 2
r, c = len(inp[0]), len(inp)
starts = [(i + k*c*1j, 1j*(k==0)) for i in range(r) for k in range(2)]
starts += [(k*r + j*1j, -1*(k==0)) for j in range(c) for k in range(2)]

print(max(n_energized(*start) for start in starts))