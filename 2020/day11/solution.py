from collections import Counter

with open('input') as f:
    inp = f.read()

seats = {}
i, j = 0, 0
for x in inp:
    if x != '\n':
        seats[i+1j*j] = x
        i += 1
    else:
        i = 0
        j += 1

c = max([int(x.real) for x in seats.keys()])
r = max([int(x.imag) for x in seats.keys()])

def get_occ(d, p, part2 = False):
    if not part2:
        return Counter(d[p+x+y*1j] for x in (-1, 0, 1) for y in (-1, 0, 1) if x+y*1j != 0 and 0 <= (p+x+y*1j).real <= c and 0 <= (p+x+y*1j).imag <= r)['#']
    else:
        n = 0
        for q in (x+y*1j for x in (-1, 0, 1) for y in (-1, 0, 1) if x+y*1j != 0):
            k = 1
            while True:
                try:
                    if d[p+k*q] != '.':
                        n += (d[p+k*q] == '#')
                        break
                except KeyError:
                    break
                k += 1
        return n

def update_seats(d, part2 = False):
    d_new = dict(d)
    cut = 5 if part2 else 4
    for p in d:
        if d[p] == 'L' and get_occ(d, p, part2) == 0:
            d_new[p] = '#'
        elif d[p] == '#' and get_occ(d, p, part2) >= cut:
            d_new[p] = 'L'
    return d_new

        
def solve(d, part2 = False):
    while True:
        old_d = d
        d = update_seats(d, part2)
        if d == old_d:
            return list(d.values()).count('#')

# Part 1
print(solve(seats))

# Part 2
print(solve(seats, True))