with open('input') as f:
    inp = [x.strip() for x in f.read().split(',')]
      
# Part 1
dirs = [1j, 1, -1j, -1]
dir = 0
p = 0
for x in inp:
    val = 1 if x[0] == 'R' else -1
    dir = ((dir + val) % len(dirs))
    p += int(x[1:])*dirs[dir]

print(int(abs(p.real)+abs(p.imag)))

# Part 2
def solve():
    visited = set()
    dir = 0
    p = 0
    for x in inp:
        val = 1 if x[0] == 'R' else -1
        dir = ((dir + val) % len(dirs))
        dist = int(x[1:])
        for _ in range(dist):
            p += dirs[dir]
            if p in visited:
                return int(abs(p.real)+abs(p.imag))
            visited.add(p)
    
print(solve())