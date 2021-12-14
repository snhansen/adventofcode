from collections import defaultdict

with open('input') as f:
    inp = [x.strip() for x in f.readlines()]

s = inp.pop(0)

rules = {}
for l in inp:
    if l:
        lhs, rhs = l.split(' -> ')
        rules[lhs] = rhs


pairs = defaultdict(int)
for i in range(len(s)-1):
    pairs[s[i:i+2]] += 1


def update(d):
    new_d = defaultdict(int)
    for p in d.keys():
        new_d[p[0] + rules[p]] += d[p]
        new_d[rules[p] + p[1]] += d[p]
        d[p] = 0
    return new_d

def get_result(ps):
    counts = defaultdict(int)
    for p in ps.keys():
        for c in p:
            counts[c] += pairs[p]
    for c in counts:
        counts[c] = (counts[c] // 2)
        if c in [s[0], s[-1]]:
            counts[c] += 1
    return max(counts.values()) - min(counts.values())

for i in range(40):
    pairs = update(pairs)
    if i == 9 or i == 39:
        print(get_result(pairs))    