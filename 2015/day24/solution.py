from itertools import combinations
from collections import deque
from functools import reduce

with open('input') as f:
    gifts = list(map(int, [x.strip() for x in f.readlines()]))

# We find the smallest number of packages such that 
# the weight is exactly a third (fourth) of the total weight.
# While there is no reason to think that the remaining packages 
# be split into two (three) groups of the same weight, this seems
# to be the case.
    
def solve(part2):
    if part2:
        valid_weight = sum(gifts) // 4
    else:
        valid_weight = sum(gifts) // 3
    ls = []
    for i in range(len(gifts)):
        for l in combinations(gifts, i):
            if sum(l) == valid_weight:
                ls.append(l)
        if ls:
            break

    return min([reduce((lambda x, y: x*y), l) for l in ls])

print(solve(False))
print(solve(True))