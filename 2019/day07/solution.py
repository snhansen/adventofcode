import itertools
    
def get_output(seq, start, inputs):
    halt = 0
    output = 0
    input_count = 0
    i = start
    while True:
        temp = str(seq[i])
        opcode = int(temp[-2:].strip())
        parmode = temp[0:len(temp)-2]
        while len(parmode) < 3:
            parmode = '0' + parmode

        mode1 = parmode[2]
        mode2 = parmode[1]
        mode3 = parmode[0] 
        try:
            x1 = seq[i+1] if int(mode1) else seq[seq[i+1]]
            x2 = seq[i+2] if int(mode2) else seq[seq[i+2]]
        except IndexError:
            pass
        if opcode == 99:
            halt = 1
            break
        elif opcode == 1:
            seq[seq[i+3]] = x1+x2
            i += 4
        elif opcode == 2:
            seq[seq[i+3]] = x1*x2
            i += 4
        elif opcode == 3:
            seq[seq[i+1]] = inputs[1] if input_count else inputs[0]
            i += 2
            input_count += 1
        elif opcode == 4:
            output = x1
            i += 2
            break
        elif opcode == 5:
            i = x2 if x1 != 0 else i+3
        elif opcode == 6:
            i = x2 if x1 == 0 else i+3
        elif opcode == 7:
            seq[seq[i+3]] = int(x1 < x2)
            i += 4
        elif opcode == 8:
            seq[seq[i+3]] = int(x1 == x2)
            i += 4
    return i, output, halt

with open('input') as f:
    raw_input = list(map(int, f.read().split(',')))

# Part 1
phase_list = list(itertools.permutations([0, 1, 2, 3, 4]))
signals = []

for phase in phase_list:
    output = 0
    for amp in range(5):
        seq = list(raw_input)
        inputs = [phase[amp], output]
        _, output, _ = get_output(seq, 0, inputs)
    signals.append(output)

print(max(signals))

# Part 2
phase_list = list(itertools.permutations([5, 6, 7, 8, 9]))
signals = []

for phase in phase_list:
    output = 0
    amp = 0
    seq = [list(raw_input), list(raw_input), list(raw_input), list(raw_input), list(raw_input)]
    start = [0, 0, 0, 0, 0]
    i = 0
    while True:
        inputs = [output, output] if i > 4 else [phase[amp], output]
        x, y, halt = get_output(seq[amp], start[amp], inputs)
        if halt and amp == 4:
            break
        elif not halt:
            start[amp] = x
            output = y
        amp = (amp + 1) % 5
        i += 1
    signals.append(output)

print(max(signals))