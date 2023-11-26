with open('input') as f:
    inp = f.readlines()

# Part 1
dirs = {'forward': 1, 'down': -1j, 'up': 1j}
pos = 0

for x in inp:
    d, v = x.strip().split()
    v = int(v)
    pos += v*dirs[d]

print(int(abs(pos.imag)*abs(pos.real)))

# Part 2
aim = pos = 0

for x in inp:
    d, v = x.strip().split()
    v = int(v)
    if d != 'forward':
        aim = aim+v if d == 'down' else aim-v
    else:
        pos += v+aim*v*1j

print(int(abs(pos.imag)*abs(pos.real)))
    