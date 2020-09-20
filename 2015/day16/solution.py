with open('input') as f:
    inp = [x.strip() for x in f.readlines()]

sues = []  
for x in inp:
    d = {}
    temp = x.split(' ')
    i = 2
    while i<len(temp)-1:
        d[temp[i].strip(':')] = int(temp[i+1].strip(','))
        i += 2
    sues.append(d)

with open('msg') as f:
    msg = [x.strip() for x in f.readlines()]

comps = [[l.split(' ')[0].strip(':'), int(l.split(' ')[1])] for l in msg]

# Part 1
for i, sue in enumerate(sues):
    gift_sue = True
    for comp in comps:
        try:
            if sue[comp[0]] != comp[1]:
                gift_sue = False
                break
        except KeyError:
            pass
    if gift_sue:
        print(i+1)
        break

# Part 2
for i, sue in enumerate(sues):
    gift_sue = True
    for comp in comps:
        if comp[0] in ['cats', 'trees']:
            try:
                if sue[comp[0]] <= comp[1]:
                    gift_sue = False
                    break
            except KeyError:
                pass
        elif comp[0] in ['pomeranians', 'goldfish']:
            try:
                if sue[comp[0]] >= comp[1]:
                    gift_sue = False
                    break
            except KeyError:
                pass
        else:
            try:
                if sue[comp[0]] != comp[1]:
                    gift_sue = False
                    break
            except KeyError:
                pass
    if gift_sue:
        print(i+1)
        break

