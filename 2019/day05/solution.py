with open('input') as f:
    inp = list(map(int, f.read().split(',')))


def run(input):
    p = list(inp)
    i = 0
    while True:
        instr = str(p[i]).zfill(5)
        opcode = int(instr[3:])
        parmode = instr[0:3]
        if opcode != 99:
            x1 = p[i+1] if int(parmode[2]) else p[p[i+1]]
        if opcode in [1, 2, 5, 6, 7, 8]:
            x2 = p[i+2] if int(parmode[1]) else p[p[i+2]]
        if opcode == 99:
            print('Halted')
            break
        elif opcode == 1:
            p[p[i+3]] = x1 + x2
            i += 4
        elif opcode == 2:
            p[p[i+3]] = x1 * x2
            i += 4
        elif opcode == 3:
            p[p[i+1]] = input
            i += 2
        elif opcode == 4:
            if x1 != 0:
                return x1
            i += 2
        elif opcode == 5:
            i = x2 if x1 != 0 else i+3
        elif opcode == 6:
            i = x2 if x1 == 0 else i+3
        elif opcode == 7:
            p[p[i+3]] = 1 if x1 < x2 else 0
            i += 4
        elif opcode == 8:
            p[p[i+3]] = 1 if x1 == x2 else 0
            i += 4


# Part 1
print(run(1))

# Part 2
print(run(5))
