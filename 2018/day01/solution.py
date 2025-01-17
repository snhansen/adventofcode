import re 
from itertools import count

with open("input") as f:
    inp = f.read().strip()

# Part 1
nums = list(map(int, re.findall("-?\d+", inp)))
print(sum(nums))

# Part 2
seen = set()
freq = 0
for i in count():
    freq += nums[i%len(nums)]
    if freq in seen:
        print(freq)
        break
    seen.add(freq)