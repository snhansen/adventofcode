from collections import deque
import networkx as nx
from itertools import permutations

with open("input") as f:
    inp = f.read().strip().split("\n")

nums = {j + i*1j: int(x) for i, l in enumerate(inp) for j, x in enumerate(l) if x.isdigit()}
rev_nums = {num: p for p, num in nums.items()}
opens = {j + i*1j for i, l in enumerate(inp) for j, x in enumerate(l) if x != "#"}


def get_distances(num):
    res = {}
    seen = set()
    q = deque([(rev_nums[num], 0)])
    other_nums = set(p for p, num2 in nums.items() if num2 != num)
    while q:
        p, steps = q.popleft()
        if p in other_nums:
            if nums[p] not in res:
                res[nums[p]] = steps
            res[nums[p]] = min(steps, res[nums[p]])
            continue
        if p in seen:
            continue
        seen.add(p)
        for dp in (1, -1, 1j, -1j):
            new_p = p + dp
            if new_p not in opens:
                continue
            q.append((new_p, steps + 1))            
    return res


g = nx.Graph()
for num in range(8):
    for other_num, steps in get_distances(num).items():
        g.add_edge(num, other_num, weight = steps)


def steps(route):
    res = 0
    for n1, n2 in zip([0] + route, route):
        if (n1, n2) not in g.edges():
            return None
        res += g[n1][n2]["weight"]
    return res


paths = []
for route in permutations(range(1, 8), 7):
    route = list(route)
    res = steps(route)
    if res is not None:
        paths.append((res, g[route[-1]][0]["weight"]))

# Part 1
print(min(path for path, _ in paths))

# Part 2
print(min(path + return_ for path, return_ in paths))