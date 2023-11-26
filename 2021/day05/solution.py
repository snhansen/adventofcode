import re
from collections import defaultdict

with open('input') as f:
    inp = [x.strip() for x in f.readlines()]


corners = []
for line in inp:
    x1, y1, x2, y2 = map(int, re.findall('\d+', line))
    corners.append([(x1, y1), (x2, y2)])

def get_points(ps):
    p1, p2 = ps
    if p1[0] == p2[0]:
        return 0, [(p1[0], x) for x in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1)]
    elif p1[1] == p2[1]:
        return 0, [(x, p1[1]) for x in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1)]
    else:
        x1s = range(p1[0], p2[0]+1) if p1[0]<p2[0] else reversed(range(p2[0], p1[0]+1))
        x2s = range(p1[1], p2[1]+1) if p1[1]<p2[1] else reversed(range(p2[1], p1[1]+1))
        return 1, list(zip(x1s, x2s))
    
# Part 1 + 2
counts_pt1, counts_pt2 = defaultdict(int), defaultdict(int)

for c in corners:
    diag, ps = get_points(c)
    for p in ps:
        if not diag:
            counts_pt1[p] += 1
        counts_pt2[p] += 1

print(len([x for x in counts_pt1 if counts_pt1[x] > 1]))
print(len([x for x in counts_pt2 if counts_pt2[x] > 1]))