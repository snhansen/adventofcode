import re

with open('input') as f:
    ls = [x.strip('\n') for x in f.readlines()]

def cut(l, k):
    if k>0:
        return(l[k:] + l[:k])
    else:
        return cut(l, len(l)+k)
    
def deal_with_inc(l, k):
    new_l = [None]*len(l)
    for i in range(len(l)):
        new_l[i*k % len(l)] = l[i]
    return new_l

# Part 1
l = list(range(10007))

for x in ls:
    if 'stack' in x:
        l.reverse()
    elif 'cut' in x:
        k = int(re.findall('.\d+', x)[0])
        l = cut(l, k)
    else:
        k = int(re.findall('.\d+', x)[0])
        l = deal_with_inc(l, k)


print(l.index(2019))

# Part 2
# The position of card x in a stack of size n after each technique is
# 1) deal into new stack: -x - 1 mod n
# 2) cut k: n - k + x mod n
# 3) deal with increment k: k*x mod n
# That is, they're all of the form ax+b mod n for some (a,b):
# 1) a = -1, b = -1,
# 2) a = 1, b = n - k,
# 3) a = k, b = 0
# Now, composing any combination of these with each other will yield
# a result of the same form; ax+b for some a and b. Let's find these.

n = 119315717514047
a, b = 1, 0
for x in ls:
    if 'stack' in x:
        a2 = -1
        b2 = -1
    elif 'cut' in x:
        k = int(re.findall('.\d+', x)[0])
        a2 = 1
        b2 = n - k
    else:
        k = int(re.findall('.\d+', x)[0])
        a2 = k
        b2 = 0
    a = (a*a2) % n
    b = (b*a2 + b2) % n

# One round of shuffling (according to the input instructions) moves card x to position 7984*x+2815 mod 10007.
# If we repeat this round of shuffling m times, then we will have moved card x to position a^m*x + b*(a^(m-1)+a^(m-2)+...+1) mod n.
# Since a^(m-1)+a^(m-2)+...+1 = (a^m-1)/(a-1) (it's a geometric series), we conclude that after m rounds card x ends up
# at position pos(x) = a^m*x + b(a^m-1)/(a-1) mod n. 
# We need to calculate a^m and 1/(1-a) mod n. For this we use this taken from elsewhere.
def inv(a, n): return pow(a, n-2, n)

# The puzzle then asks us to solve pos(x) = 2020 which has solution 
# x = (2020 - b(a^m-1)/(a-1))/a^m mod n.
m = 101741582076661
pos_a = pow(a, m, n)
pos_b = b*(pos_a-1)*inv(a-1, n) % n
print((2020-pos_b)*inv(pos_a, n) % n)