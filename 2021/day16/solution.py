from math import prod

s_hexa = open('input').read().strip()

s = ''
for x in s_hexa:
    s += '{:0b}'.format(int(x, 16)).zfill(4)

version_sum = 0

def decode(s):
    global version_sum
    version = int(s[0: 3], 2)
    version_sum += version
    type = int(s[3: 6], 2)
    if type == 4:
        s = s[6: ]
        res = ''
        while True:
            res += s[1: 5]
            if s[0] == '0':
                return int(res, 2), s[5: ]
            s = s[5: ]
    
    id = s[6]
    ls = []
    if id == '0':
        l = int(s[7: 22], 2)
        sub_s = s[22: 22+l]
        while sub_s:
            val, sub_s = decode(sub_s)
            ls.append(val)
        s = s[22+l: ]
    else:
        n = int(s[7: 18], 2)
        s = s[18: ]
        for i in range(n):
            val, s = decode(s)
            ls.append(val)
    
    if type == 0:
        return sum(ls), s
    elif type == 1:
        return prod(ls), s
    elif type == 2:
        return min(ls), s
    elif type == 3:
        return max(ls), s
    elif type == 5:
        return int(ls[0] > ls[1]), s
    elif type == 6:
        return int(ls[0] < ls[1]), s
    elif type == 7:
        return int(ls[0] == ls[1]), s


# Part 1
val, _ = decode(s)
print(version_sum)

# Part 2
print(val)