import re
from collections import defaultdict

with open('input') as f:
    instr = [x.strip() for x in f.readlines()]

# Part 1
bots = defaultdict(list)
outputs = defaultdict(list)
keys = 0
i = 0
while True:
    if keys == 0 and len(outputs)>0:
        break
    try:
        x = instr[i]
    except IndexError:
        i = 0
        x = instr[i]
    vals = list(map(int, re.findall('\d+', x)))
    if 'value' in x:
        bots[vals[1]].append(vals[0])
        keys += 1
        instr.remove(x)
    elif len(bots[vals[0]]) == 2:
        bots[vals[0]].sort()
        if bots[vals[0]][0] == 17 and bots[vals[0]][1] == 61:
            print(vals[0])
        if 'output' in x.split('and')[0]:
            outputs[vals[1]].append(bots[vals[0]][0])
            keys -= 1
        else:
            bots[vals[1]].append(bots[vals[0]][0])
        if 'output' in x.split('and')[1]:
            outputs[vals[2]].append(bots[vals[0]][1])
            keys -= 1
        else:
            bots[vals[2]].append(bots[vals[0]][1])
        bots[vals[0]] = []
    i += 1

# Part 2
print(outputs[0][0]*outputs[1][0]*outputs[2][0])

    
    
    
    
    