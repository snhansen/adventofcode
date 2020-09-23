import re

with open('input') as f:
    inp = [x.strip() for x in f.readlines()]
    
# Part 1
count = 0
for x in inp:
    valid = True
    l = list(map(int,re.findall('\d+', x)))
    if l[0]+l[1]<=l[2] or l[0]+l[2]<=l[1] or l[1]+l[2]<=l[0]:
        valid = False
    count += int(valid)
    
print(count)

# Part 2
tmp_ls = [list(map(int,re.findall('\d+', x))) for x in inp]
ls = [l[i] for i in range(3) for l in tmp_ls ]

count = 0
i = 0
while i<len(ls):
    valid = True
    if ls[i]+ls[i+1]<=ls[i+2] or ls[i]+ls[i+2]<=ls[i+1] or ls[i+1]+ls[i+2]<=ls[i]:
        valid = False
    count += int(valid)
    i += 3
    
print(count)
