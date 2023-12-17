from heapq import heappop, heappush
from collections import defaultdict

with open("input") as f:
    inp = f.read().strip().split("\n")
    
grid = {j + i*1j: int(inp[i][j]) for i in range(len(inp)) for j in range(len(inp[0]))}
corner = (len(inp[0]) - 1) + (len(inp) - 1)*1j

# Part 1

# state = (heat, id, position, direction_moved, moved_blocks)
q = [(grid[p], id(p), p, p, 1) for p in [1, 1j]]
min_heat = defaultdict(lambda: float("inf"))

while q:
    heat, _, p, dp, blocks = heappop(q)
    if p == corner:
        print(heat)
        break
    to_push = []
    dirs = [dp*1j, -dp*1j]
    # Turn.
    for new_dp in dirs:
        new_p = p + new_dp
        if new_p in grid:
            to_push.append((heat + grid[new_p], new_p, new_dp, 1))
    # If moved less than 3 blocks we can continue in the same direction.
    if blocks < 3:
        new_p = p + dp
        if new_p in grid:
            to_push.append((heat + grid[new_p], new_p, dp, blocks + 1))
    # Add all states to queue if heat is lower.
    for (heat, p, dp, blocks) in to_push:
        if heat < min_heat[(p, dp, blocks)]:
            heappush(q, (heat, id(p), p, dp, blocks))
            min_heat[(p, dp, blocks)] = heat


# Part 2

# state = (heat, id, position, direction_moved, moved_blocks)
q = [(grid[p], id(p), p, p, 1) for p in [1, 1j]]
min_heat = defaultdict(lambda: float("inf"))

while q:
    heat, _, p, dp, blocks = heappop(q)
    if (p == corner) & (blocks >= 4):
        print(heat)
        break
    to_push = []
    # If moved less than 10 block we can continue in the same direction.
    if blocks < 10:
        new_p = p + dp
        if new_p in grid:
            to_push.append((heat + grid[new_p], new_p, dp, blocks + 1))
    # If moved at least 4 blocks, we can turn.
    if blocks >= 4:
        dirs = [dp*1j, -dp*1j]
        for new_dp in dirs:
            new_p = p + new_dp
            if new_p in grid:
                to_push.append((heat + grid[new_p], new_p, new_dp, 1))
    # Add all states to queue if heat is lower.
    for (heat, p, dp, blocks) in to_push:
        if heat < min_heat[(p, dp, blocks)]:
            heappush(q, (heat, id(p), p, dp, blocks))
            min_heat[(p, dp, blocks)] = heat