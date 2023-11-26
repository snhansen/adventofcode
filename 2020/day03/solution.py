import math

with open('input') as f:
    inp = f.read()

coords = {}
i, k = 0, 0

for x in inp:
    if x != '\n':
        coords[i+1j*k] = 1 if x == '#' else 0
        i += 1
    else:
        k += 1
        i = 0

n_row = k
n_col = i

def no_trees(slope):
    c = 0
    i, k = 0, 0
    while k<=n_row:
        c += (coords[(i%n_col) + 1j*k] == 1)
        i += slope[0]
        k += slope[1]
    return c

# Part 1
print(no_trees([3,1]))

# Part 2
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
print(math.prod([no_trees(s) for s in slopes]))