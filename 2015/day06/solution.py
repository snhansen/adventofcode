with open('input') as f:
    inp = [x.strip() for x in f.readlines()]

n = 1000    

# Part 1
lights = [[0]*n for i in range(n)]

for row in inp:
    end = [int(x) for x in row.split(' through ')[1].split(',')]
    start = [int(x) for x in row.split(' through ')[0].split(' ')[-1].split(',')]
    for i in range(start[0], end[0]+1):
        for j in range(start[1], end[1]+1):
            if 'on' in row:
                lights[j][i] = 1
            elif 'off' in row:
                lights[j][i] = 0
            else:
                lights[j][i] = (lights[j][i] + 1) % 2
                
print(sum([sum(x) for x in lights]))

# Part 2
lights = [[0]*n for i in range(n)]

for row in inp:
    end = [int(x) for x in row.split(' through ')[1].split(',')]
    start = [int(x) for x in row.split(' through ')[0].split(' ')[-1].split(',')]
    for i in range(start[0], end[0]+1):
        for j in range(start[1], end[1]+1):
            if 'on' in row:
                lights[j][i] += 1
            elif 'off' in row:
                lights[j][i] -= 1 if lights[j][i] else 0
            else:
                lights[j][i] += 2
                
print(sum([sum(x) for x in lights]))