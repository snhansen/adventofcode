import sys
import os
import itertools
sys.path.insert(1, os.path.dirname(os.getcwd()))
from aoc_functions import intcode_machine


with open('input') as f:
    inp = list(map(int, f.read().split(',')))


def run_program(a, b):
    intcode = intcode_machine(inp)
    intcode[1] = a
    intcode[2] = b
    intcode.run_till_halt()
    return intcode[0]


# Part 1
print(run_program(12, 2))

# Part 2
for a, b in itertools.product(range(100), range(100)):
    if run_program(a, b) == 19690720:
        print(100*a + b)
        break
