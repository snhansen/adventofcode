import re

with open("input") as f:
    inp = f.read().strip().split("\n")

clay = set()
still = set()
flowing = set()

for line in inp:
    nums = list(map(int, re.findall("\d+", line)))
    if line[0] == "x":
        for y in range(nums[1], nums[2] + 1):
            clay.add(nums[0] + y*1j)
    else:
        for x in range(nums[1], nums[2] + 1):
            clay.add(x + nums[0]*1j)

ymax = int(max(p.imag for p in clay))
ymin = int(min(p.imag for p in clay))


def drop(p, add_flowing = False):
    while True:
        if add_flowing and ymin <= p.imag <= ymax:
            flowing.add(p)
        if p + 1j in clay | still or p.imag >= ymax:
            return p
        p += 1j


def wall_or_edge(p, dp):
    while p + 1j in clay | still:
        if p + dp in clay:
            return 0, p
        p += dp
    return 1, p - dp


def add_water(p, q, type_):
    dp = 1 if q.real > p.real else -1
    while p != q + dp:
        type_.add(p)
        p += dp


ps = [500]
seen = set()
while ps:
    p = ps.pop()
    if p in seen:
        continue
    seen.add(p)
    # We drop until we reach clay or still water.
    # We don't add the stream to flowing water for now as
    # this complicates matters. We do this at the end instead.
    p = drop(p)
    if int(p.imag) == ymax:
        continue
    while True:
        # Check if there is a wall or edge at both sides.
        left, left_p = wall_or_edge(p, -1)
        right, right_p = wall_or_edge(p, 1)
        # Walls at both sides means that water is still
        # and we move up on block and continue.
        if left == 0 and right == 0: 
            add_water(left_p, right_p, still)
            p -= 1j
            continue
        # Else, there's at least one edge and so 
        # the water is flowing in both directions
        add_water(left_p, p, flowing)
        add_water(right_p, p, flowing)
        # .. and if there's not a wall, we add the edge as
        # a new point from which water should flow.
        if left == 1:
            ps.append(left_p - 1)
        if right == 1:
            ps.append(right_p + 1)
        break

# Lastly, we add all the vertical flowing water.
for p in seen:
    drop(p, add_flowing = True)

# Part 1
print(len(still | flowing))

# Part 2
print(len(still))

# Visualisation
xmin = int(min(p.real for p in clay)) - 2
xmax = int(max(p.real for p in clay)) + 2
for y in range(ymin, ymax + 1):
    res = ""
    for x in range(xmin, xmax + 1):
        p = x + y*1j
        if p in clay:
            c = "#"
        elif p in still:
            c = "~"
        elif p in flowing:
            c = "|"
        else:
            c = "."
        res += c
    print(res)