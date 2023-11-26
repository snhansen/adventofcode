with open('input') as f:
    inp = [x.strip() for x in f.readlines()]

rooms = []
for x in inp:
    rooms.append((''.join(x.split('[')[0].split('-')[:-1]), int(x.split('[')[0].split('-')[-1]),x.split('[')[1].strip(']')))

# Part 1
sum_ids = 0

for r in rooms:
    chars = set(r[0])
    counts = [r[0].count(x) for x in chars]
    temp = sorted(list(zip(counts, chars)))
    max_c = max(temp, key=lambda x: x[0])[0]
    temp2 = [sorted([x for x in temp if x[0] == i], reverse = True) for i in range(max_c+1)]
    first_five = ''.join(reversed([x[1] for y in temp2 for x in y if x][-5:]))
    if first_five == r[2]:
        sum_ids += r[1]

print(sum_ids)

# Part 2
for r in rooms:
    new_r = ''
    for x in r[0]:
        new_r += chr(((ord(x)-97 + r[1]) % 26) + 97)
    if 'pole' in new_r:
        print(r[1])
        break