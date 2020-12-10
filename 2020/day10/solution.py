from collections import defaultdict
with open('input') as f:
    inp = list(map(int, f.readlines()))

inp.append(0)
inp.append(max(inp)+3)
inp.sort()
diff = [x-y for x,y in zip(inp[1:], inp[:len(inp)-1])]

# Part 1
print(len([x for x in diff if x == 3])*len([x for x in diff if x == 1]))

# Part 2
cache = defaultdict()
cache[0] = 1

def no_ways(i):
    try:
        return cache[i]
    except KeyError:
        cache[i] = sum([no_ways(j) for j in range(i) if inp[i]-inp[j]<=3])
        return cache[i]

print(no_ways(len(inp)-1))