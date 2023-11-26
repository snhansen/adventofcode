import sys
import os
sys.path.insert(1, os.path.dirname(os.getcwd()))
from aoc_functions import intcode_machine


with open('input') as f:
    inp = list(map(int, f.read().split(',')))

# Part 1    
ascii = intcode_machine(inp, [])
outp = []

while True:
    halt, output = ascii.run_till_output_or_halt()
    if halt:
        break
    outp.append(output)

print(''.join(chr(x) for x in outp))

scaffs = []
i, j = 0, 0
for o in outp:
    if o == 35:
        scaffs.append(complex(i, j))
    i += 1
    if o == 10:
        j += 1
        i = 0
    
def no_neighbors(p):
    count = 0
    return len(set(scaffs).intersection({p+1, p-1, p+1j, p-1j}))

print(sum([int(x.real*x.imag) for x in scaffs if no_neighbors(x)>2]))

# Part 2
# This part is done by brute force by looking at the map of scaffolds.
routine = 'A,B,A,C,B,C,A,B,A,C\n'
f1 = 'R,10,L,8,R,10,R,4\n'
f2 = 'L,6,L,6,R,10\n'
f3 = 'L,6,R,12,R,12,R,10\n'
y = list(map(ord, routine+f1+f2+f3+'n\n'))

ascii = intcode_machine(inp, y)
ascii[0] = 2
outp = []
while True:
    halt, output = ascii.run_till_output_or_halt()
    if halt:
        break
    outp.append(output)

#print(''.join(chr(x) for x in outp))
print(outp[len(outp)-1])

