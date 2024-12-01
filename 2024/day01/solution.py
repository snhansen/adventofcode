with open("input") as f:
    inp = f.read().split()


ls1 = sorted([int(x) for i, x in enumerate(inp) if i % 2 == 0])
ls2 = sorted([int(x) for i, x in enumerate(inp) if i % 2 == 1])

# Part 1
print(sum([abs(x-y) for x, y in zip(ls1, ls2)]))

# Part 2
print(sum([x*ls2.count(x) for x in ls1]))