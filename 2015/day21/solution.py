import re
from itertools import product, combinations, chain
with open('input') as f:
    inp = [x.strip() for x in f.readlines()]

weapons = []
armors = [[0, 0, 0]]
rings = [[0, 0, 0]]

for i, x in enumerate(inp):
    if 1<= i <= 5:
        weapons.append(list(map(int, re.findall('\d+', x))))
    elif 8<= i <= 12:
        armors.append(list(map(int, re.findall('\d+', x))))
    elif 15<= i <= 20:
        rings.append(list(map(int, (re.findall('\d+', x)[1:]))))

boss = [8, 2, 109]
me = [0, 0, 100]

def fight(p1, p2):
    p1c = list(p1)
    p2c = list(p2)
    while p1c[2] > 0 and p2c[2] > 0:
        p2c[2] = p2c[2] - max(p1c[0]-p2c[1], 1)
        if p2c[2] <= 0:
            return True
        p1c[2] = p1c[2] - max(p2c[0]-p1c[1], 1)
        if p1c[2] <= 0:
            return False

costs = []
for w, a, rs in product(range(len(weapons)), range(len(armors)), chain([(0,0)], combinations(range(len(rings)), 2))):
    me = [weapons[w][1]+sum([rings[r][1] for r in rs]), armors[a][2]+sum([rings[r][2] for r in rs]), 100]
    costs.append((weapons[w][0]+armors[a][0]+sum([rings[r][0] for r in rs]), fight(me, boss)))
        
print(min([c[0] for c in costs if c[1]]))
print(max([c[0] for c in costs if not c[1]]))