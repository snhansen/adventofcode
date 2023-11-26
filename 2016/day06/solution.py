with open('input') as f:
    inp = [x.strip() for x in f.readlines()]

s1 = ''
s2 = ''
for i in range(len(inp[0])):
    cols = [[x[i] for x in inp] for i in range(len(inp[0]))]
    max_freq = max([''.join(cols[i]).count(x) for x in set(cols[i])])
    min_freq = min([''.join(cols[i]).count(x) for x in set(cols[i])])
    s1 += [x for x in set(cols[i]) if ''.join(cols[i]).count(x) == max_freq][0]
    s2 += [x for x in set(cols[i]) if ''.join(cols[i]).count(x) == min_freq][0]

print(s1)
print(s2)