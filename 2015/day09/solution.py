from itertools import permutations

with open('input') as f:
    inp = [x.strip() for x in f.readlines()]

dists = {}
for l in inp:
    val = int(l.split(' = ')[1])
    loc1 = l.split(' = ')[0].split(' to ')[0]
    loc2 = l.split(' = ')[0].split(' to ')[1]
    dists[loc1, loc2] = val
    dists[loc2, loc1] = val
 
locs = list(set([x[i] for x in dists.keys() for i in range(2)]))
 
min_dist = float('inf')
max_dist = 0
for l in permutations(locs):
    temp = sum([dists[l[i], l[i+1]] for i in range(len(l)-1)])
    min_dist = min(temp, min_dist)
    max_dist = max(temp, max_dist)
 
print(min_dist)
print(max_dist)