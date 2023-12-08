import re
import math
from functools import reduce

with open("input") as f:
    inp = f.read().strip().split("\n")


dirs = inp[0]
network = {}
for line in inp[2:]:
    elements = re.findall(r"\b\w{3}\b", line)
    network[elements[0]] = (elements[1], elements[2])

# Part 1
p = "AAA"
step = 0

while p != "ZZZ":
    dir_ = dirs[step%(len(dirs))]
    lr = 0 if dir_ == "L" else 1
    p = network[p][lr]
    step += 1

print(step)
    
# Part 2
ps = [p for p in network.keys() if p[2] == "A"]
steps = []

for p in ps:
    step = 0
    while p[2] != "Z":
        dir_ = dirs[step%(len(dirs))]
        lr = 0 if dir_ == "L" else 1
        p = network[p][lr]
        step += 1
    steps.append(step)

print(reduce(math.lcm, steps))