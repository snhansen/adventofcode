import sys
import os
from itertools import product
sys.path.insert(1, os.path.dirname(os.getcwd()))
from aoc_functions import intcode_machine

with open('input') as f:
    inp = list(map(int, f.read().split(',')))

# Part 1
def is_beam(x, y):
    beam = intcode_machine(inp, [x, y])
    while True:
            halt, output = beam.run_till_output_or_halt()
            if halt:
                break
    return output

print(sum([is_beam(x, y) for x, y in product(range(50), repeat=2)]))

# Part 2
size = 100

def beam_row(y, x_start):
    l = []
    x = x_start
    while True:
        temp = is_beam(x, y)
        if temp:
            l.append(x)
        if len(l)>0 and not temp:
            break
        x += 1
    return l
    
def can_fit_ship(x, y):
    return is_beam(x, y) and is_beam(x+size-1, y) and is_beam(x, y+size-1) and is_beam(x+size-1, y+size-1)
    
# A manual search with larger increments, shows that the solution is at a y-coordinate larger than 1100.
y = 1100
x_start = 0

while True:  
    xs = beam_row(y, x_start)
    if len(xs)<size:
        y += 1
        continue
    for i in range(len(xs)+1-size):
        x = xs[0] + i
        if can_fit_ship(x, y):
            print(f'x = {x}, y = {y}')
            print(x*10000+y)
            sys.exit(0)
    y += 1
    x_start = xs[0]-10