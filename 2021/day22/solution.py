import re
from itertools import product
from tqdm import tqdm


with open('input') as f:
    inp = f.read().strip().split('\n')


coords = []
onoff = []

for line in inp:
    onoff.append((int(re.search('[a-z]+', line).group() == 'on')))
    coords.append(list(map(int, re.findall('-?\d+', line))))

xs, ys, zs = set(), set(), set()
for c in coords:
    xmin, xmax, ymin, ymax, zmin, zmax = c
    xs.add(xmin)
    xs.add(xmax+1)
    ys.add(ymin)
    ys.add(ymax+1)
    zs.add(zmin)
    zs.add(zmax+1)

# Inspired by the solution of Jonathan Paulson (https://github.com/jonathanpaulson/AdventOfCode/blob/master/2021/22.py)
# We compress the coordinate system, so that, for every axis, there is a one-unit distance between used values (from the input) after sorting them. We then store the distances between successive coordinates in a dictionary (first value is the distance between the first pair, second value is the distance between the second pair, etc.)

def compress(ps): 
    ps = sorted(list(ps))
    val = {}
    conversion = {}
    for i in range(len(ps)):
        conversion[ps[i]] = i
        if i >= 1:
            val[i-1] = ps[i] - ps[i-1] 
    return conversion, val


xs, xvals = compress(xs)
ys, yvals = compress(ys)
zs, zvals = compress(zs)


def solve(part2 = False):
    points = set()
    for c, instr in tqdm(zip(coords, onoff)):
        xmin, xmax, ymin, ymax, zmin, zmax = c
        if not part2:
            if xmin < -50 or xmax > 50 or ymin < -50 or ymax > 50 or zmin < -50 or zmax > 50:
                continue
        for x, y, z in product(range(xs[xmin], xs[xmax+1]), range(ys[ymin], ys[ymax+1]), range(zs[zmin], zs[zmax+1])):        
            if instr:
                points.add((x, y, z))
            else:
                points.discard((x, y, z))
    volume = 0
    for x, y, z in tqdm(points):
        volume += xvals[x]*yvals[y]*zvals[z]

    return volume
    
# Part 1
print(solve(False))

# Part 2
print(solve(True))
            




