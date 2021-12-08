from collections import defaultdict

with open('input') as f:
    inp = f.readlines()

# Part 1
print(len([y for l in inp for y in l.strip().split(' | ')[1].split() if len(y) in [2, 4, 3, 7]]))

# Part 2
def get_number(s, seg):
    vals = ''.join(sorted([str(seg[x]) for x in s]))
    if vals == '012456':
        return '0'
    elif vals == '25':
        return '1'
    elif vals == '02346':
        return '2'
    elif vals == '02356':
        return '3'
    elif vals == '1235':
        return '4'
    elif vals == '01356':
        return '5'
    elif vals == '013456':
        return '6'
    elif vals == '025':
        return '7'
    elif vals == '0123456':
        return '8'
    elif vals == '012356':
        return '9'

output = []
for l in inp:
    lhs, rhs = l.strip().split(' | ')
    lhs = lhs.split()
    rhs = rhs.split()
    d = defaultdict(list)
    for x in lhs:
        d[len(x)].append(set(x))

    segments = {}
    x, = d[3][0] - d[2][0]
    segments[x] = 0
    x, = d[4][0].intersection(*d[5])
    segments[x] = 3
    x, = set.intersection(*(d[5] + d[6])) - set(segments.keys())
    segments[x] = 6
    x, = d[2][0].intersection(*d[6])
    segments[x] = 5
    x, = d[4][0].intersection(d[2][0]) - set(segments.keys())
    segments[x] = 2
    x, = set.intersection(*d[6]) - set(segments.keys())
    segments[x] = 1
    x, = d[7][0] - set(segments.keys())
    segments[x] = 4

    output.append(int(''.join([get_number(x, segments) for x in rhs])))

print(sum(output))