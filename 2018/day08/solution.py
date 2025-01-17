from collections import defaultdict

with open("input") as f:
    inp = f.read().strip()


inp = list(map(int, inp.split(" ")))
metadata = defaultdict(list)
children = defaultdict(list)
descendants = defaultdict(set)
p = 0
route = []
while p < len(inp):
    jump = 2 + sum(len(metadata[desc]) + 2 for desc in descendants[p]) + len(metadata[p])
    if len(children[p]) < inp[p]:
        route.append(p)
        p += jump 
    else:
        metadata[p] = inp[p + jump: p + jump + inp[p + 1]]
        if route:
            for q in route:
                descendants[q].add(p)
            children[route[-1]].append(p)
            p = route.pop()
        else:
            p += 2 + jump + len(metadata[p])

print(sum(val for ls in metadata.values() for val in ls))

# Part 2
def value(node):
    if len(children[node]) == 0:
        return sum(metadata[node])
    res = 0
    for entry in metadata[node]:
        if 0 <= entry - 1 < len(children[node]):
            res += value(children[node][entry - 1])
    return res


print(value(0))