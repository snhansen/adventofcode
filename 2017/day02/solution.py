from itertools import permutations
import re

with open("input") as f:
    inp = f.read().strip().split("\n")

rows = [list(map(int, re.findall("\d+", line))) for line in inp]

# Part 1
print(sum(max(row) - min(row) for row in rows))

# Part 2
ans = 0
for row in rows:
    for x, y in permutations(row, 2):
        if x % y == 0:
            ans += x // y
            break
print(ans)