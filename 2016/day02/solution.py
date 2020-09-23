with open('input') as f:
    inp = [x.strip() for x in f.readlines()]

move = {'D': 1j, 'U': -1j, 'R': 1, 'L': -1}
numpad = {0: 1, 1: 2, 2: 3, 1j: 4, 1+1j: 5, 2+1j: 6, 2j: 7, 1+2j: 8, 2+2j: 9}

# Part 1
pos = 1+1j
code = []
for line in inp:
    for x in line:
        if 0<=(pos+move[x]).real<=2 and 0<=(pos+move[x]).imag<=2:
            pos += move[x]
    code.append(numpad[pos])

print(''.join([str(c) for c in code]))

# Part 2
numpad = {-2j: '1', -1-1j: '2', -1j: '3', 1-1j: '4', -2: '5', -1: '6', 0: '7', 1: '8', 2: '9', -1+1j: 'A', 1j: 'B', 1+1j: 'C', 2j: 'D'}
pos = -2
code = []
for line in inp:
    for x in line:
        try:
            key = numpad[pos+move[x]]
            pos = pos+move[x]
        except KeyError:
            pass
    code.append(numpad[pos])

print(''.join([str(c) for c in code]))