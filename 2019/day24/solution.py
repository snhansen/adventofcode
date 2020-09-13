import networkx as nx

with open('input') as f:
    inp = [x.strip() for x in f.readlines()]

grid = {}
for j, y in enumerate(inp):
    for i, x in enumerate(y):
        grid[complex(i, j)] = x

def update_grid(g):
    new_g = {}
    for p in g:
        bugs = 0
        for d in [1, -1, 1j, -1j]:
            try:
                bugs += int(g[p+d] == '#')
            except KeyError:
                pass
        if g[p] == '#' and bugs != 1:
            new_g[p] = '.'
        elif g[p] == '.' and bugs in [1,2]:
            new_g[p] = '#'
        else:
            new_g[p] = g[p]
            
    return new_g

def bio_rating(g):
    points = 0
    count = 0
    for j in range(5):
        for i in range(5):
            if g[complex(i, j)] == '#':
                points += 2**count
            count += 1
    return points
        
# Part 1
grid_cp = dict(grid)
grids = [grid]

break_var = False
while True:
    grid_cp = update_grid(grid_cp)
    if grid_cp in grids:
        break
    grids.append(grid_cp) 

print(bio_rating(grid_cp))
    
# Part 2
def get_neighbors(p):
    layer = p[0]
    tile = p[1]
    neighs = []
    # Same-layer neighbors
    for d in [1, -1, 1j, -1j]:
        if 0<=(tile+d).imag<=4 and 0<=(tile+d).real<=4 and tile+d != 2+2j:
            neighs.append((layer, tile+d))
    # Outer neighbors
    if tile.imag == 0:
        neighs.append((layer-1, 2+1j))
    if tile.imag == 4:
        neighs.append((layer-1, 2+3j))
    if tile.real == 0:
        neighs.append((layer-1, 1+2j))
    if tile.real == 4:
        neighs.append((layer-1, 3+2j))    
    # Inner neighbors
    if tile == 2+1j:
        for i in range(5):
            neighs.append((layer+1, i))
    if tile == 2+3j:
        for i in range(5):
            neighs.append((layer+1, i+4j))
    if tile == 1+2j:
        for i in range(5):
            neighs.append((layer+1, complex(0, i)))
    if tile == 3+2j:
        for i in range(5):
            neighs.append((layer+1, complex(4, i)))
    return neighs

def create_graph(l):
    g = nx.Graph()
    for i in range(5):
        for j in range(5):
            tile = complex(i, j)
            if l == 0:
                bug = (grid[tile] == '#')
            else:
                bug = False
            if  i != 2 or j != 2:
                g.add_node((l, tile), bug = bug)
                for d in [1, -1, 1j, -1j]:
                    if 0<=(tile+d).imag<=4 and 0<=(tile+d).real<=4 and tile+d != 2+2j:
                        g.add_edge((l, tile), (l, tile+d))
    return g

def update_graph(g):
    g_new = g.copy()
    n_ls = max([p[0] for p in g.nodes()])
    n_ls_w_bugs = max([p[0] for p in g.nodes() if g.nodes[p]['bug']])
    if n_ls_w_bugs == n_ls:
        g_new = nx.compose(g_new, create_graph(n_ls+1))
        g_new = nx.compose(g_new, create_graph(-n_ls-1))  
    n_ls = max([p[0] for p in g_new.nodes()])
    for p in g.nodes():
        for n in [x for x in get_neighbors(p) if abs(x[0]) <= n_ls]:
            g_new.add_edge(p, n)
    g_new_cp = g_new.copy()
    for p in g_new_cp.nodes():
        bugs = sum([g_new_cp.nodes[n]['bug'] for n in g_new_cp.neighbors(p)])
        if p not in g.nodes():
            g_new.nodes[p]['bug'] = bugs in [1, 2]
        else:
            if g.nodes[p]['bug'] and bugs != 1:
                g_new.nodes[p]['bug'] = False
            elif not g.nodes[p]['bug'] and bugs in [1,2]:
                g_new.nodes[p]['bug'] = True
            else:
                g_new.nodes[p]['bug'] = g.nodes[p]['bug']     
    return g_new

def print_graph(g):
    dict = {True: '#', False: '.'}
    l_min = min([p[0] for p in g.nodes()])
    l_max = max([p[0] for p in g.nodes()])
    for l in range(l_min, l_max+1):
        print(f'Layer {l}:')
        for j in range(5):
            temp = []
            for i in range(5):
                try:
                    temp.append(dict[g.nodes[(l, complex(i, j))]['bug']])
                except KeyError:
                    temp.append(' ')
            print(''.join(temp))

g = create_graph(0)
for i in range(200):
    g = update_graph(g)

print(sum(nx.get_node_attributes(g, 'bug').values()))