import re
from itertools import count

with open("input") as f:
    inp = f.read().strip()

discs = []
for line in inp.split("\n"):
    nums = list(map(int, re.findall("\d+", line)))
    nums.pop(2)
    discs.append(tuple(nums))


def solve(part2 = False):
    if part2:
        discs.append((len(discs) + 1, 11, 0))
    for t in count():
        if all((init_pos + t + disc) % n == 0 for disc, n, init_pos in discs):
            return t


# Part 1
print(solve())

# Part 2
print(solve(True))