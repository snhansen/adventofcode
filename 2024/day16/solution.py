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
    for ddp in (1j, -1j):
        new_dp = dp * ddp
        if score + 1000 < scores[(p, new_dp)]:
            scores[(p, new_dp)] = score + 1000
            previous[(p, new_dp)] = {(p, dp)}
            heappush(q, (score + 1000, make_id(), p, new_dp))
        elif score + 1000 == scores[(p, new_dp)]:
            previous[(p, new_dp)].add((p, dp))
    new_p = p + dp
    if new_p not in grid.keys():
        continue
    if grid[new_p] == ".":
        if score + 1 < scores[(new_p, dp)]:
            scores[(new_p, dp)] = score + 1
            previous[(new_p, dp)] = {(p, dp)}
            heappush(q, (score + 1, make_id(), new_p, dp))
        elif score + 1 == scores[(new_p, dp)]:
            previous[(new_p, dp)].add((p, dp))

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