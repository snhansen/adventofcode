import re
import string
import itertools
from collections import defaultdict

with open("input") as f:
    inp = f.read().strip().split("\n")

symbols = [sym for sym in string.punctuation + string.whitespace if sym != "."]
numbers = []
gears = defaultdict(set)

for y, line in enumerate(inp):
    matches = re.finditer("\d+", line)
    for match in matches:
        number = match.group()
        valid = False
        for x in range(match.start(), match.end()):
            for dx, dy in itertools.product((-1, 0, 1), (-1, 0, 1)):
                if x+dx < 0 or x+dx >= len(inp) or y+dy < 0 or y+dy >= len(inp):
                    continue
                if inp[y+dy][x+dx] in symbols:
                    valid = True
                    if inp[y+dy][x+dx] == "*":
                        gears[(x+dx, y+dy)].add(int(number))
        if valid:
            numbers.append(int(number))

# Part 1
print(sum(numbers))

# Part 2
res = 0
for gear in gears.values():
    gear = list(gear)
    if len(gear) == 2:
        res += gear[0]*gear[1]

print(res)