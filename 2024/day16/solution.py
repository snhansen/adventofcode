from heapq import heappop, heappush
from collections import defaultdict
import uuid

with open("input") as f:
    inp = f.read().strip().split("\n")

grid = {j + i*1j: x for i, l in enumerate(inp) for j, x in enumerate(l)}

for p, c in grid.items():
    if c == "S":
        start = p
        grid[p] = "."
    if c == "E":
        end = p
        grid[p] = "."


def make_id():
    return str(uuid.uuid4().fields[-1])[:20]


scores = defaultdict(lambda: float("inf"))
previous = defaultdict(set)
best_score = float("inf")

q = [(0, make_id(), start, 1)]
while q:
    score, _, p, dp = heappop(q)
    if score > best_score:
        break
    if p == end:
        best_score = score
    new_ps = [p, p]
    new_dps = [1j*dp, -1j*dp]
    costs = [1000, 1000]
    if p + dp in grid.keys() and grid[p + dp] == ".":
        new_ps.append(p + dp)
        new_dps.append(dp)
        costs.append(1)
    for new_p, new_dp, cost in zip(new_ps, new_dps, costs):
        if score + cost <= scores[(new_p, new_dp)]:
            scores[(new_p, new_dp)] = score + cost
            previous[(new_p, new_dp)] |= {(p, dp)}
            heappush(q, (score + cost, make_id(), new_p, new_dp))

# Part 1
print(best_score)

# Part 2
to_check = set()
for (p, dp) in previous.keys():
    if p == end:
        to_check.add((p, dp))

best_paths = set()
while to_check:
    p, dp = to_check.pop()
    if (p, dp) in best_paths:
        continue
    best_paths.add((p, dp))
    to_check |= previous[(p, dp)]

print(len(set([p for p, _ in best_paths])))