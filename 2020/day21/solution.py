from collections import defaultdict, OrderedDict
from itertools import cycle

with open('input') as f:
    inp = f.read().splitlines()

als = defaultdict(list)
ings = []
for x in inp:
    ings += x.split(' (contains ')[0].split()
    for al in x.split('contains ')[1].strip('\)').split(', '):
        als[al].append(set(x.split(' (contains ')[0].split()))
        
for al in als:
    als[al] = set.intersection(*als[al])

iter = cycle(als)
while sum([type(als[al]) == str for al in als]) < len(als):
    al = next(iter)
    if len(als[al]) == 1:
        ing = list(als[al])[0]
        als[al] = ing
        for x in als:
            if ing in als[x] and x != al:
                als[x].remove(ing)

# Part 1
print(len([ing for ing in ings if ing not in als.values()]))

# Part 2
als_sorted = OrderedDict(sorted(als.items()))
ans = ''
for x in als_sorted:
    ans += als_sorted[x]
    ans += ','

print(ans[:-1])
    