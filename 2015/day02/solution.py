with open('input') as f:
    inp = [x.strip() for x in f.readlines()]

# Part 1
paper = 0
for x in inp:
    dims = list(sorted(map(int, x.split('x'))))
    paper += 3*dims[0]*dims[1] + 2*dims[1]*dims[2] + 2*dims[0]*dims[2]
    
print(paper)

# Part 2
ribbon = 0
for x in inp:
    dims = list(sorted(map(int, x.split('x'))))
    ribbon += 2*dims[0] + 2*dims[1] + dims[0]*dims[1]*dims[2]
    
print(ribbon)