with open('input') as f:
    inp = f.read()

instr = {'(': 1, ')': -1}
    
# Part 1
floor = 0
for x in inp:
    floor += instr[x]

print(floor)

# Part 2
floor = 0
for i, x in enumerate(inp):
    floor += instr[x]
    if floor == -1:
        print(i+1)
        break
