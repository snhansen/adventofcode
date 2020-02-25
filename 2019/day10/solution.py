import sys
import math
eps = sys.float_info.epsilon

with open('input') as f:
    inp = [x.strip() for x in f.readlines()]

ps = []
for i, line in enumerate(inp):
    for j, symb in enumerate(line):
        if symb == '#':
            ps.append((j, i))


def is_blocked(a, b, c):
    crossproduct = (c[1] - a[1]) * (b[0] - a[0]) - (c[0] - a[0]) * (b[1] - a[1])

    if abs(crossproduct) > eps:
        return False

    dotproduct = (c[0] - a[0]) * (b[0] - a[0]) + (c[1] - a[1])*(b[1] - a[1])
    if dotproduct < 0:
        return False

    squaredlengthba = (b[0] - a[0])*(b[0] - a[0]) + (b[1] - a[1])*(b[1] - a[1])
    if dotproduct > squaredlengthba:
        return False

    return True


detect = []
for p in ps:
    n = 0
    ps_not_p = [q for q in ps if q not in {p}]
    for q in ps_not_p:
        ps_not_pq = [r for r in ps if r not in {p, q}]
        m = 1
        for r in ps_not_pq:
            if is_blocked(p, q, r):
                m = 0
                break
        n += m
    detect.append(n)
    
# Part 1
print(max(detect))


# Part 2
def angle(p1, p2):
    (dx, dy) = (p2[0]-p1[0], p2[1]-p1[1])
    if dx == 0 and dy < 0:
        angle = 0
    elif dx == 0 and dy > 0:
        angle = 180
    else:
        angle = math.atan(dy/dx)
        if dx >0:
            angle = 90 + angle*180/math.pi
        else:
            angle = 270 + angle*180/math.pi
    return(angle)


def dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


laser = ps[detect.index(max(detect))]
ps_nolaser =  [p for p in ps if p not in {laser}]
angles = list(set([angle(laser, p) for p in ps_nolaser]))
angles.sort()

vaporize = []
i = 0
while True:
    a = angles[i]
    asteroids = [p for p in ps_nolaser if -eps < abs(angle(laser, p) -a) < eps]
    dists = [dist(laser, p) for p in asteroids]
    if len(asteroids):
        x = asteroids[dists.index(min(dists))]
        vaporize.append(x)
        ps_nolaser.remove(x)
    if len(ps_nolaser) == 0:
        break
    i = (i + 1) % len(angles)

print(vaporize[199][0]*100+vaporize[199][1])