from functools import reduce
import networkx as nx


def knot_hash_bin(s):
    ascii_lengths = [ord(c) for c in s]
    ascii_lengths += [17, 31, 73, 47, 23]
    ls = list(range(256))
    n = len(ls)
    p = 0
    skip_size = 0
    for _ in range(64):
        for l in ascii_lengths:
            if p + l <= n:
                sub_ls = ls[p:(p+l)]
                ls = ls[:p] + sub_ls[::-1] + ls[p+l:]
            else:
                rev = ls[p:] + ls[:(l-(n-p))]
                rev = rev[::-1]
                rest = ls[(l-(n-p)):p]
                ls = rev[(n-p):] + rest + rev[:(n-p)]
            p += l + skip_size
            p %= n
            skip_size += 1

    res = ""
    for i in range(0, 16):
        block = reduce(lambda x, y: x ^ y, ls[16*i:16*(i+1)])
        h = hex(block)[2:]
        if len(h) == 1:
            h = "0" + h
        res += h


    bin_res = ""
    for c in res:
        bin_res += bin(int(c, 16))[2:].zfill(4)
    
    return bin_res


# Part 1
inp = "amgozmfv"
disc = {j + i*1j: c for i in range(128) for j, c in enumerate(knot_hash_bin(f"{inp}-{i}"))}
print(list(disc.values()).count("1"))

# Part 2
g = nx.Graph()
for p, used in disc.items():
    if used == "0":
        continue
    for dp in (-1, 1, 1j, -1j):
        if p + dp in disc and disc[p + dp] == "1":
            g.add_edge(p, p + dp)

comps = list(nx.connected_components(g))

comp_ps = [p for comp in comps for p in comp]
lone_comps = []
for p, used in disc.items():
    if used == "1" and p not in comp_ps:
        lone_comps.append(p)

print(len(list(nx.connected_components(g))) + len(lone_comps))