from collections import deque
import sys
import time

with open('input') as f:
    inp = f.read()
    
#print(inp)

chars = {}
all_keys = {}
i, j = 0, 0

for x in inp:
    if x != '\n':
        chars[complex(i, j)] = x
        if x == '@':
            start = complex(i, j)
        if x.islower():
            all_keys[x] = complex(i, j)
        i += 1
    else:
        j += 1
        i = 0

# Part 1
to_visit = deque()
to_visit.append((start, set(), 0))
visited = set()
break_now = False

while to_visit: 
    pos, keys, dist = to_visit.popleft()
    node = (pos, tuple(sorted(keys)))
    if node in visited:
        continue
    visited.add(node)
    if not chars[pos] or chars[pos] == '#':
        continue      
    if chars[pos].isupper() and chars[pos].lower() not in keys:
        continue
    for x in [1, 1j, -1, -1j]:
        new_pos = pos + x
        new_keys = set(keys)
        if chars[new_pos].islower():
            new_keys.add(chars[new_pos])
        if len(new_keys) == len(all_keys):
            print(dist+1)
            break_now = True  
            break
        to_visit.append((new_pos, new_keys, dist+1))
    if break_now:
        break

# Part 2
n_cols = int(max([x.real for x in chars.keys()]))
n_rows = int(max([x.imag for x in chars.keys()]))

for x in list(chars):
    if chars[x] == '@':
        chars[x] = '#'
        for i in [-1, 1]:
            for j in [-1j, 1j]:
                chars[x+j] = '#'
                chars[x+i] = '#'
                chars[x+i+j] = '@'
        break
            
for r in range(n_rows+1):
    print(''.join([chars[complex(i, r)] for i in range(n_cols+1)]))

def reachable_keys(pos, keys):
    dists = {}
    q = deque([(pos[i], i, 0) for i in range(len(pos))])
    while q:
        p, robot, dist = q.popleft()
        if not chars[p] or chars[p] == '#':
            continue
        if chars[p].isupper() and chars[p].lower() not in keys:
            continue
        if p in dists:
            continue
        dists[p] = (robot, dist)
        for x in [1, 1j, -1, -1j]:
            q.append((p + x, robot, dist+1))
    
    key_dists = {}
    for k in set(all_keys) - keys:
        try:
            key_dists[k] = dists[all_keys[k]]
        except KeyError:
            pass
    return key_dists

starts = [x for x in chars if chars[x] == '@']
to_visit = deque()
to_visit.append((tuple(starts), set(), 0))
visited = {}

best = float('inf')

while to_visit:
    pos, keys, dist = to_visit.popleft()
    node = (pos, tuple(sorted(keys)))
    if node in visited and dist >= visited[node]:
        continue
    visited[node] = dist
    skip_p = False
    for p in pos:
        if not chars[p] or chars[p] == '#':
            skip_p = True
            break
        if chars[p].isupper() and chars[p].lower() not in keys:
            skip_p = True
            break
    if skip_p:
        continue
    
    r_keys = reachable_keys(pos, keys)
    for key in r_keys:
        robot, d = r_keys[key]
        new_pos = list(pos)
        new_pos[robot] = all_keys[key]
        new_keys = set(keys)
        new_keys.add(key)
        new_dist = dist + d
        if len(new_keys) == len(all_keys):
            if new_dist < best:
                best = new_dist
        to_visit.append((tuple(new_pos), new_keys, new_dist))
        
print(best)