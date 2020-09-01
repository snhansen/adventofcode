with open('input') as f:
    inp = f.read()

# Part 1
dirs = {'<': -1, '>': 1, '^': -1j, 'v': 1j}
visited = [0]

for x in inp:
    visited.append(visited[-1]+dirs[x])
    
print(len(set(visited)))