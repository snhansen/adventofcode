import re
from collections import deque

with open('input') as f:
    inp = f.read()

# Part 1
print(sum(map(int, re.findall('-?[0-9]+', inp))))

# Part 2
def remove_red(s):
    for i in range(len(s)-2):
        if s[i:i+3] == 'red':
            c1 = -1
            c2 = -1
            cont = False
            for j in range(i):
                if s[i-1-j] == ']':
                    c1 -= 1
                elif s[i-1-j] == '[':
                    c1 += 1
                    if c1 == 0:
                        cont = True
                        break
                elif s[i-1-j] == '}':
                    c2 -= 1
                elif s[i-1-j] == '{':
                    c2 += 1
                    if c2 == 0:
                        start = i-1-j
                        break
            if not cont:
                c = -1
                for j in range(i+1, len(s)):
                    if s[j] == '{':
                        c -= 1
                    if s[j] == '}':
                        c += 1
                        if c == 0:
                            end = j
                            break
                return s[0:start] + s[end+1:len(s)]
    return s

while True:
    temp = remove_red(inp)
    if len(temp) == len(inp):
        break
    inp = temp

print(sum(map(int, re.findall('-?[0-9]+', inp))))