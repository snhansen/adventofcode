from collections import defaultdict, deque

with open('input') as f:
    inp = f.read().split()

goto = defaultdict(list)

for l in inp:
    x, y = l.split('-')
    if y != 'start':
        goto[x].append(y)
    if x != 'start':
        goto[y].append(x)

to_check = deque()
to_check.append((['start'], False))
paths = []

while to_check:
    path, twice = to_check.popleft()
    if 'end' in path:
        paths.append((path, twice))
    else:
        for x in goto[path[-1]]:
            criterion = x.islower() and x in path
            if twice and criterion:
                continue
            if not twice and criterion:
                to_check.append((path + [x], True))
                continue
            else:
                to_check.append((path + [x], twice))

# Part 1
print(sum(not twice for _, twice in paths))

# Part 2
print(len(paths))