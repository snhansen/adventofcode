with open("input") as f:
    inp = f.read().strip().split("\n")

lookup = {}
weight = {}
for line in inp:
    first, *rest = line.split(" -> ")
    if rest:
        rest = rest[0].split(", ")
    first, w = first.split(" ")
    lookup[first] = rest
    weight[first] = int(w.strip("(").strip(")"))

# Part 1
subtowers = {x for u in lookup.values() for x in u}
print((set(lookup.keys()) - subtowers).pop())

# Part 2
def total_weight(node):
    if not lookup[node]:
        return weight[node]
    return sum(total_weight(subnode) for subnode in lookup[node]) + weight[node]


bottom = (set(lookup.keys()) - subtowers).pop()
q = [bottom]
while q:
    node = q.pop(0)    
    weights = {subnode: total_weight(subnode) for subnode in lookup[node]}
    for subnode, w in weights.items():
        if list(weights.values()).count(w) == 1:
            unbl_node = subnode
            q.append(subnode)

for node, subnodes in lookup.items():
    if unbl_node in subnodes:
        target_weight = [total_weight(subnode) for subnode in subnodes if subnode !=  unbl_node][0]

print(weight[unbl_node] - (total_weight(unbl_node) - target_weight))