import re

with open('input') as f:
    inp = [x.strip() for x in f.readlines()]

instrs = []
for x in inp:
    temp = x.split(' ') 
    try:
        val = int(re.findall('[-+]\d+', x)[0])
    except IndexError:
        pass
    if temp[0] == 'jmp':
        instrs.append((temp[0], None, val))
    elif temp[0][0:2] == 'ji':
        instrs.append((temp[0], temp[1].strip(','), val))
    else:
        instrs.append((temp[0], temp[1].strip(','), None))

def solve(a):
    registers = {'a': a, 'b': 0}
    i = 0
    while True:
        try:
            instr, reg, val = instrs[i]
        except IndexError:
            break
        if instr == 'hlf':
            registers[reg] //= 2
            i += 1
        elif instr == 'tpl':
            registers[reg] *= 3
            i += 1
        elif instr == 'inc':
            registers[reg] += 1
            i += 1
        elif instr == 'jmp':
            i += val
        elif instr == 'jie':
            i = i + val if (registers[reg] % 2) == 0 else i+1
        elif instr == 'jio':
            i = i + val if registers[reg] == 1 else i+1
        
    return registers['b']

# Part 1
print(solve(0))    

# Part 2
print(solve(1))