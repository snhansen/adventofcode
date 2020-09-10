import networkx as nx
from collections import defaultdict, deque
import math

with open('input') as f:
    ls = [x.strip('\n') for x in f.readlines()]

g = nx.grid_2d_graph(len(ls[0])-4, len(ls)-4, create_using = nx.Graph)

for y in range(len(ls)-4):
    for x in range(len(ls[0])-4):
        if ls[y+2][x+2] != '.':
            g.remove_node((x,y))

rows = []
for y in range(len(ls)):
    if len([x for x in ls[y] if x == ' ']) > 4:
        rows.append(y)

rows = rows[0:4] + rows[-4:]

cols = []
for x in range(len(ls[0])):
    if len([ls[i][x] for i in range(len(ls)) if ls[i][x] == ' ']) > 4:
        cols.append(x)

cols = cols[0:4] + cols[-4:]

tps = defaultdict(list)

for x in range(len(ls[0])):
    if ls[rows[0]][x].isupper() and ls[rows[1]][x].isupper():
        tps[ls[rows[0]][x]+ls[rows[1]][x]].append((x-2, rows[1]-1, 'o'))
    if ls[rows[2]][x].isupper() and ls[rows[3]][x].isupper():
        tps[ls[rows[2]][x]+ls[rows[3]][x]].append((x-2, rows[2]-3, 'i'))
    if ls[rows[4]][x].isupper() and ls[rows[5]][x].isupper():
        tps[ls[rows[4]][x]+ls[rows[5]][x]].append((x-2, rows[4], 'i'))
    if ls[rows[6]][x].isupper() and ls[rows[7]][x].isupper():
        tps[ls[rows[6]][x]+ls[rows[7]][x]].append((x-2, rows[6]-3, 'o'))
 
for y in range(len(ls)):
    if ls[y][cols[0]].isupper() and ls[y][cols[1]].isupper():
        tps[ls[y][cols[0]]+ls[y][cols[1]]].append((cols[1]-1, y-2, 'o'))
    if ls[y][cols[2]].isupper() and ls[y][cols[3]].isupper():
        tps[ls[y][cols[2]]+ls[y][cols[3]]].append((cols[2]-3, y-2, 'i'))
    if ls[y][cols[4]].isupper() and ls[y][cols[5]].isupper():
        tps[ls[y][cols[4]]+ls[y][cols[5]]].append((cols[4], y-2, 'i'))
    if ls[y][cols[6]].isupper() and ls[y][cols[7]].isupper():       
        tps[ls[y][cols[6]]+ls[y][cols[7]]].append((cols[6]-3, y-2, 'o'))

start = tps['AA'][0][0:2]
end = tps['ZZ'][0][0:2]
del tps['AA']
del tps['ZZ']

# Part 1
g_pt1 = g.copy()
for tp in tps:
    g_pt1.add_edge(tps[tp][0][0:2], tps[tp][1][0:2])

print(nx.shortest_path_length(g_pt1, start, end))

# Part 2
tps_pos = {}
tps_edge = {}
for tp in tps:
    tps_pos[tps[tp][0][0:2]] = tps[tp][1][0:2]
    tps_pos[tps[tp][1][0:2]] = tps[tp][0][0:2]
    for i in range(2):
        tps_edge[tps[tp][i][0:2]] = tps[tp][i][2]


exits_cache = {}
def reachable_exits(pos, layer):
    try:
        return exits_cache[pos, layer]
    except KeyError:
        exits = {}
        for p in [x for x in tps_pos if tps_edge[x] == 'i']:
            if nx.has_path(g, pos, p) and pos != p:
                exits[p] = nx.shortest_path_length(g, pos, p)
        
        if layer:
            for p in [x for x in tps_pos if tps_edge[x] == 'o']:
                if nx.has_path(g, pos, p) and pos != p:
                    exits[p] = nx.shortest_path_length(g, pos, p)

        if not layer:
            if nx.has_path(g, pos, end) and pos != end:
                exits[end] = nx.shortest_path_length(g, pos, end)
        
        exits_cache[pos, layer] = exits
        return exits


to_visit = deque()
to_visit.append((start, 0, 0))
visited = {}

min_dist = float('inf')

while to_visit:
    pos, layer, dist = to_visit.popleft()
    node = (pos, layer, dist)
    if node in visited and dist >= visited[node]:
        continue
    visited[node] = dist
    exits = reachable_exits(pos, layer)
    for p in exits:
        new_dist = dist + exits[p]
        if new_dist <= min_dist:    
            if p == end and layer == 0:
                min_dist = new_dist
                continue
            else:
                new_dist += 1
                new_layer = layer + 1 if tps_edge[p] == 'i' else layer - 1
                new_pos = tps_pos[p]
                to_visit.append((new_pos, new_layer, new_dist))

print(min_dist)