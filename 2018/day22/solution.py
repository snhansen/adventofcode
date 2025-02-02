from functools import cache
from collections import defaultdict
from heapq import heappop, heappush

depth = 9171
target = (7, 721)

@cache
def geo_index(x, y):
    if (x, y) == target:
        return 0
    if y == 0:
        return x * 16807
    if x == 0:
        return y * 48271
    return erosion_lvl(x - 1, y) * erosion_lvl(x, y - 1)


def erosion_lvl(x, y):
    return ((geo_index(x, y) + depth) % 20183)


def get_type(x, y):
    return erosion_lvl(x, y) % 3


# Part 1
print(sum(get_type(x, y) for x in range(target[0] + 1)  for y in range(target[1] + 1)))

# Part 2
valid_tools = {0: {1, 2}, 1: {0, 1}, 2: {0, 2}} # 0: neither, 1: climbing gear, 2: torch


def get_adjacent(x, y, tool):
    res = []
    type_ = get_type(x, y)
    for (dx, dy) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0:
            continue
        if tool in valid_tools[get_type(nx, ny)]:
            res.append((nx, ny))
    return res


q = [(0, 0, 0, 2)]
best_time = defaultdict(lambda: float("inf"))
while q:
    time, x, y, tool = heappop(q)
    if (x, y) == target and tool == 2:
        print(time)
        break
    if x < 0 or y < 0:
        continue
    to_push = []
    for nx, ny in get_adjacent(x, y, tool):
        to_push.append((time + 1, nx, ny, tool))

    new_tool, = valid_tools[get_type(x, y)] - {tool}
    to_push.append((time + 7, x, y, new_tool))
    
    for (time, x, y, tool) in to_push:
        if time < best_time[(x, y, tool)]:
            heappush(q, (time, x, y, tool))
            best_time[(x, y, tool)] = time