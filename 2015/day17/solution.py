from itertools import chain, combinations
with open('input') as f:
    ls = [int(x) for x in f.readlines()]

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

# Part1
liters = 150
print(len([x for x in powerset(ls) if sum(x) == liters]))

# Part 2
min_cont = min([len(x) for x in powerset(ls) if sum(x) == liters])
print(len([x for x in powerset(ls) if sum(x) == liters and len(x) == min_cont]))