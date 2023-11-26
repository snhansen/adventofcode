from collections import defaultdict
import math

with open('input') as f:
    inp = [x.splitlines() for x in f.read().split('\n\n')]

tiles = defaultdict(list)

for tile in inp:
    id = int(tile[0].split(' ')[1].strip(':'))
    i = 0
    for j, row in enumerate(tile[1:]):
        tiles[id].append([int(c == '#') for c in row])

def print_tile(tile):
    d = {0: '.', 1: '#'}
    n = len(tile[0])
    for j in range(n):
        print(''.join([d[tile[j][i]] for i in range(n)]))
    print('')

def rotate(tile):
    new = []
    n = len(tile[0])
    for j in range(n):
        new.append([tile[n-1-i][j] for i in range(n)])
    return new

def flip(tile):
    new = []
    n = len(tile[0])
    for j in range(n):
        new.append([tile[n-1-j][i] for i in range(n)])
    return new

def get_tiles(tile):
    ls = []
    ls.append(list(tile))
    ls.append(flip(tile))
    for _ in range(3):
        tile = rotate(tile)
        ls.append(tile)
        ls.append(flip(tile))
    return ls

def get_border(tile, o):
    n = len(tile[0])
    if o == 'u':
        return tile[0]
    elif o == 'd':
        return tile[n-1]
    elif o == 'l':
        return [tile[i][0] for i in range(n)]
    elif o == 'r':
        return [tile[i][n-1] for i in range(n)]

d = {'u': 'd', 'd': 'u', 'l': 'r', 'r': 'l'}
dirs = ['u', 'd', 'l', 'r']

def match(tile1, tile2, o):
    return get_border(tile1, o) == get_border(tile2, d[o])

def has_adjacent(tile, o):
    for tile2 in tiles.values():
        if tile2 != tile:
            tiles_to_check = get_tiles(tile2)
            for tile3 in tiles_to_check:
                if match(tile, tile3, o):
                    return True
    return False

def is_corner(tile):
    return sum([has_adjacent(tile, o) for o in dirs]) == 2

# Part 1
corners = [id for id in tiles.keys() if is_corner(tiles[id])]
print(math.prod(corners))

# Part 2
def get_topleft():
    for id in tiles:
        for tile2 in get_tiles(tiles[id]):
            if has_adjacent(tile2, 'd') and has_adjacent(tile2, 'r') and not has_adjacent(tile2, 'u') and not has_adjacent(tile2, 'l'):
                return id, tile2

def get_adjacent(tile, o, ids):
    for id in ids:
        for tile2 in get_tiles(tiles[id]):
            if match(tile, tile2, o):
                return id, tile2

ids_left = list(tiles.keys())

id, tile = get_topleft()
grid = {}
grid[(0, 0)] = tile
ids_left.remove(id)
k = int(len(tiles)**0.5)

for i in range(1, k):
    id, tile = get_adjacent(grid[(i-1, 0)], 'r', ids_left)
    grid[(i, 0)] = tile
    ids_left.remove(id)

for i in range(k):
    for j in range(1, k):
        id, tile = get_adjacent(grid[(i, j-1)], 'd', ids_left)
        grid[(i, j)] = tile
        ids_left.remove(id)

def remove_borders(tile):
    new = []
    n = len(tile[0])
    for j in range(1,n-1):
        new.append([tile[j][i] for i in range(1,n-1)])
    return new

for coord in grid:
    grid[coord] = remove_borders(grid[coord])

n = len(grid[(0,0)][0])
final_grid = []
for j1 in range(k):
    for j2 in range(n):
        final_grid.append([x for i in range(k) for x in grid[(i,j1)][j2] ])
        
#print_tile(final_grid)

seamonster = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """

i, j = 0, 0
indices = [] 
for x in seamonster:
    if x == '#':
        indices.append((i, j))
    i += 1
    if x == '\n':
        j += 1
        i = 0

def is_monster(grid, i, j):
    for di, dj in indices:
        if grid[j+dj][i+di] == 0:
            return False
    return True

def get_no_monsters(g):
    c = 0
    for j in range(len(final_grid)-3):
        for i in range(len(final_grid)-20):
            c += int(is_monster(g, i, j))
    return c

ls = []
for _ in range(4):
    final_grid = rotate(list(final_grid))
    ls.append(final_grid)
    ls.append(flip(final_grid))
    
for grid in ls:
    c = get_no_monsters(grid)
    if c>0:
        print(sum([sum(final_grid[j]) for j in range(k*n)])-c*15)
        break