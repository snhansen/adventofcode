from collections import deque

with open("input") as f:
    pt1, pt2 = f.read().strip().split("\n\n")


instr = pt2.replace("\n", "")
dirs = {">": 1, "<": -1, "v": 1j, "^": -1j}

# Part 1
walls = set()
boxes = set()
for i, l in enumerate(pt1.split("\n")):
    for j, c in enumerate(l):
        p = j + i*1j
        if c == "#":
            walls.add(p)
        elif c == "O":
            boxes.add(p)
        elif c == "@":
            robot = p


def move_boxes(p, dp, boxes):
    to_move = []
    while True:
        if p in boxes:
            to_move.append(p)
        elif p not in walls:
            break
        if p in walls:
            return False, boxes
        p += dp
    new_boxes = set()
    for p in boxes:
        if p in to_move:
            new_boxes.add(p + dp)
        else:
            new_boxes.add(p)
    return True, new_boxes


for dp in instr:
    new_p = robot + dirs[dp]
    if new_p in walls:
        continue
    if new_p not in walls | boxes:
        robot = new_p
        continue
    if new_p in boxes:
        move, boxes = move_boxes(new_p, dirs[dp], boxes)
        if move:
            robot = new_p


print(sum(int(p.real) + 100*int(p.imag) for p in boxes))

# Part 2
walls = set()
boxes = {}
for i, l in enumerate(pt1.split("\n")):
    j = 0
    for x in l:
        p = j + i*1j
        if x == "#":
            walls.add(p)
            walls.add(p + 1)
        elif x == "O":
            boxes[p] = p + 1
            boxes[p + 1] = p
        elif x == "@":
            robot = p
        j += 2


def affected_boxes(p, dp, boxes):
    q = deque([p, boxes[p]])
    aff_boxes = set()
    seen = set()
    while q:
        p = q.pop()
        if p in seen:
            continue
        seen.add(p)
        if p in boxes:
            aff_boxes.add(p)
        if p + dp in boxes:
            q.append(p + dp)
            q.append(boxes[p + dp])
    return aff_boxes


def move_boxes(p, dp, boxes):
    aff_boxes = affected_boxes(p, dp, boxes)
    for p in aff_boxes:
        if p + dp in walls:
            return False, boxes
    new_boxes = {}
    for p in boxes:
        if p in aff_boxes:
            new_boxes[p + dp] = boxes[p] + dp
        else:
            new_boxes[p] = boxes[p]
    return True, new_boxes


for dp in instr:
    new_p = robot + dirs[dp]
    if new_p in walls:
        continue
    if new_p not in walls | boxes.keys():
        robot = new_p
        continue
    if new_p in boxes.keys():
        move, boxes = move_boxes(new_p, dirs[dp], boxes)
        if move:
            robot = new_p


ans = 0
seen = set()
for p in boxes:
    if p in seen:
        continue
    seen.add(p)
    seen.add(boxes[p])
    ans += int(min(p.real, boxes[p].real)) + 100*int(min(p.imag, boxes[p].imag))

print(ans)