import re

with open("input") as f:
    inp = f.read().strip().split("\n")

ls = []
for line in inp:
    sx, sy, bx, by = map(int, re.findall("-?\d+", line))
    ls.append((sx, sy, bx, by))


def get_x_ranges(y):
    ranges = []
    beacons = set()
    for sx, sy, bx, by in ls:
        dist = abs(sy-by) + abs(sx-bx)
        dx = dist - abs(sy-y)
        if dx > 0:
            ranges.append((sx-dx, sx+dx))
        if by == y:
            beacons.add((bx, by))
    return (ranges, beacons)

# Part 1
ranges, beacons = get_x_ranges(2000000)
res = set().union(*[set(range(x1, x2+1)) for x1, x2 in ranges])
print(len(res)-len(beacons))

# Part 2
def reduce_ranges(ls):
    x1, x2 = ls.pop(0)
    while ls:
        x3, x4 = ls.pop(0)
        if x3 <= x2+1 and x4 >= x1+1:
            x1 = min(x1, x3)
            x2 = max(x2, x4)
        else:
            ls.append((x3, x4))
            break
    ls.append((x1, x2))
    return ls


upper = 4000000
for y in range(0, upper+1):
    ranges, _ = get_x_ranges(y)
    ranges.sort()
    ranges = reduce_ranges(ranges)
    ranges = reduce_ranges(ranges)
    if len(ranges) > 1:
        (_, x2), _ = ranges
        print(x2*4000000 + y)
        break