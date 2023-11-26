from itertools import combinations

with open('input') as f:
    inp = list(map(int, f.readlines()))

# Part 1
i = 25
while True:
    valid = False
    for x in combinations(inp[i-25:i], 2):
        if inp[i] == sum(x):
            valid = True
    if not valid:
        inv = inp[i]
        break
    i += 1

print(inv)

# Part 2
for i in range(len(inp)):
    for j in range(i+1, len(inp)):
        ls = inp[i:j+1]
        if sum(ls) > inv:
            break
        if sum(ls) == inv:
            print(min(ls)+max(ls))