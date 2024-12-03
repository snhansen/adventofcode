import re
from math import prod

with open("input") as f:
    inp = f.read().strip()


# Part 1
print(sum((prod(map(int, m)) for m in re.findall("mul\((\d+),(\d+)\)", inp))))

# Part 2
mults = re.finditer("mul\((\d+),(\d+)\)", inp)
dos = re.finditer("do\(\)|don't\(\)", inp)

iter_ = []

for m in mults:
    iter_.append((m.start(0), m.end(0), m.group()))

for m in dos:
    iter_.append((m.start(0), m.end(0), m.group()))
    
iter_.sort(key = lambda x: x[0])

do = True
ans = 0
for i, _, s in iter_:
    if s == "don't()":
        do = False
    elif s == "do()":
        do = True
    else:
        if do:
            nums = re.findall("\d+", s)
            ans += prod(map(int, nums))
    
print(ans)    