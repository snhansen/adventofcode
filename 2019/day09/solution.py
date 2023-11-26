def get_output(seq, input):
    output = 0
    relbase = 0
    i = 0
    while True:
        temp = str(seq[i])
        opcode = int(temp[-2:].strip())
        parmode = temp[0:len(temp)-2]
        while len(parmode) < 3:
            parmode = '0' + parmode

        mode1 = int(parmode[2])
        mode2 = int(parmode[1])
        mode3 = int(parmode[0])
        try:
            if mode1 == 0:
                index1 = seq[i+1]
            elif mode1 == 1:
                index1 = i+1
            elif mode1 == 2:
                index1 = seq[i+1] + relbase
            if mode2 == 0:
                index2 = seq[i+2]
            elif mode2 == 1:
                index2 = i+2
            elif mode2 == 2:
                index2 = seq[i+2] + relbase
            if mode3 == 0:
                index3 = seq[i+3]
            elif mode3 == 1:
                index3 = i+3
            elif mode3 == 2:
                index3 = seq[i+3] + relbase
        except IndexError:
            pass
        if opcode == 99:
            break
        elif opcode == 1:
            seq[index3] = seq[index1] + seq[index2]
            i += 4
        elif opcode == 2:
            seq[index3] = seq[index1]*seq[index2]
            i += 4
        elif opcode == 3:
            seq[index1] = input
            i += 2
        elif opcode == 4:
            output = seq[index1]
            i += 2
            break
        elif opcode == 5:
            i = seq[index2] if seq[index1] != 0 else i+3
        elif opcode == 6:
            i = seq[index2] if seq[index1] == 0 else i+3
        elif opcode == 7:
            seq[index3] = int(seq[index1] < seq[index2])
            i += 4
        elif opcode == 8:
            seq[index3] = int(seq[index1] == seq[index2])
            i += 4
        elif opcode == 9:
            relbase += seq[index1]
            i += 2
    return output


with open('input') as f:
    inp = list(map(int, f.read().split(',')))

inp = inp + [0]*1000
print(get_output(inp, 1))
print(get_output(inp, 2))
