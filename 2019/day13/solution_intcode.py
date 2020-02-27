import sys
import os
import numpy as np
sys.path.insert(1, os.path.dirname(os.getcwd()))
from aoc_functions import intcode_machine


with open('input') as f:
    inp = list(map(int, f.read().split(',')))

# Part 1
intcode = intcode_machine(inp, [])
blocktiles = 0

while True:
    halt, x = intcode.run_till_output_or_halt()
    if halt:
        break
    else:
        _, y = intcode.run_till_output_or_halt()
        _, id = intcode.run_till_output_or_halt()
        blocktiles += id == 2

print(blocktiles)


# Part 2
intcode = intcode_machine(inp, [])
intcode[0] = 2
x_paddle = 0
x_ball = 0
score = 0

while True:
    halt, x = intcode.run_till_output_or_halt()
    _, y = intcode.run_till_output_or_halt()
    _, id = intcode.run_till_output_or_halt()
    if x == -1 and y == 0:
        score = id
    elif id == 3:
        x_paddle = x
    elif id == 4:
        x_ball = x
    intcode.set_inputs([np.sign(x_ball-x_paddle)])
    if halt:
        break

print(score)
