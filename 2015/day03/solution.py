with open('input') as f:
    inp = f.read()

# Part 1
dirs = {'<': -1, '>': 1, '^': -1j, 'v': 1j}
visited = [0]

for x in inp:
    visited.append(visited[-1]+dirs[x])
    
print(len(set(visited)))

# Part 2
visit1 = [0]
visit2 = [0]
for i, x in enumerate(inp):
    if i%2 == 0:
        visit1.append(visit1[-1]+dirs[x])
    else:
        visit2.append(visit2[-1]+dirs[x])

print(len(set(visit1+visit2)))

    