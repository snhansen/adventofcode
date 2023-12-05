import re

with open("input") as f:
    inp = f.read().strip().split("\n\n")

seeds = list(map(int, re.findall("\d+", inp[0])))

maps = []
for part in inp[1:]:    
    maps.append([list(map(int, x.split())) for x in part.split("\n")[1:]])

def convert(n, map_):
    for d0, s0, d in map_:
        if s0 <= n <= s0+d-1:
            return(d0+(n-s0))
    return n

source = seeds
for map_ in maps:
    source = [convert(n, map_) for n in source]

print(min(source))

# Part 2
def convert2(interval, map_):
    int0, int1 = interval
    output = []
    for dest0, src0, d in map_:
        src1 = src0 + d -1
        dest1 = dest0 + d - 1
        lower = max(int0, src0)
        upper = min(int1, src1)
        if upper >= lower:
            output.append(( (lower, upper), (dest0 + max(0, int0-src0), dest1 - max(0, src1-int1)) ))
    
    if not output:
        return [interval]
    
    output = sorted(output, key = lambda x: x[0][0])
    res = []
    start = int0
    for out in output:
        (x0, x1), _ = out
        if x0 > start:
            res.append(((start, x0-1), (start, x0-1)))
        res.append(out)
        start = x1 + 1
    if start < int1:
        res.append(((start, int1), (start, int1)))
    return([x[1] for x in res])

seed_ranges = []
for i in range(0, len(seeds), 2):
    seed_ranges.append((seeds[i], seeds[i]+seeds[i+1]-1))

seed_ranges = sorted(seed_ranges, key = lambda x: x[0])

output = []
for seed in seed_ranges:
    res = [seed]
    for map_ in maps:
        res_new = []
        for r in res:
            res_new += convert2(r, map_)
        res = res_new
    output.append((seed, res))

print(min([y[0] for x in output for y in x[1]]))