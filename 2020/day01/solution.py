from itertools import combinations

with open('input') as f:
    inp = list(map(int, f.readlines()))

# Part 1
for x, y in combinations(inp, 2):
    if x + y == 2020:
        print(x*y)
        break

# Part 2
for x, y, z in combinations(inp, 3):
    if x + y + z == 2020:
        print(x*y*z)
        break
        