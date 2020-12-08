with open('input') as f:
    inp = [x.strip() for x in f.readlines()]

def run(ls):
    seen = set()
    acc = 0
    i = 0
    while True:
        if i == len(ls):
            terminate = True
            break
        if i in seen:
            terminate = False
            break
        instr = ls[i].split(' ')[0]
        val = int(ls[i].split(' ')[1])
        seen.add(i)
        if instr == 'nop':
            i += 1
        elif instr == 'acc':
            acc += val
            i += 1
        elif instr == 'jmp':
            i += val
     
    return terminate, acc

# Part 1
_, acc = run(inp)
print(acc)

# Part 2
for j in range(len(inp)):
    instr = inp[j].split(' ')[0]
    if instr != 'acc':
        val = inp[j].split(' ')[1]
        inp_mod = list(inp)
        inp_mod[j] = 'jmp ' + val if instr == 'nop' else 'nop ' + val
        terminate, acc = run(inp_mod)
        if terminate:
            print(acc)  
            break