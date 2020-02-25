import itertools
import re
import math

inp = ['<x=0, y=6, z=1>', '<x=4, y=4, z=19>', '<x=-11, y=1, z=8>', '<x=2, y=19, z=15>']
#inp = ['<x=-1, y=0, z=2>', '<x=2, y=-10, z=-7>', '<x=4, y=-8, z=8>', '<x=3, y=5, z=-1>']
#inp = ['<x=-8, y=-10, z=0>', '<x=5, y=5, z=10>', '<x=2, y=-7, z=3>', '<x=9, y=-8, z=-3>']
pos = [[int(x) for x in re.findall('(?<==)[-]*[0-9][0-9]*', line)] for line in inp]
vel = [[0, 0, 0] for i in range(len(pos))]

def apply_gravity(i, j):
    for k in range(3):
        change = 0
        if pos[i][k] < pos[j][k]:
            change = 1
        elif pos[i][k] > pos[j][k]:
            change = -1
        vel[i][k] += change
        vel[j][k] -= change


def update_velocity():
    for (i, j) in itertools.combinations(range(0, len(inp)), 2):
        apply_gravity(i, j)
        
        
def update_position():
    for k in range(4):
        pos[k] = [sum(x) for x in zip(pos[k], vel[k])]
        

def update(times):
    for _ in range(times):
        update_velocity()
        update_position()
    
def get_total_energy(times):
    update(times)
    energy = 0
    for k in range(4):
        energy += sum(map(abs, pos[k]))*sum(map(abs, vel[k]))
        
    return energy


# Part 1
print(get_total_energy(1000))

# Part 2
pos_start = [[int(x) for x in re.findall('(?<==)[-]*[0-9][0-9]*', line)] for line in inp]
vel_start = [[0, 0, 0] for i in range(len(pos))]


def get_state(k):
    return [pos[i][k] for i in range(4)] + [vel[i][k] for i in range(4)]

    
cycles = []
for i in range(3):
    pos = [list(x) for x in pos_start]
    vel = [list(x) for x in vel_start]
    history = [get_state(i)]
    k = 0
    while True:
        update(1)
        coords = get_state(i)
        if coords in history:
            cycles.append(k+1)
            break
        history.append(coords)
        k += 1


def lcm(l):
    if len(l) == 2:
        return abs(l[0]*l[1]) // math.gcd(l[0], l[1])
    else:
        return lcm([l[0]] + [lcm(l[1:len(l)])])
    

print(lcm(cycles))

    
