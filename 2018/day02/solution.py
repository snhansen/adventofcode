from collections import Counter
from itertools import combinations

with open("input") as f:
    inp = f.read().strip().split("\n")


# Part 1
twos, threes = 0, 0
for id_ in inp:
    counts = Counter(id_).values()
    twos += (2 in counts)
    threes += (3 in counts)

print(twos*threes)

# Part 2
for id1, id2 in combinations(inp, 2):
    if sum(l1 != l2 for l1, l2 in zip(id1, id2)) == 1:
        print("".join(c for i, c in enumerate(id1) if c == id2[i]))
        break