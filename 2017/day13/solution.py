from itertools import count

with open("input") as f:
    inp = f.read().strip().split("\n")


depths = {int(x): int(y) for line in inp for x, y in [line.split(": ")]}

# For a layer with depth d, the scanner is at the top
# at times k*2*(d-1) for k = 0, 1, 2...

# Part 1
severity = 0
for layer, depth in depths.items():
    top_t = 2*(depth - 1)
    if layer % top_t == 0:
        severity += layer*depth

print(severity)

# Part 2
def can_pass(delay):
    for layer, depth in depths.items():
        top_t = 2*(depth - 1)
        if (layer + delay) % top_t == 0:
            return False
    return True


for delay in count():
    if can_pass(delay):
        print(delay)
        break