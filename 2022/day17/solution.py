with open("input") as f:
    jet = f.read().strip()

rock_types = [[2, 3, 4, 5], [3, 2+1j, 3+1j, 4+1j, 3+2*1j], [2, 3, 4, 4+1j, 4+2*1j], [2, 2+1j, 2+2*1j, 2+3*1j], [2, 3, 2+1j, 3+1*1j]]
dirs = {">": 1, "<": -1}
n_jets = len(jet)


def move(rock, dp, rocks):
    if any(p+dp in rocks for p in rock):
        return False
    if any((p+dp).real < 0 or (p+dp).real > 6 for p in rock):
        return False
    return [p+dp for p in rock]

    
def drop_rock(height, rock_type, jet_pos, rocks):
    rock = list(rock_types[rock_type])
    rock = [p + (height+4)*1j for p in rock]
    while True:
        res = move(rock, dirs[jet[jet_pos]], rocks)
        jet_pos = (jet_pos + 1)%n_jets
        if res:
            rock = res
        res = move(rock, -1j, rocks)
        if not res:
            rocks = rocks | set(rock)
            break
        else:
            rock = res
    return jet_pos, rocks


def xheight(rocks):
    ls = []
    for x in range(7):
        ls.append(int(max([p.imag for p in rocks if p.real == x])))
    return tuple(ls)


def run(n, rocks = set(range(7)), jet_pos = 0, rock_type = 0):
    for _ in range(n):
        height = int(max([p.imag for p in rocks]))
        jet_pos, rocks = drop_rock(height, rock_type, jet_pos, rocks)
        rock_type = (rock_type + 1)%5
    return (jet_pos, rock_type, rocks)


def max_height(n):
    _, _, rocks = run(n)
    return int(max([p.imag for p in rocks])) 


def print_map(ymin, ymax, rocks):
    for row in reversed(range(ymin, ymax+1)):
        print("".join(["#" if i+row*1j in rocks else "." for i in range(7)]))


# Part 1
print(max_height(2022))

# Part 2
# We seek a configuration that is repeated and save two indices.
seen = set()
rocks = set(range(7))
jet_pos = 0
rock_type = 0
i = 0
found = False
config = None
indices = []
while True:
    heights = xheight(rocks)
    height = max(heights)
    rel_heights = tuple([height-x for x in heights])
    if (jet_pos, rel_heights, rock_type) in seen and not found:
        config = (jet_pos, rel_heights, rock_type)
        found = True
    if (jet_pos, rel_heights, rock_type) == config:
        indices.append(i)
    if len(indices) == 2:
        break
    seen.add((jet_pos, rel_heights, rock_type))
    jet_pos, rock_type, rocks = run(1, rocks, jet_pos, rock_type)
    i += 1


# The rest is figuring out how many times this cycle is repeated
# within the 1000000000000 rounds.
n = 1000000000000
cycle = indices[1] - indices[0]
first = indices[0]
dh = max_height(first+cycle) - max_height(first)
m = (n - first) // cycle
rem = (n - first)%cycle
print(m*dh + max_height(first + rem))