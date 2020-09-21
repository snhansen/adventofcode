from collections import defaultdict, deque

with open('input') as f:
    inp = [x.strip() for x in f.readlines()]

repl = defaultdict(list)
for x in inp:
    if x == '':
        break
    repl[x.split(' => ')[0]].append(x.split(' => ')[1])
    
mole = inp[len(inp)-1]

# Part 1
def repl_moles(s):
    ls = []
    for i in range(len(s)):
        if s[i] in repl:
            ls.append([i, 1, s[i]])
        elif i<len(s)-1 and s[i:i+2] in repl:
            ls.append([i, 2, s[i:i+2]])
    return ls

ls = []
for m in repl_moles(mole):
    for r in repl[m[2]]:
        ls.append(mole[:m[0]] + r + mole[m[0]+m[1]:])

print(len(set(ls)))

# Part 2
ls = deque(['e'])
i = 0
while ls:
    l = ls.popleft()
    print(l)
    i += 1
    for m in repl_moles(l):
        for r in repl[m[2]]:
            new_mole = l[:m[0]] + r + l[m[0]+m[1]:]
            if new_mole == mole:
                print(i)
                break
            ls.append(new_mole)
            
print(ls)




     
           

#i = 0
#for l in ls:
    #for m in repl[l]:
        
    

