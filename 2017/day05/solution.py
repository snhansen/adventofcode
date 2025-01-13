from itertools import count

with open("input") as f:
    inp = f.read().strip().split("\n")


def solve(part2 = False):
    jumps = list(map(int, inp))
    p = 0
    for c in count():
        if p >= len(jumps):
            return c
        jump = jumps[p]
        jumps[p] += 1
        if part2 and jump >= 3:
            jumps[p] -= 2
        p += jump

# Part 1
print(solve())

# Part 2
print(solve(True))