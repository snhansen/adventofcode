from collections import defaultdict
from itertools import count

with open("input") as f:
    top, bottom = f.read().strip().split("\n\n")


state = defaultdict(lambda: ".")
for p, c in enumerate(top.split(": ")[1]):
    state[p] = c


rules = {}
for line in bottom.split("\n"):
    first, second = line.split(" => ")
    rules[first] = second


def update():
    surroundings = []
    ps = list(state.keys())
    ps += [min(ps) - 1, min(ps) - 2, max(ps) + 1, max(ps) + 2]
    for p in ps:
        surroundings.append("".join(state[p + dp] for dp in (-2, -1, 0, 1, 2)))
    for p, sur in zip(ps, surroundings):
        state[p] = rules[sur]

# Part 1
print(sum(p for p, c in state.items() if c == "#"))

# Part 2
# We notice that, after a certain point, the pattern will stay the same
# but will just move one index to the right at each update.
def pattern(state):
    return "".join((c for p, c in sorted(state.items()))).lstrip(".").rstrip(".")


for t in count():
    prev_pattern = pattern(state)
    update()
    if pattern(state) == prev_pattern:
        break

score = sum(p for p, c in state.items() if c == "#")
plants = sum(1 for p, c in state.items() if c == "#")
score += plants*(50000000000 - (t + 1))
print(score)