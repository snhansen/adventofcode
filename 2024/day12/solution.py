from collections import deque

with open("input") as f:
    inp = f.read().strip().split("\n")

grid = {j + i*1j: x for i, l in enumerate(inp) for j, x in enumerate(l)}


def get_region(p):
    q = deque([p])
    region = set()
    while q:
        p = q.pop()
        region.add(p)
        for dp in [1, -1, 1j, -1j]:
            if p + dp in region or p + dp not in grid.keys() or grid[p] != grid[p + dp]:
                continue
            q.append(p + dp)
    return region


regions = []
to_check = set(grid.keys())
while to_check:
    p = to_check.pop()
    region = get_region(p)
    regions.append(region)
    to_check -= region

# Part 1
areas = [len(region) for region in regions]

perimeters = []
for region in regions:
    perimeter = 0
    for p in region:
        for dp in [1, -1, 1j, -1j]:
            if p + dp not in region:
                perimeter += 1
    perimeters.append(perimeter)

print(sum(x*y for x, y in zip(areas, perimeters)))

# Part 2
def n_corners(region):
    ans = 0
    for p in region:
        if p - 1 not in region and p - 1j not in region:
            ans += 1
        if p + 1 not in region and p - 1j not in region:
            ans += 1
        if p - 1 not in region and p + 1j not in region:
            ans += 1
        if p + 1 not in region and p + 1j not in region:
            ans += 1
        if p - 1 in region and p - 1j in region and p - 1 - 1j not in region:
            ans += 1
        if p + 1 in region and p - 1j in region and p + 1 - 1j not in region:
            ans += 1
        if p - 1 in region and p + 1j in region and p - 1 + 1j not in region:
            ans += 1
        if p + 1 in region and p + 1j in region and p + 1 + 1j not in region:
            ans += 1
    return ans

sides = [n_corners(region) for region in regions]
print(sum(x*y for x, y in zip(areas, sides)))