import re
from z3 import *

with open("input") as f:
    inp = f.read().strip().split("\n")

bots = []
for line in inp:
    x, y, z, r = map(int, re.findall("-?\d+", line))
    bots.append(((x, y, z), r))

# Part 1
def dist(p1, p2):
    return sum(abs(c1 - c2) for c1, c2 in zip(p1, p2))


p, r = sorted(bots, key = lambda x: x[1])[-1]
print(sum(1 for p2, _ in bots if dist(p, p2) <= r))

# Part 2
opt = Optimize()
x, y, z = Int("x"), Int("y"), Int("z")

in_range = []
for (bx, by, bz), br in bots:
    in_range.append(If(Abs(x - bx) + Abs(y - by) + Abs(z - bz) <= br, 1, 0))

opt.maximize(Sum(in_range))
opt.minimize(x + y + z)
opt.check()
model = opt.model()

print(sum(abs(model[c].as_long()) for c in model))