# We decode the program to the following loop which operates on
# registers 3 and 4 (d and e).
# After each iteration the program halts if the first register
# is equal to d. We keep of track of the values of d after 
# each iteration and notices that the values are cyclic.

d_init = 2176960
e = 65536
seen = []
while True:
    d = d_init
    while e >= 256:
        d = (((d + (e & 255)) & 16777215) * 65899) & 16777215
        e = e // 256
    d = (((d + (e & 255)) & 16777215) * 65899) & 16777215
    if d in seen:
        break
    seen.append(d)
    e = d | 65536

# Part 1
# This is just the first possible d value.
print(seen[0])

# Part 2
# This is the last d value before entering the cycle.
print(seen[-1])