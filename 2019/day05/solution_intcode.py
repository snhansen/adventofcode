import sys
import os
sys.path.insert(1, os.path.dirname(os.getcwd()))
from aoc_functions import intcode_machine


with open('input') as f:
    inp = list(map(int, f.read().split(',')))


def run_program(a):
    intcode = intcode_machine(inp, [a])
    return intcode.run_till_halt()


# Part 1
print(run_program(1))

# Part 2
print(run_program(5))


