with open('input') as f:
    inp = f.readlines()

# Part 1
dirs = {'forward': 1, 'down': -1j, 'up': 1j}
pos = 0

for x in inp:
    d = x.strip().split(' ')[0]
    v = int(x.strip().split(' ')[1])
    pos += v*dirs[d]

print(int(abs(pos.imag)*abs(pos.real)))

# Part 2
aim = 0
pos = 0

for x in inp:
    d = x.strip().split(' ')[0]
    v = int(x.strip().split(' ')[1])
    if d != 'forward':
        aim = aim+v if d == 'down' else aim-v
    else:
        pos += v+aim*v*1j

print(int(abs(pos.imag)*abs(pos.real)))
    