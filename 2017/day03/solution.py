from itertools import count
from collections import defaultdict

inp = 368078

# Part 1
def solve_pt1():
    dp = [1, -1j, -1, 1j]
    points = {1: 0}
    p, c = 0, 2
    for n in count():
        dist = int(((n + 2)/2) // 1)
        for _ in range(dist):
            new_p = p + dp[n % 4]
            points[c] = new_p
            p = new_p
            if c == inp:
                return int(abs(p.imag) + abs(p.real))
            c += 1
        
print(solve_pt1())

# Part 2
def solve_pt2():
    dp = [1, -1j, -1, 1j]
    points = defaultdict(int)
    points[0] = 1
    p = 0
    for n in count():
        dist = int(((n + 2)/2) // 1)
        for _ in range(dist):
            new_p = p + dp[n % 4]
            points[new_p] = sum(points[new_p + dp2] for dp2 in (1, -1, 1j, -1j, 1+1j, 1-1j, -1+1j, -1-1j))
            if points[new_p] >= inp:
                return points[new_p]
            p = new_p

print(solve_pt2())