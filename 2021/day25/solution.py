with open('input') as f:
    inp = f.read().split('\n')


region = {}
for r, line in enumerate(inp):
    for c, x in enumerate(line):
        region[c+r*1j] = x

cmax = int(max(p.real for p in region))
rmax = int(max(p.imag for p in region))


def update_region(d):
    new_d = dict(d)
    east = [p for p, val in d.items() if val == '>']
    south = [p for p, val in d.items() if val == 'v']
    for p in east:
        next_p = (p.real+1)%(cmax+1) + p.imag*1j
        if d[next_p] == '.':
            new_d[next_p] = '>'
            new_d[p] = '.'
    
    d = dict(new_d)
    for p in south:
        next_p = p.real + ((p.imag+1)%(rmax+1))*1j
        if d[next_p] == '.':
            new_d[next_p] = 'v'
            new_d[p] = '.'
            
    return new_d


c = 0
while True:
    c += 1
    new_region = update_region(region)
    if new_region == region:
        print(c)
        break
    region = new_region