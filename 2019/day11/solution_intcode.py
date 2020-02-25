import sys
import os
import itertools
sys.path.insert(1, os.path.dirname(os.getcwd()))
from aoc_functions import intcode_machine


with open('input') as f:
    inp = list(map(int, f.read().split(',')))


directions = {'U': ['L', 'R'], 'D': ['R', 'L'], 'L': ['D', 'U'], 'R': ['U', 'D']}
moves = {'U': [(-1, 0), (1, 0)], 'D': [(1, 0), (-1, 0)], 'L': [(0, -1), (0, 1)], 'R': [(0, 1), (0, -1)]}


def new_pos(pos, face, turn):
    return directions[face][turn], tuple(sum(x) for x in zip(pos, moves[face][turn]))

def get_colors(start_color):
    intcode = intcode_machine(inp, [])
    face = 'U'
    pos = (0, 0)
    colors = {pos: start_color}
    while True:
        try:
            intcode.add_inputs([colors[pos]])
        except KeyError:
            intcode.add_inputs([0])
        halt1, paint = intcode.run_till_output_or_halt()
        if not halt1:
            halt2, turn = intcode.run_till_output_or_halt()
            colors[pos] = paint
            face, pos = new_pos(pos, face, turn)
        else:
            break
    
    return colors
    


# Part 1
print(len(get_colors(0)))

# Part 2
colors = get_colors(1)
xmin, xmax = min([x[0] for x in colors]), max([x[0] for x in colors])
ymin, ymax = min([x[1] for x in colors]), max([x[1] for x in colors])
paint = {0: ' ', 1: 'x'}

result = []
for y in reversed(range(ymin, ymax+1)):
    r = ''
    for x in range(xmin, xmax+1):
        try:
            r += paint[colors[(x,y)]]
        except KeyError:
            r += ' '
    result.append(r)
            

for i in range(len(result)):
    print(result[i])