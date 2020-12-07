from collections import defaultdict, deque

with open('input') as f:
    inp = [x.strip() for x in f.readlines()]

bags = {}

for l in inp:
    col = l.split(' bags contain ')[0]
    bags[col] = defaultdict()
    if not 'no other bags' in l:
        for x in l.split(' bags contain ')[1].replace('.', '').split(', '):
            bags[col][x[2:].replace('bags','').replace('bag', '').strip()] = int(x[0])

# Part 1
colors = set()
colors.add('shiny gold')

while True:
    n = len(colors)
    for col in list(colors):
        for bag in bags:
            if col in bags[bag]:
                colors.add(bag)
    if len(colors) == n:
        break
    
print(len(colors) - 1)

# Part 2
to_check = deque([['shiny gold', 1]])
n_bags = []
while to_check:
    col, qt = to_check.popleft()
    n_bags.append([col, qt])
    if not bags[col]:
        continue
    else:
        for x in bags[col]:
            to_check.append([x, qt*bags[col][x]])

print(sum([x[1] for x in n_bags if x[0] != 'shiny gold']))