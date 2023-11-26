from collections import deque

with open("input") as f:
    inp = f.read().strip().split("\n")


points = [tuple(map(int, line.split(","))) for line in inp]
dirs = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]

# Part 1
res = 0
for p in points:
    for dp in dirs:
        new_p = tuple(c+dc for (c, dc) in zip(p, dp))
        if new_p not in points:
            res += 1

print(res)

# Part 2
maxs = list(map(max, [[p[i] for p in points] for i in range(3)]))
mins = list(map(min, [[p[i] for p in points] for i in range(3)]))


def out_of_bounds(p):
    return any(p[i] < mins[i]-1 or p[i] > maxs[i]+1 for i in range(3))


# We create coordinates of the exterior space starting at a corner.
ext = set()
seen = set()
to_check = deque()
to_check.append((mins[0], mins[1], mins[2]))
while to_check:
    p = to_check.popleft()
    if p in seen:
        continue
    seen.add(p)
    if out_of_bounds(p):
        continue
    if p not in points:
        ext.add(p)
        for dp in dirs:
            to_check.append(tuple(c+dc for (c, dc) in zip(p, dp)))

# Then we check which sides are exposed to the exterior.
sides = [(p, d) for p in points for d in dirs]
print(sum(tuple(c+dc for (c, dc) in zip(p, dp)) in ext for p, dp in sides))