import re

with open('input') as f:
    ls = [x.strip() for x in f.readlines()]

valid_pws_pt1 = 0
valid_pws_pt2 = 0

for l in ls:
    lower = int(re.findall('\d+', l)[0])
    upper = int(re.findall('\d+', l)[1])
    char = re.findall('(\w+)\:+', l)[0]
    pw = re.findall('\:+\s(\w+)', l)[0]
    if lower <= pw.count(char) <= upper:
        valid_pws_pt1 += 1
    if pw[lower-1] == char and pw[upper-1] != char:
        valid_pws_pt2 += 1
    if pw[lower-1] != char and pw[upper-1] == char:
        valid_pws_pt2 += 1
        
print(valid_pws_pt1)
print(valid_pws_pt2)