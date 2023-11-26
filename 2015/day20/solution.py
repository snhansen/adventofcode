from functools import reduce
inp = 33100000

# Part 1
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def presents(n):
    fs = factors(n)
    return sum([f*10 for f in fs])

i = 1
while True:
    if presents(i) >= inp:
        print(i)
        break
    i += 1

# Part 2
def factors_v2(n):
    return [x for x in factors(n) if n<=x*50]

def presents_v2(n):
    fs = factors_v2(n)
    return sum([f*11 for f in fs])

i = 1
while True:
    if presents_v2(i) >= inp:
        print(i)
        break
    i += 1