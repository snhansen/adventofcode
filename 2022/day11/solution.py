import re
import math
import copy

with open("input") as f:
    inp = f.read().strip().split("\n\n")

items_init = []
operations = []
tests = []
to = []
for text in inp:
    ls = []
    for line in text.split("\n"):    
        match line.split(": "):
            case ["  Starting items", s]:
                items_init.append(list(map(int, re.findall("\d+", s))))
            case ["  Operation", s]:
                _, expr = s.split(" = ")
                operations.append(lambda old, expr = expr: eval(expr))
            case ["  Test", s]:
                tests.append(int(re.findall("\d+", s)[0]))
            case ["    If true", s]:
                ls.append(int(re.findall("\d+", s)[0]))
            case ["    If false", s]:
                ls.append(int(re.findall("\d+", s)[0]))
    to.append(ls)


def solve(part2 = False):
    items = copy.deepcopy(items_init)
    inspected = [0 for _ in range(len(items))]
    rounds = 10000 if part2 else 20
    for _ in range(rounds):
        for i in range(len(items)):
            inspected[i] += len(items[i])
            while items[i]:
                item = items[i].pop(0)
                item = operations[i](item)
                if part2:
                    item = item % math.prod(tests)
                else:
                    item = item // 3
                to_monkey = to[i][int(item%tests[i] != 0)]
                items[to_monkey].append(item)
    return math.prod(sorted(inspected)[-2:])

# Part 1
print(solve())

# Part 2
print(solve(True))