with open('input') as f:
	inp = f.read().strip()

ans = inp.split('\n\n')

# Part 1
print(sum([len(set(x.replace('\n', ''))) for x in ans]))

# Part 2
print(sum([len(set.intersection(*[set(x) for x in y.split('\n')])) for y in ans]))




