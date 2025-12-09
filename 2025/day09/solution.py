from itertools import combinations
from shapely.geometry.polygon import Polygon, LineString

with open("input") as f:
    inp = f.read().strip().split("\n")

coords = [(x, y) for x, y in (map(int, line.split(",")) for line in inp)]

# Part 1
print(
    max(
        (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        for (x1, y1), (x2, y2) in combinations(coords, 2)
    )
)

# Part 2
polygon = Polygon(coords)
ans = 0

for (x1, y1), (x2, y2) in combinations(coords, 2):
    p1 = (x1, y1)
    p2 = (x2, y2)
    p3 = (x1, y2)
    p4 = (x2, y1)
    lines = [LineString([p1, p3]), LineString([p1, p4]), LineString([p3, p2]), LineString([p2, p4])]
    if all(line.covered_by(polygon) for line in lines):
        ans = max(ans, (abs(x1 - x2) + 1)*(abs(y1 - y2) + 1))

print(ans)