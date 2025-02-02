import networkx as nx

with open("input") as f:
    inp = f.read().strip().replace("^", "").replace("$", "")

# We make a simplifying assumption that, after a branching has ended,
# we either return to the initial room or reach a dead end.
# The input seems to satisfy this.

g = nx.Graph()
dirs = {"E": 1, "W": -1, "N": 1j, "S": -1j}
s = list(inp)
route = [0]
p = route[-1]
while s:
    c = s.pop(0)
    if c.isalpha():
        new_p = p + dirs[c]
        g.add_edge(p, new_p)
        p = new_p
        continue
    if c == "(":
        route.append(p)
    elif c == ")":
        p = route.pop()
    elif c == "|":
        p = route[-1]

# Part 1
paths = list(nx.shortest_path_length(g, 0).values())
print(max(paths))

# Part 2
print(sum(1 for path in paths if path >= 1000))