from itertools import product, combinations

raw = open('input').read().strip().split('\n\n')

ls = []
for line in raw:
    _, *rest = line.split('\n')
    subls = []
    for l in rest:
        x, y, z = map(int, l.split(','))
        subls.append((x, y, z))
    ls.append(subls)
   
   
def matches(ls1, ls2):
    ls1_set = set(ls1)
    do_break = False
    for x1, y1, z1 in ls1:
        for x2, y2, z2 in ls2:
            dx, dy, dz = x1-x2, y1-y2, z1-z2
            ls2_moved = [(x+dx, y+dy, z+dz) for x, y, z in ls2]
            if len(ls1_set&set(ls2_moved)) >= 12:
                do_break = True
                break
        if do_break:
            return True, ls2_moved, (dx, dy, dz)
            
    return False, None, None
            
 
def get_transformations(ls):
    res = []
    for k1, k2, k3 in product([-1, 1], repeat=3):
        res.append([(x*k1, y*k2, z*k3) for x, y, z in ls])
        res.append([(x*k1, z*k2, y*k3) for x, y, z in ls])
        res.append([(y*k1, x*k2, z*k3) for x, y, z in ls])
        res.append([(y*k1, z*k2, x*k3) for x, y, z in ls])
        res.append([(z*k1, y*k2, x*k3) for x, y, z in ls])
        res.append([(z*k1, x*k2, y*k3) for x, y, z in ls])
    return res


def manhattan(p1, p2):
    return sum(abs(c1-c2) for c1, c2 in zip(p1, p2))


finished = []
finished.append((ls.pop(0), 0, (0, 0, 0)))

while ls:
    next = ls.pop(0)
    configs = get_transformations(next)
    stop = False
    for config in configs:
        for i, (target, _, _) in enumerate(finished):
            match, points, dist = matches(target, config)
            if match:
                stop = True
                break
        if stop:
            break
    if stop:
        finished.append((points, i, dist))
    else:
        ls.append(next)

# Part 1
beacons = set()
for x, *_ in finished:
    for y in x:
        beacons.add(y)

print(len(beacons))

# Part 2
scanners = [(x,y,z) for _, _, (x,y,z) in finished]
max_dist = 0
for p1, p2 in combinations(scanners, 2):
    dist = manhattan(p1, p2)
    max_dist = max(dist, max_dist)

print(max_dist)