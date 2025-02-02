import networkx as nx
from itertools import count

with open("input") as f:
    inp = f.read().strip().split("\n")


def print_():
    maxx = int(max(p.real for p in cavern))
    maxy = int(max(p.imag for p in cavern))
    for y in range(0, maxy + 2):
        res = ""
        for x in range(0, maxx + 2):
            p = x + y*1j
            if p in goblins:
                res += "G"
            elif p in elves:
                res += "E"
            elif p in cavern:
                res += "."
            else:
                res += "#"
        print(res)


def valid(p):
    if p not in cavern:
        return False
    if p in (goblins.keys() | elves.keys()):
        return False
    return True


def get_move(p_unit):
    enemies = goblins if p_unit in elves else elves
    paths = []
    for dp in (1, -1, 1j, -1j):
        p_from = p_unit + dp
        if p_from not in g.nodes():
            continue
        for p_enemy in enemies:
            for dq in (1, -1, 1j, -1j):
                p_to = p_enemy + dq
                if p_to not in g.nodes():
                    continue
                if nx.has_path(g, p_from, p_to):
                    paths.append((p_from, p_to, nx.shortest_path_length(g, p_from, p_to)))

    paths = sorted(paths, key = lambda x: (x[2], x[1].imag, x[1].real))
    dirs = {path[0] - p_unit for path in paths if path[2] == paths[0][2] and path[1] == paths[0][1]}
    for dir_ in (-1j, -1, 1, 1j):
        if dir_ in dirs:
            return dir_

    return None


def move(p_unit):
    enemies = goblins if p_unit in elves else elves
    allies = goblins if p_unit in goblins else elves
    for dp in (1, -1, 1j, -1j):
        if p_unit + dp in enemies:
            return 0
    dp = get_move(p_unit)
    if dp:
        allies[p_unit + dp] = allies[p_unit]
        allies.pop(p_unit)
        g.remove_node(p_unit + dp)
        for dq in (1, -1, 1j, -1j):
            if not valid(p_unit + dq):
                continue
            g.add_edge(p_unit, p_unit + dq)
        return dp
    else:
        return 0

def attack(p, attack_power):
    enemies = goblins if p in elves else elves
    allies = goblins if p in goblins else elves
    attack_power = attack_power if p in elves else 3
    res = [(p + dp, enemies[p + dp]) for dp in (1, -1, 1j, -1j) if p + dp in enemies]
    if res:
        res = sorted(res, key = lambda x: (x[1], x[0].imag, x[0].real))
        p_target = res[0][0]
        enemies[p_target] -= attack_power


def clean_up():
    res = []
    for units in [goblins, elves]:
        for p, hp in list(units.items()):
            if hp <= 0:
                units.pop(p)
                res.append(p)
    for p in res:
        for dp in (1, -1, 1j, -1j):
            if not valid(p + dp):
                continue
            g.add_edge(p, p + dp)
    return res


def round(attack_power):
    ps = list(goblins.keys()) + list(elves.keys())
    ps = sorted(ps, key = lambda x: (x.imag, x.real))
    killed = []
    while ps:
        p = ps.pop(0)
        if p in killed:
            continue
        dp = move(p)
        attack(p + dp, attack_power)
        killed += clean_up()
        if len(elves) == 0 or len(goblins) == 0:
            if ps:
                return 2
            else:
                return 1
    return 0


def combat(attack_power = 3):
    global cavern
    global goblins
    global elves
    global g
    cavern = set()
    goblins = {}
    elves = {}
    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            p = x + y*1j
            if c != "#":
                cavern.add(p)
            if c == "G":
                goblins[p] = 200
            if c == "E":
                elves[p] = 200

    g = nx.Graph()
    for p in cavern - (goblins.keys() | elves.keys()):
        for dp in (1, -1, 1j, -1j):
            np = p + dp
            if not valid(np):
                continue
            g.add_edge(p, np)

    for c in count():
        res = round(attack_power)
        if res:
            if res == 2:
                c -= 1
            break

    return (c + 1)*(sum(elves.values()) + sum(goblins.values()))

# Part 1
print(combat())

# Part 2
low, high = 3, 200
while (low < high):
    mid = low + (high - low) // 2
    res = combat(mid)
    if len(elves) < 10:
        low = mid + 1
    if len(elves) == 10:
        high = mid

print(combat(mid))