import re
from functools import reduce

with open('input') as f:
    inp = f.read()

numbers = list(map(int, re.findall('\d+', inp)))
start = numbers[0]
buses = numbers[1:]

# Part 1
min_time = min([x*(start // x + 1) for x in buses])
id = [x for x in buses if x*(start // x + 1) == min_time][0]
print(id*(min_time - start))

# Part 2
ls = inp.split('\n')[1].split(',')
lag = [i for i in range(len(ls)) if ls[i] != 'x']
rem = [buses[i]-lag[i] for i in range(len(lag))]

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * pow(p, -1, n_i) * p
    return sum % prod

print(chinese_remainder(buses, rem))