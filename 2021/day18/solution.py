#import ast
import re
import math
from itertools import product


def reverse_string(s):
    return s[len(s)::-1]


def add_to_nearest(s, val, reverse = False):    
    res = re.search('\d+', s)
    if res:
        start, end = res.span()
        if reverse:
            new_val = reverse_string(str(int(reverse_string(res.group())) + val))
        else:
            new_val = str(int(res.group()) + val)
        return s[:start] + new_val + s[end:]
    return s


def explode(s):
    level = 0
    for start, x in enumerate(s):        
        if x == '[':
            level += 1
        elif x == ']':    
            level -= 1
        if level >= 5:
            for j in range(start + 1, len(s)):
                if s[j] == ']':
                    go_next = False
                    break
                if s[j] == '[':
                    go_next = True
                    break
            if go_next:
                continue
            end = start + re.search('\]', s[start:]).span()[1]
            pair = s[start:end]
            p1, p2 = map(int, re.findall('\d+', pair))
            right = add_to_nearest(s[end:], p2)
            left = reverse_string(add_to_nearest(reverse_string(s[:start]), p1, reverse = True))
            return True, left + '0' + right
            
    return False, s


def split(s):
    numbers = re.finditer('\d+', s)
    do_split = False
    for x in numbers:
        n = int(x.group())
        if n >= 10:
            start, end = x.span()
            do_split = True
            break
    if do_split:
        p1 = math.floor(n / 2)
        p2 = math.ceil(n / 2)
        return True, s[:start] + f'[{p1},{p2}]' + s[end:]
    return False, s


def reduce(s):
    while True:
        start = s
        exploded, s = explode(s)
        if not exploded:
            _, s = split(s)      
        if s == start:
            return s


def magnitude(s):
    while True:
        cont = re.search('\[', s)
        if not cont:
            return int(s)
        res1 = re.search('\]', s)
        end = res1.span()[0]
        res2 = re.search('\[', reverse_string(s[:end+1]))
        start = end - res2.span()[0]
        pair = s[start:end+1]
        p1, p2 = map(int, re.findall('\d+', pair))
        s = s[:start] + str(3*p1 + 2*p2) + s[end+1:]
        

# Part 1
with open('input') as f:
    inp = f.read().strip().split('\n')


res = inp.pop(0)
while inp:
    add = inp.pop(0)
    res = f'[{res},{add}]'
    res = reduce(res)

print(magnitude(res))

# Part 2
with open('input') as f:
    inp = f.read().strip().split('\n')


max_mag = 0
for i, j in product(range(len(inp)), range(len(inp))):
    max_mag = max(magnitude(reduce(f'[{inp[i]},{inp[j]}]')), max_mag)

print(max_mag)