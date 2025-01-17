import re
from itertools import count

with open("input") as f:
    inp = f.read().strip().split("\n")

points = []
velocities = []
for line in inp:
    px, py, vx, vy = list(map(int, re.findall("-?\d+", line)))
    points.append(px + py*1j)
    velocities.append(vx + vy*1j)


def print_(ps):
    minx = int(min(p.real for p in ps))
    maxx = int(max(p.real for p in ps))
    miny = int(min(p.imag for p in ps))
    maxy = int(max(p.imag for p in ps))
    for y in range(miny, maxy + 1):
        print("".join("#" if x + y*1j in ps else " " for x in range(minx, maxx + 1)))


# We anticipate that the height of the letters is at most 10 pixels.
for t in count():
    points = [p + v for p, v in zip(points, velocities)]
    miny = int(min(p.imag for p in points))
    maxy = int(max(p.imag for p in points))
    if maxy - miny < 10:
        print_(points)
        print(t + 1)
        break