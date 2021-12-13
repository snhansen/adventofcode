from collections import defaultdict

with open('input') as f:
    inp = f.read().strip()

inp1, inp2 = inp.split('\n\n')

paper = defaultdict(int)
for l in inp1.split():
    x, y = l.split(',')
    paper[int(x)+int(y)*1j] = 1

folds = []
for f in inp2.split('\n'):
    x, y = f.strip('fold along ').split('=')
    folds.append((x,int(y)))

def print_paper(p, dims):
    chars = {0: '.', 1: '#'}
    for r in range(dims[0]+1):
        print(''.join([chars[p[c+r*1j]] for c in range(dims[1]+1)]))


def fold(p, dims, fold):
    axis, val = fold
    if axis == 'y':
        dims = (val-1, dims[1])
        for r in range(dims[0]+1):
            for c in range(dims[1]+1):
                if p[c+(2*val-r)*1j] == 1:
                    p[c+r*1j] = 1
                    
    elif axis == 'x':
        dims = (dims[0], val-1)
        for r in range(dims[0]+1):
            for c in range(dims[1]+1):
                if p[2*val-c+r*1j] == 1:
                    p[c+r*1j] = 1
    return p, dims


dims = (int(max([x.imag for x in paper.keys()])), int(max([x.real for x in paper.keys()])))
for i, f in enumerate(folds):
    paper, dims = fold(paper, dims, f)
    if i == 0:
        print(sum([paper[c+r*1j] for r in range(dims[0]+1) for c in range(dims[1]+1)]))
    
print_paper(paper, dims)