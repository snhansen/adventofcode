from collections import deque

with open("input") as f:
    inp = f.read().strip().split("\n")


components = {}
for i, line in enumerate(inp):
    x, y = line.split("/")
    components[i] = (int(x), int(y))


bridges = []
q = deque([])
q.append((0, [], dict(components)))

while q:
    port, bridge, comps = q.popleft()
    for i, (x, y) in comps.items():
        if port == x:
            new_port = y
        elif port == y:
            new_port = x
        else:
            continue
        new_bridge = list(bridge)
        new_bridge += [port, new_port]
        new_comps = dict(comps)
        new_comps.pop(i)
        q.append((new_port, new_bridge, new_comps))
        bridges.append(new_bridge)

# Part 1
print(max(map(sum, bridges)))

# Part 2
max_len = max(map(len, bridges))
print(max(map(sum, (x for x in bridges if len(x) == max_len))))