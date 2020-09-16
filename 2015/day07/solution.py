with open('input') as f:
    inp = [x.strip() for x in f.readlines()]

instructions = []
for x in inp:
    if 'AND' in x or 'OR' in x:
        for word in ['AND', 'OR']:
            if word in x:
                op = word
                temp = [x.split(' -> ')[0].split(f' {word} ')[0], x.split(' -> ')[0].split(f' {word} ')[1]]
                i = [y for y in temp if y.isalpha()]
                v = [int(y) for y in temp if y.isnumeric()]
                o = x.split(' -> ')[1]
    elif 'LSHIFT' in x or 'RSHIFT' in x:
        for word in ['LSHIFT', 'RSHIFT']:
            if word in x:
                op = word
                temp = [x.split(' -> ')[0].split(f' {word} ')[0], x.split(' -> ')[0].split(f' {word} ')[1]]
                i = [y for y in temp if y.isalpha()]
                v = [int(y) for y in temp if y.isnumeric()]
                o = x.split(' -> ')[1]
                break

    elif 'NOT' in x:
        op = 'NOT'
        i = [x.split(' -> ')[0].split(' ')[1]]
        o = x.split(' -> ')[1]
        v = []
            
    else:
        op = ''
        i = [x.split(' -> ')[0]]
        o = x.split(' -> ')[1]
        v = []
    instructions.append([op, i, v, o])

# Part 1
def get_signals(b = None):
    signals = {}
    instr = list(instructions)
    for x in instr:
        if b:
            if x[3] == 'b':
                x[1][0] = str(b)
        if x[0] == '' and x[1][0].isnumeric():
            signals[x[3]] = int(x[1][0])
            instr.remove(x)

    i = 0
    while instr:
        try:
            x = instr[i]
        except IndexError:
            i = 0
            continue
        if len([w for w in x[1] if w in signals]) == len(x[1]):
            if x[0] == 'AND':
                if len(x[1]) == 2:
                    signals[x[3]] = signals[x[1][0]] & signals[x[1][1]]
                else:
                    signals[x[3]] = signals[x[1][0]] & x[2][0]
            elif x[0] == 'OR':
                signals[x[3]] = signals[x[1][0]] | signals[x[1][1]]
            elif x[0] == 'LSHIFT':
                signals[x[3]] = signals[x[1][0]] << x[2][0]
            elif x[0] == 'RSHIFT':
                signals[x[3]] = signals[x[1][0]] >> x[2][0]
            elif x[0] == 'NOT':
                signals[x[3]] = ~ signals[x[1][0]]
            else:
                signals[x[3]] = signals[x[1][0]]
                
            instr.remove(x)
        else:
            i += 1
    return signals

signals = get_signals()
print(signals['a'])

# Part 2
signals_new = get_signals(signals['a'])
print(signals_new['a'])