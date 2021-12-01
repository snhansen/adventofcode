with open('input') as f:
    inp = list(map(int, f.readlines()))

def get_no_inc(ls):
    diff = [x-y for x, y in zip(ls[1:], ls[:-1])]
    return sum((x > 0 for x in diff))

# Part 1
print(get_no_inc(inp))

# Part 2
sums = []
for i in range(len(inp)-2):
    sums.append(inp[i] + inp[i+1] + inp[i+2])

print(get_no_inc(sums))