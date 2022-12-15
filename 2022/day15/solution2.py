import re
from collections import defaultdict

with open("input") as f:
    inp = f.read().strip().split("\n")

ls = []
for line in inp:
    sx, sy, bx, by = map(int, re.findall("-?\d+", line))
    ls.append((sx, sy, bx, by))


def get_y_range(sx, sy, bx, by, y):
    dist = abs(sy-by) + abs(sx-bx)
    dx = max(dist - abs(sy - y), 0)
    return set(range(sx-dx, sx+dx+1))

res = set()
beacons = set()
y = 2000000
# y = 10
for sx, sy, bx, by in ls:
    res = res.union(get_y_range(sx, sy, bx, by, y))
    if by == y:
        beacons.add(bx)

print(len(beacons))
print(len(res))
print(len(res - beacons))





    
