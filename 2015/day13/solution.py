from itertools import permutations
from collections import defaultdict

with open('input') as f:
    inp = [x.strip() for x in f.readlines()]

change = defaultdict(dict)

for x in inp:
    if 'lose' in x:
        change[x.split(' ')[0]][x.split(' ')[10].strip('.')] = -int(x.split(' ')[3])
    else:
        change[x.split(' ')[0]][x.split(' ')[10].strip('.')] = int(x.split(' ')[3])

def get_change(s):
    h = 0
    for i, p in enumerate(s):
        h += change[p][s[(i-1) % len(s)]]
        h += change[p][s[(i+1) % len(s)]]
    return h

# Part 1
max_change = -float('inf')
for seat in permutations(list(change.keys())):
    max_change = max(max_change, get_change(seat))

print(max_change)

# Part 2
for p in list(change.keys()):
    change['me'][p] = 0
    change[p]['me'] = 0

max_change = -float('inf')
for seat in permutations(list(change.keys())):
    max_change = max(max_change, get_change(seat))

print(max_change)
