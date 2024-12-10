from collections import deque

with open("input") as f:
    inp = f.read().strip().split("\n")

grid = {j + i*1j: int(x) for i, l in enumerate(inp) for j, x in enumerate(l)}

heads = []
for p, height in grid.items():
    if height == 0:
        heads.append(p)

dests = []
for p in heads:
    q = deque([(p, 0, {p})])
    p_dests = []
    while q:
        p, height, seen = q.pop()
        if height == 9:
            p_dests.append(p)
        for dp in [1, -1, 1j, -1j]:
            new_p = p + dp
            if new_p not in grid.keys() or new_p in seen:
                continue
            if grid[new_p] == height + 1:
                q.append((new_p, height + 1, seen | {new_p}))
    dests.append(p_dests)


# Part 1
print(sum(map(len, map(set, dests))))

# Part 2
print(sum(map(len, dests)))