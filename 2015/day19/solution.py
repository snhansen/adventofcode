from collections import defaultdict
import re

with open('input') as f:
    inp = [x.strip() for x in f.readlines()]

repl = defaultdict(list)
repl_rev = defaultdict()
for x in inp:
    if x == '':
        break
    repl[x.split(' => ')[0]].append(x.split(' => ')[1])
    repl_rev[x.split(' => ')[1]] = x.split(' => ')[0]
    
mol = inp[len(inp)-1]

# Part 1
def repl_mols(s):
    ls = []
    for i in range(len(s)):
        if s[i] in repl:
            ls.append([i, 1, s[i]])
        elif i<len(s)-1 and s[i:i+2] in repl:
            ls.append([i, 2, s[i:i+2]])
    return ls

ls = []
for m in repl_mols(mol):
    for r in repl[m[2]]:
        ls.append(mol[:m[0]] + r + mol[m[0]+m[1]:])

print(len(set(ls)))

# Part 2
# A greedy approach (making the largest backwards substitution) yields the answer.
vals = [x[i] for x in repl.values() for i in range(len(x))]
vals = sorted(vals, key = len, reverse = True)

def max_subst(mol):
    for v in vals:
        if v in mol:
            index = mol.index(v)
            return mol[:index] + repl_rev[v] + mol[index+len(v):]
i = 0
while True:
    if mol == 'e':
        print(i)
        break
    mol = max_subst(mol)
    i += 1