from collections import deque
import re
import copy

with open("input") as f:
    inp = f.readlines()

stacks = [[] for _ in range(len(inp[0])//4)]
moves = []
for line in inp:
    for i in range(0,len(line),4):
        if line[i] == "[":
            stacks[i//4].append(line[i+1])
    if "move" in line:
        moves.append(list(map(int, re.findall("\d+", line))))

stacks = list(map(deque, stacks))

# Part 1
stacks_cp = copy.deepcopy(stacks)
for move in moves:
    n, fr, to = move
    for _ in range(n):
        stacks_cp[to-1].appendleft(stacks_cp[fr-1].popleft())

print(''.join([stack[0] for stack in stacks_cp]))

# Part 2
stacks_cp = copy.deepcopy(stacks)
for move in moves:
    n, fr, to = move
    stack = []
    for _ in range(n):
        stack.append(stacks_cp[fr-1].popleft())
    stacks_cp[to-1].extendleft(reversed(stack))

print(''.join([stack[0] for stack in stacks_cp]))