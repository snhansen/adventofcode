import re
from itertools import permutations

with open("input") as f:
    inp = f.read().strip().split("\n")

nodes = []
for line in inp:
    if line[0] != "/":
        continue
    nodes.append(tuple(map(int, re.findall("\d+", line))))

# Part 1
viable_pairs = 0
for nodea, nodeb in permutations(nodes, 2):
    _, _, _, useda, availa, _ = nodea
    _, _, _, usedb, availb, _ = nodeb
    if useda > 0 and useda <= availb:
        viable_pairs += 1

print(viable_pairs)

# Part 2

# Our grid is 38x38 so the node we have access to is at (0,0) and the node which data we want to access is at (37,0).
# Data blocks between (12,6) and (12,37) are large (490-498), and they can never fit into smaller sized nodes, 
# so they're stuck. This means we can only move data between smaller sized nodes (85-94). Since the smaller data blocks
# themselves are between 64-73 these can only be moved into an empty node. We note that all small-sized data blocks can fit
# into all nodes.
# Since there is only one empty node, we are essentially swapping data between the empty node and its neighbors.
#
# Our grid looks like this:
#
# a . . . . . . . . . . . . d
# . . . . . . . . . . . . . .
# . . . . . . . . . . . . . .
# . . . . # # # # # # # # # #
# . . . . . . . . . . . . . .
# . . . . . . . . . . . . . .
# . . . . . . . . . . . 0 . .
#
# where 
# - # denotes the large nodes which can't be moved (12,6), ..., (12,37)
# - d denotes the data we want access to (37,0)
# - a the node we have access to (0,0)
# - 0 the empty node (16,23)
#
# The goal is to move d to a. This can be achieved in two steps:
# 1. Move the empty node up next to d, so the grid looks like this:
#
# a . . . . . . . . . . . 0 d
# . . . . . . . . . . . . . .
# . . . . . . . . . . . . . .
# . . . . # # # # # # # # # #
# . . . . . . . . . . . . . .
# . . . . . . . . . . . . . .
# . . . . . . . . . . . . . .
# 
# This can be done via this path: (16,23) -> (5,23) -> (5,0) -> (36,0) which
# takes (16 - 5) + (23 - 0) + (36 - 5) steps
# 
# 2. Then we move d to left one step and then we need to move the 0 around d so it
# again is in front requiring 4 steps. This would look like this:
#
# a . . . . . . . . . . . d 0
# . . . . . . . . . . . . . .
# . . . . . . . . . . . . . .
# . . . . # # # # # # # # # #
# . . . . . . . . . . . . . .
# . . . . . . . . . . . . . .
# . . . . . . . . . . . . . .
# 
# a . . . . . . . . . . 0 d .
# . . . . . . . . . . . . . .
# . . . . . . . . . . . . . .
# . . . . # # # # # # # # # #
# . . . . . . . . . . . . . .
# . . . . . . . . . . . . . .
# . . . . . . . . . . . . . .
# 
# Each step to the left requires 5 steps and we end up with 0 in front af d. After 36*5 steps
# d is positioned at (1,0) with 0 at (0,0). After one additional step d has been moved to (0,0).
print((16 - 5) + (23 - 0) + (36 - 5) + 36*5 + 1)