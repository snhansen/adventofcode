from collections import defaultdict
import math

with open("input") as f:
    inp = f.read().strip().split("\n")


def calculate(nums, op):
    if op == "+":
        return sum(nums)
    elif op == "*":
        return math.prod(nums)


# Part 1
operators = inp[-1].split()
numbers = defaultdict(list)
for line in inp[:-1]:
    for i, x in enumerate(line.split()):
        numbers[i].append(int(x))
        
print(sum(calculate(nums, op) for nums, op in zip(numbers.values(), operators)))


# Part 2
grid = {x + y*1j: c for y, line in enumerate(inp[:-1]) for x, c in enumerate(line)}
R = len(inp) - 1
C = len(inp[0])

numbers = defaultdict(list)
c = 0
for x in range(C):
    n = "".join(grid[x + y*1j] for y in range(R)).strip()
    if not n.isdigit():
        c += 1
    else:
        numbers[c].append(int(n))

print(sum(calculate(nums, op) for nums, op in zip(numbers.values(), operators)))