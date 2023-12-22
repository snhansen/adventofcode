from collections import defaultdict
from copy import deepcopy

with open("input") as f:
    inp = f.read().strip().split("\n")


bricks = []

for line in inp:
    st, end = line.split("~")
    st = list(map(int, st.split(",")))
    end = list(map(int, end.split(",")))
    bricks.append(tuple(zip(st, end)))
    
def get_z_max(brick, bricks):
    z_max = 0
    (x0, x1), (y0, y1), (z0, z1) = brick
    for other_brick in bricks:
        (u0, u1), (v0, v1), (w0, w1) = other_brick
        if w1 >= z1:
            continue
        if (u0 > x1) or (u1 < x0) or (v0 > y1) or (v1 < y0):
            continue
        z_max = max(z_max, w1)
    return z_max


def get_support(brick, bricks):
    (x0, x1), (y0, y1), (z0, z1) = brick
    support = set()
    for other_brick in bricks:
        (u0, u1), (v0, v1), (w0, w1) = other_brick
        if (w1+1) != z0:
            continue
        if (u0 > x1) or (u1 < x0) or (v0 > y1) or (v1 < y0):
            continue
        support.add(other_brick)
    return support


bricks = sorted(bricks, key = lambda x: x[2][0]) # sorting by z-height
settled_bricks = []
for brick in bricks:
    (x0, x1), (y0, y1), (z0, z1) = brick
    new_z = get_z_max(brick, settled_bricks) + 1
    drop_z = z0 - new_z
    settled_bricks.append(((x0, x1), (y0, y1), (z0 - drop_z, z1 - drop_z)))


support = {brick: get_support(brick, settled_bricks) for brick in settled_bricks}

# Part 1
ans = 0
for brick in support.keys():
    can_be_disintegrated = True
    for other_brick, supp in support.items():
        if brick == other_brick:
            continue
        if supp == {brick}:
            can_be_disintegrated = False
            break
    ans += int(can_be_disintegrated)

print(ans)

# Part 2
ans = 0
for brick in support.keys():
    (x0, x1), (y0, y1), (z0, z1) = brick
    will_fall = set()
    will_fall.add(brick)
    for other_brick in support.keys():
        (u0, u1), (v0, v1), (w0, w1) = other_brick
        if brick == other_brick:
            continue
        if w0 <= z1:
            continue
        if len(support[other_brick] - will_fall) == 0:
            will_fall.add(other_brick)
    ans += len(will_fall) - 1

print(ans)