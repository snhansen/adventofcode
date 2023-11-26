inp = 'hxbxwxba'

def increment(s):
    s_inc = ''
    c = 0
    for i in range(len(s)):
        if s[len(s)-i-1] == 'z':
            c += 1
        else:
            break
    s_inc = s[0:(len(s)-c-1)]
    for i in range(c+1):
        s_inc += chr(((ord(s[len(s)-c-1+i])-96) % 26) +97)
    return s_inc
    
def req1(s):
    for i in range(len(s)-2):
        if ord(s[i]) == ord(s[i+1]) - 1 and ord(s[i+1]) == ord(s[i+2]) - 1:
            return True
    return False

def req3(s):
    c = 0
    i = 0
    l = []
    while i<len(s)-1:
        if s[i] == s[i+1]:
            if s[i] not in l:
                c += 1
                l.append(s[i])
            i += 2
            if c == 2:
                return True
        else:
            i += 1
    return False

while True:
    inp = increment(inp)
    if 'i' in inp or 'o' in inp or 'l' in inp:    
        continue
    if req1(inp) and req3(inp):
        print(inp)
        break

while True:
    inp = increment(inp)
    if 'i' in inp or 'o' in inp or 'l' in inp:    
        continue
    if req1(inp) and req3(inp):
        print(inp)
        break