with open('input') as f:
	inp = [x.strip() for x in f.readlines()]

pos = 0
face = 'E'
faces = ['N', 'E', 'S', 'W']
dirs = {'N': -1j, 'S': 1j, 'E': 1, 'W': -1}

# Part 1
for x in inp:
	act = x[0]
	val = int(x[1:])
	if act in dirs:
		pos += dirs[act]*val
	elif act == 'F':
		pos += dirs[face]*val
	else:
		turn = val/90 if act == 'R' else -val/90
		face = faces[(faces.index(face) + int(turn))%len(faces)]


print(int(abs(pos.real)+abs(pos.imag)))

# Part 2
rots = {'R': 1j, 'L': -1j}
wayp = 10-1j
ship = 0

for x in inp:
	act = x[0]
	val = int(x[1:])
	if act in dirs:
		wayp += dirs[act]*val
	elif act == 'F':
		ship += val*wayp
	else:
		wayp *= (rots[act]**(val/90))

print(int(abs(ship.real)+abs(ship.imag)))