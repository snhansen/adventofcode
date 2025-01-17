import re
from itertools import combinations

with open("input") as f:
    inp = f.read().strip().split("\n")

claims = {}
for line in inp:
    id_, ox, oy, w, h = list(map(int, re.findall("\d+", line)))
    claims[id_] = {
        x + y*1j
        for x in range(ox, ox + w)
        for y in range(oy, oy + h)
    }

# Part 1
res = set()
for cl1, cl2 in combinations(claims.values(), 2):
    res |= cl1 & cl2

print(len(res))

# Part 2
for i, claim in claims.items():
    no_overlap = True
    for j, other_claim in claims.items():
        if i == j:
            continue
        if len(claim & other_claim) > 0:
            no_overlap = False
            break
    if no_overlap:
        print(i)
        break   