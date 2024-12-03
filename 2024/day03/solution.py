import re
from math import prod

with open("input") as f:
    inp = f.read().strip()


# Part 1
print(sum((prod(map(int, m)) for m in re.findall("mul\((\d+),(\d+)\)", inp))))

# Part 2
iter_ = re.finditer("mul\((\d+),(\d+)\)|do\(\)|don't\(\)", inp)

do = True
ans = 0
for x in iter_:
    s = x.group()
    if s == "don't()":
        do = False
    elif s == "do()":
        do = True
    else:
        if do:
            nums = re.findall("\d+", s)
            ans += prod(map(int, nums))
    
print(ans)    