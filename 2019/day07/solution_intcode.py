import sys
import os
import itertools
sys.path.insert(1, os.path.dirname(os.getcwd()))
from aoc_functions import intcode_machine


with open('input') as f:
    inp = list(map(int, f.read().split(',')))

# Part 1
phase_list = list(itertools.permutations([0, 1, 2, 3, 4]))
signals = []

for phase in phase_list:
    output = 0
    for amp in range(5):
        intcode = intcode_machine(inp, [phase[amp], output])
        output = intcode.run_till_halt()
    signals.append(output)

print(max(signals))

# Part 2
phase_list = list(itertools.permutations([5, 6, 7, 8, 9]))
signals = []
for phase in phase_list:
    intcodes = [intcode_machine(inp, [p]) for p in phase]
    outputs = [0]
    while True:
        for intcode in intcodes:
            intcode.add_inputs([outputs[-1]])
            halt, output = intcode.run_till_output_or_halt()
            outputs.append(output)
            if halt:
                break
        if halt:
            break
    signals.append(outputs[-2])
    
print(max(signals))