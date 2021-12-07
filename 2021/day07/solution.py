import math

with open('input') as f:
    ls = list(map(int, f.read().split(',')))

min_dist1, min_dist2 = math.inf, math.inf
for y in range(min(ls), max(ls)+1):
    dist1 = sum([abs(x-y) for x in ls])
    if dist1 < min_dist1:
        min_dist1 = dist1
    dist2 = sum([abs(x-y)*(abs(x-y)+1)//2 for x in ls])
    if dist2 < min_dist2:
        min_dist2 = dist2
    
print(min_dist1)
print(min_dist2)