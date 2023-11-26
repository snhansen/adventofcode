from collections import defaultdict

with open('input') as f:
    inp = f.read().splitlines()

tiles = defaultdict(int)
dirs = {'se': 1+2j, 'sw': -1+2j, 'nw': -1-2j, 'ne': 1-2j, 'e': 2, 'w': -2}

def get_pos(s):
    pos = 0
    idx = 0
    while idx<len(s):
        try:
            if s[idx:idx+2] in dirs:
                pos += dirs[s[idx:idx+2]]
                idx += 2
                continue
        except IndexError:
            continue
        pos += dirs[s[idx]]
        idx += 1
    return pos

# Part 1
pos = [get_pos(s) for s in inp]
for p in pos:
    tiles[p] = (tiles[p] + 1)%2

print(sum(tiles.values()))

# Part 2
def update(t):
    to_check = list(set([x+dir for dir in dirs.values() for x in t.keys()]))
    new_t = defaultdict(int)
    for pos in to_check:
        c = sum([t[pos+dir] for dir in dirs.values()])
        if t[pos] == 1 and (c == 0 or c > 2):
            new_t[pos] = 0
        elif t[pos] == 0 and c == 2:
            new_t[pos] = 1
        else:
            new_t[pos] = t[pos]
    return new_t

for _ in range(100):
    tiles = update(tiles)

print(sum(tiles.values()))