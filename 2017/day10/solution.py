from functools import reduce

with open("input") as f:
    inp = f.read().strip()

lengths = list(map(int, inp.split(",")))

# Part 1
ls = list(range(256))
n = len(ls)
p = 0
skip_size = 0
for l in lengths:
    if p + l <= n:
        sub_ls = ls[p:(p+l)]
        ls = ls[:p] + sub_ls[::-1] + ls[p+l:]
    else:
        rev = ls[p:] + ls[:(l-(n-p))]
        rev = rev[::-1]
        rest = ls[(l-(n-p)):p]
        ls = rev[(n-p):] + rest + rev[:(n-p)]
    p += l + skip_size
    p %= n
    skip_size += 1


print(ls[0]*ls[1])

# Part 2
ascii_lengths = [ord(c) for c in inp]
ascii_lengths += [17, 31, 73, 47, 23]

ls = list(range(256))
n = len(ls)
p = 0
skip_size = 0
for _ in range(64):
    for l in ascii_lengths:
        if p + l <= n:
            sub_ls = ls[p:(p+l)]
            ls = ls[:p] + sub_ls[::-1] + ls[p+l:]
        else:
            rev = ls[p:] + ls[:(l-(n-p))]
            rev = rev[::-1]
            rest = ls[(l-(n-p)):p]
            ls = rev[(n-p):] + rest + rev[:(n-p)]
        p += l + skip_size
        p %= n
        skip_size += 1

res = ""
for i in range(0, 16):
    block = reduce(lambda x, y: x ^ y, ls[16*i:16*(i+1)])
    h = hex(block)[2:]
    if len(h) == 1:
        h = "0" + h
    res += h

print(res)