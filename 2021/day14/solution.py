from collections import defaultdict, Counter

start, end = open('input').read().split('\n\n')

rules = {}
for l in end.strip().split('\n'):
    lhs, rhs = l.split(' -> ')
    rules[lhs] = rhs

pairs = Counter([start[i:i+2] for i in range(len(start)-1)])


def update(d):
    new_d = defaultdict(int)
    for p in d:
        new_d[p[0] + rules[p]] += d[p]
        new_d[rules[p] + p[1]] += d[p]
    return new_d

def get_result(ps):
    counts = defaultdict(int)
    for p, val in ps.items():
        for c in p:
            counts[c] += val
    for c in counts:
        counts[c] = counts[c] // 2
        if c in [start[0], start[-1]]:
            counts[c] += 1
    return max(counts.values()) - min(counts.values())

for i in range(40):
    pairs = update(pairs)
    if i == 9 or i == 39:
        print(get_result(pairs))    