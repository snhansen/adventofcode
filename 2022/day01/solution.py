with open('input') as f:
    inp = f.read()

elves = inp.split('\n\n')
cals = [sum(map(int, elf.split('\n'))) for elf in elves]
cals.sort()

# Part 1
print(cals[-1])

# Part 2
print(sum(cals[-3:]))