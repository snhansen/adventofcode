import re

with open("input") as f:
    raw_inp = f.read()


raw_inp, seq = raw_inp.split("\n\n")
raw_inp = raw_inp.split("\n")

moves = list(map(int, re.findall("\d+", seq)))
turns = re.findall("[LR]", seq)

inp = []
R = max(len(line) for line in raw_inp)
dim = R//3

for line in raw_inp:
    inp.append(line + "".join([" " for _ in range(R-len(line))]))
    
rows = []
for line in inp:
    ls = []
    wspaces = [0]*2
    i = 0
    for c in line:
        if c == " ":
            wspaces[i] += 1
        if c != " ":
            i = 1
            ls.append(c)
    rows.append((wspaces[0], wspaces[1], ls))

cols = []
for j in range(len(inp[0])):
    line = [line[j] for line in inp]
    ls = []
    wspaces = [0]*2
    i = 0
    for c in line:
        if c == " ":
            wspaces[i] += 1
        if c != " ":
            i = 1
            ls.append(c)
    cols.append((wspaces[0], wspaces[1], ls))


# facing: 0 = right, 1 = down, 2 = left, 3 = up
def move(x, y, facing):
    if facing == 0:
        offset, _, row = rows[y]
        nxt = (x-offset+1)%len(row)
        if row[nxt] != "#":
            x = offset + nxt
    elif facing == 2:
        offset, _, row = rows[y]
        nxt = (x-offset-1)%len(row)
        if row[nxt] != "#":
            x = offset + nxt
    elif facing == 1:
        offset, _ ,col = cols[x]
        nxt = (y-offset+1)%len(col)
        if col[nxt] != "#":
            y = offset + nxt
    elif facing == 3:
        offset, _ ,col = cols[x]
        nxt = (y-offset-1)%len(col)
        if col[nxt] != "#":
            y = offset + nxt
    return x, y


# Part 1
x, y = dim, 0
facing = 0
for i, steps in enumerate(moves):
    for _ in range(steps):
        x_new, y_new = move(x, y, facing)
        if x_new == x and y_new == y:
            break
        x, y = x_new, y_new
    if i < len(turns):
        turn = turns[i]
        if turn == "R":
            facing = (facing+1)%4
        else:
            facing = (facing-1)%4

print(1000*(y+1)+4*(x+1)+facing)

# Part 2
squares = []
squares.append((dim, 0, [row[dim:2*dim] for row in inp[:dim]]))
squares.append((2*dim, 0, [row[2*dim:3*dim] for row in inp[:dim]]))
squares.append((dim, dim, [row[dim:2*dim] for row in inp[dim:2*dim]]))
squares.append((0, 2*dim, [row[:dim] for row in inp[2*dim:3*dim]]))
squares.append((dim, 2*dim, [row[dim: 2*dim] for row in inp[2*dim:3*dim]]))
squares.append((0, 3*dim, [row[:dim] for row in inp[3*dim:4*dim]]))


def get_square(x, y):
    if 0 <= y < dim and dim <= x < 2*dim:
        return 0
    elif 0 <= y < dim and 2*dim <= x < 3*dim:
        return 1
    elif dim <= y < 2*dim and dim <= x < 2*dim:
        return 2
    elif 2*dim <= y < 3*dim and 0 <= x < dim:
        return 3
    elif 2*dim <= y < 3*dim and dim <= x < 2*dim:
        return 4
    elif 3*dim <= y < 4*dim and 0 <= x < dim:
        return 5
    else:
        assert False


def move2(x, y, facing):
    square = get_square(x, y)
    off_x, off_y, rows = squares[square]
    int_x, int_y = x-off_x, y-off_y
    dx, dy = dirs[facing]
    facing_old = facing
    if 0 <= int_x+dx < dim and 0 <= int_y+dy < dim:
        if rows[int_y+dy][int_x+dx] == ".":
            return (x+dx, y+dy, facing)
        else:
            return (x, y, facing)
    else:
        if square == 0 and facing == 0:
            int_x = 0
            int_y = int_y
            facing = 0
            square = 1
        elif square == 0 and facing == 1:
            int_x = int_x
            int_y = 0
            facing = 1
            square = 2
        elif square == 0 and facing == 2:
            int_x = 0
            int_y = dim-1-int_y
            facing = 0
            square = 3
        elif square == 0 and facing == 3:
            int_y = int_x
            int_x = 0
            facing = 0
            square = 5
        elif square == 1 and facing == 0:
            int_y = dim-1-int_y
            int_x = dim-1
            facing = 2
            square = 4
        elif square == 1 and facing == 1:
            int_y = int_x
            int_x = dim-1
            facing = 2
            square = 2
        elif square == 1 and facing == 2:
            int_x = dim-1
            int_y = int_y
            facing = 2
            square = 0
        elif square == 1 and facing == 3:
            int_x = int_x
            int_y = dim-1
            facing = 3
            square = 5
        elif square == 2 and facing == 0:
            int_x = int_y
            int_y = dim-1
            square = 1
            facing = 3
        elif square == 2 and facing == 1:
            int_y = 0
            int_x = int_x
            square = 4
            facing = 1
        elif square == 2 and facing == 2:
            int_x = int_y
            int_y = 0
            square = 3
            facing = 1
        elif square == 2 and facing == 3:
            int_y = dim-1
            int_x = int_x
            facing = 3
            square = 0
        elif square == 3 and facing == 0:
            int_x = 0
            int_y = int_y
            facing = 0
            square = 4
        elif square == 3 and facing == 1:
            int_x = int_x
            int_y = 0
            square = 5
            facing = 1
        elif square == 3 and facing == 2:
            int_x = 0
            int_y = dim-1-int_y
            square = 0
            facing = 0
        elif square == 3 and facing == 3:
            int_y = int_x
            int_x = 0
            square = 2
            facing = 0
        elif square == 4 and facing == 0:
            int_x = dim-1
            int_y = dim-1-int_y
            facing = 2
            square = 1
        elif square == 4 and facing == 1:
            int_y = int_x
            int_x = dim-1
            square = 5
            facing = 2
        elif square == 4 and facing == 2:
            int_x = dim-1
            int_y = int_y
            square = 3
            facing = 2
        elif square == 4 and facing == 3:
            int_x = int_x
            int_y = dim-1
            square = 2
            facing = 3
        elif square == 5 and facing == 0:
            int_x = int_y
            int_y = dim-1
            facing = 3
            square = 4
        elif square == 5 and facing == 1:
            int_y = 0
            int_x = int_x
            facing = 1
            square = 1
        elif square == 5 and facing == 2:
            int_x = int_y
            int_y = 0
            facing = 1
            square = 0
        elif square == 5 and facing == 3:
            int_y = dim-1
            int_x = int_x
            facing = 3
            square = 3
        off_x, off_y, rows = squares[square]
        if rows[int_y][int_x] == "#":
            return (x, y, facing_old)
        else:
            return (off_x+int_x, off_y+int_y, facing)
            
  
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]  
x, y = dim, 0
facing = 0
for i, steps in enumerate(moves):
    for _ in range(steps):
        x_new, y_new, facing = move2(x, y, facing)
        if x_new == x and y_new == y:
            break
        x, y = x_new, y_new
    if i < len(turns):
        turn = turns[i]
        if turn == "R":
            facing = (facing+1)%4
        else:
            facing = (facing-1)%4

print(1000*(y+1)+4*(x+1)+facing)