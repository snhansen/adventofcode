import re
import math

with open('input') as f:
    inp = f.read().splitlines()

def calc(s):
    s = s.replace(' ', '')
    if s.isnumeric():
        return int(s)
    for i in reversed(range(len(s))):
        if s[i] == '+':
            return calc(s[:i]) + int(s[i+1:])
        elif s[i] == '*':
            return calc(s[:i]) * int(s[i+1:])
        
def calc2(s):
    try:
        j = re.search('\)', s).span()[0]
        i = re.search('\((?!.*\()', s[:j]).span()[0]
    except AttributeError:
        return calc(s)
    return calc2(s[0:i] + str(calc(s[i+1:j])) + s[j+1:])
    
# Part 1
print(sum([calc2(s) for s in inp]))

# Part 2
def calc3(s):
    s = s.replace(' ', '')
    while True:
        if s.count('+') == 0:
            return math.prod(map(int, s.split('*')))
            #return s
        i = re.search('\+', s).span()[0]
        try:
            j = re.search('\*(?!.*\*)', s[:i]).span()[0]
        except AttributeError:
            j = -1
        try:
            k = re.search('[\*\+]', s[i+1:]).span()[0] + i + 1
        except AttributeError:
            k = len(s)
        s = f'{s[:j+1]}{int(s[j+1:i]) + int(s[i+1:k])}{s[k:]}'
    
def calc4(s):
    try:
        j = re.search('\)', s).span()[0]
        i = re.search('\((?!.*\()', s[:j]).span()[0]
    except AttributeError:
        return calc3(s)
    return calc4(s[0:i] + str(calc3(s[i+1:j])) + s[j+1:])   

print(sum([calc4(s) for s in inp]))