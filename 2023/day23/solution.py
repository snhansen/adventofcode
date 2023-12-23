from collections import deque
import networkx as nx

with open("input") as f:
    inp = f.read().strip().split("\n")


R, C = len(inp), len(inp[0])
grid = {i+j*1j: inp[j][i] for i in range(C) for j in range(R)}

for i in range(C):
    if grid[i] == ".":
        start = i
    if grid[i+(R-1)*1j] == ".":
        end = i+(R-1)*1j

grid[start-1j] = "#"
grid[end+1j] = "#"

# Part 1
slide = {">": 1, "<": -1, "^": -1j, "v": 1j}

paths = []
q = deque([(start, set())])
while q:
    p, seen = q.popleft()
    if p == end:
        paths.append(seen | {p})    
    if p in seen:
        continue
    c = grid[p]
    if c == "#":
        continue
    if c != ".":
        assert c in slide.keys()
        q.append((p + slide[c], seen | {p}))
    else:
        for dp in [1, -1, 1j, -1j]:
            q.append((p + dp, seen | {p}))

print(max(len(path)-1 for path in paths))
        
# Part 2
def find_segment(p, dir_):
    cur_p = p + dir_
    seen = {p, cur_p}
    steps = 1
    while True:
        dirs = [dp for dp in [-1, 1, 1j, -1j] if grid[cur_p+dp] != "#" and cur_p+dp not in seen]
        if len(dirs) != 1:
            break
        cur_p += dirs[0]
        seen.add(cur_p)
        steps += 1
    return (p, cur_p, steps)
        

opp = {1: -1, -1: 1, 1j: -1j, -1j: 1j}
segments = set()
q = deque([(start, 1j)])

while q:
    p, dir_ = q.pop()
    segment = find_segment(p, dir_)
    if segment in segments:
        continue
    segments.add(segment)
    st, en, steps = segment
    (new_p, ) = {st, en} - {p}
    for dp in [-1, 1, -1j, 1j]:
        if dp == opp[dir_]:
            continue
        if grid[new_p+dp] != "#":
            q.append((new_p, dp))


g = nx.Graph()
for p0, p1, n in segments:
    g.add_edge(p0, p1, weight = n)

ans = 0
q = deque([(start, {start}, 0)])
while q:
    p, seen, steps = q.pop()
    if p == end:
        ans = max(ans, steps)
        continue
    for new_p in g.neighbors(p):
        if new_p in seen:
            continue
        d_steps = g[p][new_p]["weight"]
        q.append((new_p, seen | {new_p}, steps + d_steps))

print(ans)