import re
import networkx as nx

with open("input") as f:
    inp = f.read().strip().split("\n")

positions = []
velocities = []
for line in inp:
    x, y, dx, dy = map(int, re.findall("-?\d+", line))
    positions.append((x, y))
    velocities.append((dx, dy))

height, width = 103, 101


def move(ps, vs, t):
    res = []
    for (x, y), (dx, dy) in zip(ps, vs):
        xend = (x + dx*t) % width
        yend = (y + dy*t) % height
        res.append((xend, yend))
    return res


# Part 1
positions_end = move(positions, velocities, 100)
q1 = sum([1 for x, y in positions_end if x < width//2 and y < height//2])
q2 = sum([1 for x, y in positions_end if x > width//2 and y < height//2])
q3 = sum([1 for x, y in positions_end if x < width//2 and y > height//2])
q4 = sum([1 for x, y in positions_end if x > width//2 and y > height//2])
print(q1*q2*q3*q4)

# Part 2
def largest_component(ps):
    g = nx.Graph()
    for (x, y) in ps:
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if (x + dx, y + dy) in ps:
                g.add_edge((x, y), (x + dx, y + dy))
    return max(map(len, nx.connected_components(g)))


def print_(ps):
    for y in range(height):
        print("".join("#" if (x, y) in ps else " " for x in range(width)))


t = 0
while True:
    positions_end = move(positions, velocities, t)
    if largest_component(move(positions, velocities, t)) > 20:
        print_(positions_end)
        print(t)
        break
    t += 1