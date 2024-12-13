import re
from sympy import symbols, Eq, solve

with open("input") as f:
    inp = f.read().strip().split("\n\n")

machines = [list(map(int, re.findall("\d+", part))) for part in inp]


def aoc_solve(machines, part2):
    ans = 0
    for machine in machines:
        if part2:
            machine[4] += 10000000000000
            machine[5] += 10000000000000
        k1, k2 = symbols("k1 k2")
        eq1 = Eq(k1*machine[0] + k2*machine[2], machine[4])
        eq2 = Eq(k1*machine[1] + k2*machine[3], machine[5])
        solution = solve((eq1, eq2), (k1, k2))
        k1, k2 = solution[k1], solution[k2]
        if k1 == int(k1) and k2 == int(k2):
            ans += 3*k1 + k2
    return ans


# Part 1
print(aoc_solve(machines, False))

# Part 2
print(aoc_solve(machines, True))