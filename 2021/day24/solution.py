from math import prod

# The input is divided into sections given by when an input is required. Each section requires a digit input (integer between 1 and 9) stored in w and then performs some operations on x, y, z and w. In the first section, x, y and z are initialized as 0. Their result at the end of a section is carried forward to the next section. First thing to note is that, in all sections, the first operation involving x is multiplication by 0, so it's initial value is irrelevant. The same goes for y. Thus, the two relevant parameters to keep track of is z and w.

# Although not really necessary, here's the resulting function from each section (seen as a function of (x,y,z,w)):

with open('input') as f:
    inp = f.read().strip().split('inp w')

del inp[0]
sections = []
for x in inp:
    x = x.split('\n')
    for y in x:
        if not y:
            x.remove(y)
    sections.append(x)

operators = {'mul': prod, 'add': sum, 'div': lambda ls: ls[0] // ls[1], 'mod': lambda ls: ls[0] % ls[1], 'eql': lambda ls: int(ls[0] == ls[1])}


def func(digit, ls):
    res = {c: ls[i] for i, c in enumerate('xyzw')}
    for line in sections[digit]:
        instr, v1, v2 = line.split()
        if v2.isnumeric() or v2[1:].isnumeric():
            res[v1] = operators[instr]([res[v1], int(v2)])
        else:
            res[v1] = operators[instr]([res[v1], res[v2]])
    return list(res.values())

# After manually going through the operations in each section, we realize that the sections correspond to two types of functions (here f denotes the value of z at the end of the section which is a function of z and w at the beginning of the section). The first type is f(w,z) = a+w+26*z and the second type is f(w,z) = z//26 if "condition" else (z//26)*26+w+a. Here "condition" is a requirement of the form (z-a-w) & 26 == 0. The exact functions are given here:

def test(digit, ls):
    x, y, z, w = ls
    if digit == 0:
        return [1, 9+w, 9+w+26*z, w]
    if digit == 1:
        return [1, 4+w, 4+w+26*z, w]
    if digit == 2:
        return [1, 2+w, 2+w+26*z, w]
    if digit == 3:
        cond = (z-9-w) % 26 == 0
        return [0 if cond else 1, 0 if cond else w+5, z//26 if cond else (z//26)*26+w+5, w]
    if digit == 4:
        cond = (z-9-w) % 26 == 0
        return [0 if cond else 1, 0 if cond else w+1, z//26 if cond else (z//26)*26+w+1, w]
    if digit == 5:
        return [1, 6+w, 6+w+26*z, w]
    if digit == 6:
        return [1, 11+w, 11+w+26*z, w]
    if digit == 7:
        cond = (z-10-w) % 26 == 0
        return [0 if cond else 1, 0 if cond else w+15, z//26 if cond else (z//26)*26+w+15, w]
    if digit == 8:
        return [1, 7+w, 7+w+26*z, w]
    if digit == 9:
        cond = (z-2-w) % 26 == 0
        return [0 if cond else 1, 0 if cond else w+12, z//26 if cond else (z//26)*26+w+12, w]
    if digit == 10:
        return [1, 15+w, 15+w+26*z, w]
    if digit == 11:
        cond = (z-15-w) % 26 == 0
        return [0 if cond else 1, 0 if cond else w+9, z//26 if cond else (z//26)*26+w+9, w]
    if digit == 12:
        cond = (z-9-w) % 26 == 0
        return [0 if cond else 1, 0 if cond else w+12, z//26 if cond else (z//26)*26+w+12, w]
    if digit == 13:
        cond = (z-3-w) % 26 == 0
        return [0 if cond else 1, 0 if cond else w+12, z//26 if cond else (z//26)*26+w+12, w]


# We verify that this corresponds to what we will get by manually applying each operation:
for digit in range(14):
    for z in range(1000):
        for w in range(1,10):
            ls = [0,0,z,w]   
            assert func(digit, ls) == test(digit, ls)


# Since there are 7 of the first type and 7 of the second type, the only way we can have a z-value of 0 at the end of all 14 sections is if the "condition" is satisfied for all 7 of the functions of the second type. We thus only need to decipher what these conditions are.

# This we do manually:
# ---------------------------
# step 0
# z0 = 9+d0

# step 1
# z1 = 4+d1+26*z0 = 4+d1+26*(9+d0)

# step 2
# z2 = 2+d2+26*z1

# step 3
# cond 1: 
# (z2-9-d3) % 26 == 0
# (2+d2-9-d3) % 26 == 0
# d2 = d3+7

# z3 = z1

# step 4:
# cond 2:
# (z3-9-d4) % 26 == 0
# (4+d1-9-d4) % 26 == 0
# d1 = d4+5

# z4 = z0

# step 5:
# z5 = 6+d5+26*z0

# step 6:
# z6 = 11+d6+26*z5

# step 7:
# cond 3
# (z6-10-d7) % 26 ==0
# (11+d6-10-d7) % 26 == 0
# d6 = d7-1

# z7 = z5

# step 8:
# z8 = 7+d8+26*z5

# step 9:
# cond 4: 
# (z8-2-d9) % 26 == 0
# (7+d8-2-d9) % 26 == 0
# d8 = d9-5

# z9 = z5

# step 10:
# z10 = 15+d10+26*z5

# step 11:
# cond 5: 
# (z10-15-d11) % 26 == 0
# (15+d10-15-d11) % 26 == 0
# d10 = d11

# z11 = z5

# step 12:
# cond 6: 
# (z5-9-d12) % 26 == 0
# (6+d5-9-d12) % 26 == 0
# d5 = d12+3

# z12 = z0

# step 13:
# cond 7: 
# (z0-3-d13) % 26 == 0
# (9+d0-3-d13) % 26 == 0
# d0 = d13-6

# z13 = 0

# ---------------------------

# We thus end up with 7 requirements: d2=d3+7, d1=d4+5, d7=d6+1, d9=d8+5, d10=d11, d5=d12+3 ,d13 = d0+6.
# This yields a maximum and minimum number satisfying these conditions of 39924989499969 and 16811412161117 respectively.