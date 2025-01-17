from collections import defaultdict

with open("input") as f:
    inp = f.read().strip().split("\n")

coords = [tuple(map(int, line.split(","))) for line in inp]

# Part 1
minx = min(x for x, _ in coords)
maxx = max(x for x, _ in coords)
miny = min(y for _, y in coords)
maxy = max(y for _, y in coords)

regions = defaultdict(set)
for x in range(minx, maxx + 1):
    for y in range(miny, maxy + 1):
        dists = [(abs(x - cx) + abs(y - cy), (cx, cy)) for (cx, cy) in coords]
        dists = sorted(dists)
        (d1, (c1x, c1y)), (d2, (c2x, c2y)) = dists[0], dists[1]
        if d1 != d2:
            regions[(c1x, c1y)].add((x, y))

corners = []
left = sorted([(cx, cy) for cx, cy in regions.keys() if cx == minx])
right = sorted([(cx, cy) for cx, cy in regions.keys() if cx == maxx])
corners = [left[0], left[-1], right[0], right[-1]]

print(max(len(region) for c, region in regions.items() if c not in corners))

# Part 2
total_dist = 10000

region = set()
for x in range(minx - total_dist // len(coords), maxx + total_dist // len(coords)):
    for y in range(miny - total_dist // len(coords), maxy + total_dist // len(coords)):
        if sum(abs(x - cx) + abs(y - cy) for cx, cy in coords) < total_dist:
            region.add((x, y))

print(len(region))