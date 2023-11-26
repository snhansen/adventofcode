import sys
import os
sys.path.insert(1, os.path.dirname(os.getcwd()))
from aoc_functions import droid
from collections import deque
from itertools import chain, combinations

with open('input') as f:
    inp = list(map(int, f.read().split(',')))

# Let us find all items and the directions to get there.
opp_dir = {'north': 'south', 'south': 'north', 'east': 'west', 'west': 'east'}
items = {}
d = droid(inp)
d.initialize()

droids = deque([d])
while droids:
    d = droids.popleft()
    if d.items:
        for item in d.items:
            if item not in items:
                items[item] = d.dir_history
    if 'pressure-sensitive' in d.msg:
        door_dirs = d.dir_history
    else:
        for dir in d.dirs:
            if not d.dir_history:
                clone = d.clone()
                clone.move(dir)
                droids.append(clone)
            elif dir != opp_dir[d.dir_history[-1]]:
                clone = d.clone()
                clone.move(dir)
                droids.append(clone)

# Manual removal of unsafe items.
for item in ['molten lava', 'photons', 'infinite loop', 'escape pod', 'giant electromagnet']:
    del items[item]

def go_to(d, item):
    if item == 'start':
        dirs = deque([opp_dir[x] for x in reversed(d.dir_history)])
    elif item == 'door':
        dirs = door_dirs
    else:    
        dirs = deque(items[item])
    while dirs:
        d.move(dirs.popleft())

# Let's pick up all items and go to door.
d = droid(inp)
d.initialize()           

for item in items:
    go_to(d, item)
    d.take(item)
    go_to(d, 'start')

go_to(d, 'door')

# # Let's try all combinations of equipped items until we are let through.
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

for items in powerset(set(items)):
    clone = d.clone()
    for item in items:
        clone.drop(item)
    clone.move('east')
    if 'lighter' not in clone.msg and 'heavier' not in clone.msg:
        print(clone.msg)
        break
