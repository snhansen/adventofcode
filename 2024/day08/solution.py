from collections import defaultdict
from itertools import combinations

with open("input") as f:
    inp = f.read().strip(). split("\n")

freqs = defaultdict(set)

for y, line in enumerate(inp):
    for x, char in enumerate(line):
        if char.isdigit() or char.isalpha():
            freqs[char].add(x + y*1j)

C, R = x, y


def solve(part2 = False):
    antinodes = set()
    for freq, locs in freqs.items():
        for p, q in combinations(locs, 2):
            if part2:
                candidates = [p + sgn*i*(p - q) for sgn in (-1, 1) for i in range(R)]
            else:
                candidates = [p + (p - q), q + (q - p)]
            for antinode in candidates: 
                if 0 <= antinode.real <= C and 0 <= antinode.imag <= R:
                    antinodes.add(antinode)
    return(len(antinodes))


# Part 1
print(solve(False))

# Part 2
print(solve(True))