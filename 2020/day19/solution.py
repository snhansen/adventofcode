with open('input') as f:
    inp = [x.splitlines() for x in f.read().split('\n\n')]

msgs = inp[1]

rules = {}
for x in inp[0]:
    rule = x.split(': ')[1].replace('"', '')
    if rule.isalpha():
        rules[int(x.split(': ')[0])] = rule
    else:
        rules[int(x.split(': ')[0])] = [list(map(int,y.split(' '))) for y in rule.split(' | ')]

def valid(m, v):
    if (m, v) in cache:
        return cache[(m, v)]
    rule = rules[v]
    if type(rule) == str:
        return int(rule == m)
    for r in rule:
        if len(r) == 1:
            if valid(m, r[0]):
                cache[(m, v)] = 1
                return 1
        else:
            for p in range(1, len(m)):
                if valid(m[:p], r[0]) and valid(m[p:], r[1]):
                    cache[(m, v)] = 1
                    return 1
            
    cache[(m, v)] = 0
    return 0

# Part 1
cache = {}
print(sum([valid(msg, 0) for msg in msgs]))

# Part 2
rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 1000]]
rules[1000] = [[11, 31]]
cache = {}
print(sum([valid(msg, 0) for msg in msgs]))