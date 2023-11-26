import sys
import os
from itertools import product
sys.path.insert(1, os.path.dirname(os.getcwd()))
from aoc_functions import intcode_machine

with open('input') as f:
    inp = list(map(int, f.read().split(',')))
    
def inspect(instr):
    instr = list(map(ord, instr))
    droid = intcode_machine(inp, instr)
    outp = []
    while True:
        halt, output = droid.run_till_output_or_halt()
        if halt:
            break
        outp.append(output)
    return outp
    
# Part 1
instr = """NOT A J
NOT B T
OR T J
NOT C T
OR T J
AND D J
WALK
"""

outp = inspect(instr)
print(outp[-1])
#print(''.join(chr(x) for x in outp))

# Part 2
instr = """NOT A T
NOT B J
OR T J
NOT C T
OR T J
AND D J
NOT D T
OR H T
OR E T
AND T J
RUN
"""

outp = inspect(instr)
print(outp[-1])