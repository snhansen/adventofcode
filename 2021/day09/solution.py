from collections import defaultdict

with open('input') as f:
    inp = [x.strip() for x in f.readlines()]

area = defaultdict(lambda: 10)

for i, x in enumerate(inp):
    for j, y in enumerate(x):
        area[(j+1j*i)] = int(y)

# Part 1
lows = [x for x in dict(area) if all(area[x] < area[x+pos] for pos in [-1, 1, -1j, 1j])]
print(sum(area[x]+1 for x in lows))

# Part 2
bassins = []

for low in lows:
    bassin = set()
    bassin.add(low)  
    while True:
        n = len(bassin)
        for x in list(bassin):
            for pos in [-1, 1, -1j, 1j]:
                if area[x] < area[x+pos] and area[x+pos] < 9:
                    bassin.add(x+pos)
        if len(bassin) == n:
            break
    bassins.append(bassin)

lens = sorted([len(b) for b in bassins], reverse=True)
print(lens[0]*lens[1]*lens[2])