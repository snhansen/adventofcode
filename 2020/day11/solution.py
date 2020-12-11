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

def get_occ(d, p, part2 = False):
    c = 0
    for q in [-1-1j, -1, -1+1j, -1j, 1j, 1+1j, 1, 1-1j]:
        if not part2:
            try:
                if d[p+q] == '#':
                    c += 1
            except KeyError:
                continue
        else:
            k = 1
            while True:
                try:
                    if d[p+k*q] != '.':
                        c += (d[p+k*q] == '#')
                        break
                except KeyError:
                    break
                k += 1
    return c

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
    seen = [d]
    while True:
        d = update_seats(d, part2)
        if d in seen:
            return list(d.values()).count('#')
        seen.append(d)

# Part 1
print(solve(seats))

# Part 2
print(solve(seats, True))