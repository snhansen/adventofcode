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
        

# Part 1
ans = 0
for line in inp:
    diagram, *buttons, reqs = line.split(" ")
    diagram = diagram[1:-1]
    buttons = [set(map(int, re.findall(r"\d+", bs))) for bs in buttons]
    ans += solve_part1(diagram, buttons)

print(ans)

# Part 2
def solve_part2(reqs, buttons):
    buttons_vecs = [tuple(1 if i in bs else 0 for i in range(len(reqs))) for bs in buttons]
    ns = [Int(f"n{i}") for i in range(len(buttons))]
    opt = Optimize()
    for n in ns:
        opt.add(n >= 0)
    for i in range(len(reqs)):
        eq = sum(button[i]*ns[j] for j, button in enumerate(buttons_vecs))
        opt.add(eq == reqs[i])

    opt.minimize(sum(ns))
    opt.check()
    model = opt.model()
    return sum([model[n].as_long() for n in ns])
    

ans = 0
for line in inp:
    diagram, *buttons, reqs = line.split(" ")
    diagram = diagram[1:-1]
    buttons = [set(map(int, re.findall(r"\d+", bs))) for bs in buttons]
    reqs = tuple(map(int, re.findall(r"\d+", reqs)))
    ans += solve_part2(reqs, buttons)

print(ans)