import re
from collections import deque

with open('input') as f:
    s = f.read().strip()

# Part 1
res = ''
i = 0
while True:
    if i > len(s)-1:
        break
    if s[i] == '(':
        j = i
        while True:
            if s[j] == ')':
                break
            j += 1
        vals = list(map(int, s[i+1:j].split('x')))
        res += ''.join([s[j+1:j+vals[0]+1] for k in range(vals[1])])
        i = j+vals[0]+1
    else:
        i += 1

print(len(res))

# Part 2
def decompress(s, m):
    res = re.search('\(\w+\)', s)
    if res:
        x = res.span()[0]
        y = res.span()[1]
        length, rep = list(map(int, res.group(0)[1:-1].split('x')))
        new_ls = []
        if x > 0:
            new_ls.append((s[0: x], 1))
        new_ls.append((s[y: y+length], rep*m))
        if y+length < len(s):
            new_ls.append((s[y+length: len(s)], 1*m))
        return new_ls



to_check = deque()
to_check.append((s, 1))
done = []

while to_check:
    s, m = to_check.popleft()
    res = decompress(s, m)
    if not res:
        done.append((s, m))
    else:
        to_check.extend(res)

print(sum([len(s)*m for s, m in done]))