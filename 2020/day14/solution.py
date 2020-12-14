import re
from itertools import product

with open('input') as f:
    inp = f.read().splitlines()

mem = {}

for line in inp:
    if 'mask' in line:
        mask = line.split(' = ')[1]
    else:
        index = int(re.findall('\d+', line)[0])
        val = int(re.findall('\d+', line)[1])
        binval = '{0:036b}'.format(val)
        for i, x in enumerate(mask):
            if x != 'X':
                binval = binval[:i] + x + binval[i+1:]
        mem[index] = int(binval, 2)
 
print(sum(mem.values()))

mem = {}

for line in inp:
    if 'mask' in line:
        mask = line.split(' = ')[1]
    else:
        index = int(re.findall('\d+', line)[0])
        val = int(re.findall('\d+', line)[1])
        binindex = '{0:036b}'.format(index)
        for i, x in enumerate(mask):
            if x != '0':
                binindex = binindex[:i] + x + binindex[i+1:]
        xs = [i for i in range(len(binindex)) if binindex[i] == 'X']
        for x in product([0, 1], repeat = len(xs)):
            addr = binindex
            for i, j in enumerate(xs):
                addr = addr[:j] + str(x[i]) + addr[j+1:]
            mem[int(addr, 2)] = val
       
print(sum(mem.values()))