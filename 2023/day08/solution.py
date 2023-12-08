import re
import math
from functools import reduce

with open("input") as f:
    inp = f.read().strip().split("\n")

dirs = inp[0]
network = {}
for line in inp[2:]:
    elements = re.findall("\w+", line)
    network[elements[0]] = (elements[1], elements[2])


def get_steps(p, part2):
    step = 0
    while True:
        if (p == "ZZZ" and not part2) or (p[2] == "Z" and part2):
            return step
        dir_ = dirs[step%(len(dirs))]
        lr = 0 if dir_ == "L" else 1
        p = network[p][lr]
        step += 1


# Part 1
print(get_steps("AAA", False))
    
# Part 2
steps = [get_steps(p, True) for p in network.keys() if p[2] == "A"]
print(reduce(math.lcm, steps))