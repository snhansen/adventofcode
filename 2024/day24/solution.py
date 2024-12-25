import networkx as nx
import random

with open("input") as f:
    inp1, inp2 = f.read().strip().split("\n\n")

conns = {}
for line in inp2.split("\n"):
    x, op, y, _, z = line.split(" ")
    conns[z] = (x, y, op)

xy_vals = inp1.split("\n")

x = ""
for i in range(45):
    x += xy_vals[i].split(": ")[1]
x = x[::-1]
    
y = ""
for i in range(45, 90):
    y += xy_vals[i].split(": ")[1]
y = y[::-1]


def process(x, y, conns):
    n = len(conns.keys()) + 2*45
    ops = {"OR": "|", "AND": "&", "XOR": "^"}
    vals = {}

    for i, bit in enumerate(reversed(x)):
        vals[f"x{i:02}"] = int(bit)

    for i, bit in enumerate(reversed(y)):
        vals[f"y{i:02}"] = int(bit)

    while len(vals.keys()) < n:
        cur_len = len(vals.keys())
        for z, (x, y, op) in conns.items():
            if x not in vals.keys() or y not in vals.keys():
                continue
            vals[z] = eval(f"{vals[x]} {ops[op]} {vals[y]}")
        if len(vals.keys()) == cur_len:
            return None

    zs = sorted([(wire, val) for wire, val in vals.items() if wire.startswith("z")], reverse = True)
    ans = "".join([str(val) for _, val in zs])
    return ans

# Part 1
print(int(process(x, y, conns), 2))

# Part 2
def xbit(i):
    return "0" * (45 - i - 1) + "1" + "0" * i

# Looking at individual bits, we see that z06/z07, z11, z24, z35/z36 are problematic.
for i in range(45):
    x = xbit(i)
    print(process(x, x, conns), f"z{i+1}")


g = nx.Graph()
for line in inp2.split("\n"):
    x, op, y, _, z = line.split(" ")
    g.add_edge(x, z)
    g.add_edge(y, z)


def works(i, conns):
    x = xbit(i)
    return process(x, x, conns) == "0" + xbit(i + 1)


def works_for_all(conns):
    for i in range(44):
        if not works(i, conns):
            return False
    return True


def get_neighbors(node, depth):
    if depth == 1:
        return set(g.neighbors(node))
    res = set(g.neighbors(node))
    for subnode in set(g.neighbors(node)):
        res |= get_neighbors(subnode, depth - 1)
    return res


def swap(node1, node2, conns):
    new_conns = dict(conns)
    new_conns[node1], new_conns[node2] = new_conns[node2], new_conns[node1]
    return new_conns


# For each problematic bit we look at any two neighbors (of depth 3) and see if swapping them would resolve the issue.
# For each problematic bit there may be more than one swap that does the job, so we store them all.
swaps1 = []
from itertools import combinations
for node1, node2 in combinations(get_neighbors("z06", 3), 2):
    if node1[0] in ["x", "y"] or node2[0] in ["x", "y"]:
        continue
    if works(5, swap(node1, node2, conns)):
        swaps1.append((node1, node2))

swaps2 = []
for node1, node2 in combinations(get_neighbors("z11", 3), 2):
    if node1[0] in ["x", "y"] or node2[0] in ["x", "y"]:
        continue
    if works(10, swap(node1, node2, conns)):
        swaps2.append((node1, node2))

swaps3 = []
for node1, node2 in combinations(get_neighbors("z24", 3), 2):
    if node1[0] in ["x", "y"] or node2[0] in ["x", "y"]:
        continue
    if works(23, swap(node1, node2, conns)):
        swaps3.append((node1, node2))

swaps4 = []
for node1, node2 in combinations(get_neighbors("z35", 3), 2):
    if node1[0] in ["x", "y"] or node2[0] in ["x", "y"]:
        continue
    if works(34, swap(node1, node2, conns)):
        swaps4.append((node1, node2))


# We now create a map of all the (so far) valid swaps and their associated connections.
valid_swaps = {}
for swap1 in swaps1:
    for swap2 in swaps2:
        for swap3 in swaps3:
            for swap4 in swaps4:
                conns_alt = dict(conns)
                conns_alt = swap(swap1[0], swap1[1], conns_alt)
                conns_alt = swap(swap2[0], swap2[1], conns_alt)
                conns_alt = swap(swap3[0], swap3[1], conns_alt)
                conns_alt = swap(swap4[0], swap4[1], conns_alt)
                if works_for_all(conns_alt):
                    valid_swaps[(swap1, swap2, swap3, swap4)] = conns_alt


# We now randomly perform additions to weed out all the faulty swaps until we only have
# one remaining set of swaps.
while True:
    num1 = bin(random.getrandbits(45))[2:]
    num1 = num1.zfill(45)
    num2 = bin(random.getrandbits(45))[2:]
    num2 = num2.zfill(45)
    for swaps, conns_alt in list(valid_swaps.items()):
        if int(process(num1, num2, conns_alt), 2) != int(num1, 2) + int(num2, 2):
            valid_swaps.pop(swaps)
    if len(valid_swaps.keys()) == 1:
        break

print(",".join(sorted([node for tple in list(valid_swaps.keys())[0] for node in tple])))