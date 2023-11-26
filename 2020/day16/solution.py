import re
import math
with open('input') as f:
    inp = f.read().splitlines()

ranges = []
tickets = []
write_ranges, write_tickets, write_my = True, False, False
for x in inp:
    if x == '':
        write_ranges, write_my, write_tickets = False, False, False
    if write_ranges:
        ranges.append(list(map(int, re.findall('\d+', x))))
    if write_my:
        my = list(map(int, x.split(',')))
    if write_tickets:
        tickets.append(list(map(int, x.split(','))))
    if 'your ticket' in x:
        write_my = True
    if 'nearby tickets' in x:
        write_tickets = True

# Part 1
invalid_ts = []
ans = 0

for t in tickets:
    for num in t:
        valid = False
        for r in ranges:
            if r[0] <= num <= r[1] or r[2] <= num <= r[3]:
                valid = True
                break
        if not valid:
            ans += num
            invalid_ts.append(t)
print(ans)

# Part 2
tickets = [t for t in tickets if t not in invalid_ts]

def does_comply(ranges, col):
    ls = []
    for i, r in enumerate(ranges):
        valid = True
        for c in col:
            if not (r[0] <= c <= r[1] or r[2] <= c <= r[3]):
                valid = False
        if valid:
            ls.append(i)
    return ls
             
d_comply = {i : does_comply(ranges, [t[i] for t in tickets]) for i in range(len(tickets[0]))}

used = set()
for c in sorted(d_comply, key = lambda l: len(d_comply[l])):
    for x in used:
        d_comply[c].remove(x)
    used = used.union(d_comply[c])
    
print(math.prod([my[i] for i in sorted(d_comply, key = lambda l: d_comply[l][0])[:6]]))