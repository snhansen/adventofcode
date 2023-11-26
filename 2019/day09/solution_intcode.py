import sys
import os
sys.path.insert(1, os.path.dirname(os.getcwd()))
from aoc_functions import intcode_machine


with open('input') as f:
    inp = list(map(int, f.read().split(',')))

intcode = intcode_machine(inp, [1])
intcode.run_till_halt()
print(intcode.output)

intcode = intcode_machine(inp, [2])
intcode.run_till_halt()
print(intcode.output)
