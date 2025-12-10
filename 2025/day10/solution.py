from collections import deque
import re
from z3 import *

with open("input") as f:
    inp = f.read().strip().split("\n")


def solve_part1(diagram, buttons):
    q = deque([(0, "."*len(diagram))])
    seen = set()
    while q:
        n, lights = q.popleft()
        if lights in seen:
            continue
        seen.add(lights)
        if lights == diagram:
            return n
        for button in buttons:
            new_lights = ''.join(
                ('#' if ch == '.' else '.') if i in button else ch
                for i, ch in enumerate(lights)
            )
            q.append((n + 1, new_lights))


def solve_part2(reqs, buttons):
    buttons = [tuple(1 if i in bs else 0 for i in range(len(reqs))) for bs in buttons]
    ns = [Int(f"n{i}") for i in range(len(buttons))]
    opt = Optimize()
    for n in ns:
        opt.add(n >= 0)
    for i, req in enumerate(reqs):
        opt.add(sum(button[i]*ns[j] for j, button in enumerate(buttons)) == req)
    opt.minimize(sum(ns))
    opt.check()
    model = opt.model()
    return sum([model[n].as_long() for n in ns])


# Part 1 and 2
ans_pt1 = ans_pt2 = 0
for line in inp:
    diagram, *buttons, reqs = line.split(" ")
    diagram = diagram[1:-1]
    buttons = [set(map(int, re.findall(r"\d+", bs))) for bs in buttons]
    reqs = tuple(map(int, re.findall(r"\d+", reqs)))
    ans_pt1 += solve_part1(diagram, buttons)
    ans_pt2 += solve_part2(reqs, buttons)

print(ans_pt1)
print(ans_pt2)