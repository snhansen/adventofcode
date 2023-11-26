with open('input') as f:
    inp = [x.strip() for x in f.readlines()]

ls_out = [[y.split(']')[-1] for y in x.split('[')] for x in inp]
ls_in = [[y.split(']')[0] for y in x.split('[') if len(y.split(']'))>1] for x in inp]

def has_abba(s):
    for i in range(len(s)-3):
        if s[i] == s[i+3] and s[i+1] == s[i+2] and s[i] != s[i+1]:
            return True
    return False

# Part 1
count = 0
for i in range(len(ls_out)):
    if sum(map(has_abba,ls_out[i])) and not sum(map(has_abba,ls_in[i])):
        count += 1
    
print(count)

# Part 2
def get_abas(ls):
    abas = []
    for s in ls:    
        for i in range(len(s)-2):
            if s[i] == s[i+2] and s[i] != s[i+1]:
                abas.append(s[i:i+3])
    return abas

def rev_abas(ls):
    new_ls = []
    for s in ls:
        new_ls.append(s[1]+s[0]+s[1])
    return new_ls

count = 0
for i in range(len(ls_out)):
    abas_out = get_abas(ls_out[i])
    abas_in = get_abas(ls_in[i])
    if len(set(rev_abas(abas_out)).intersection(set(abas_in))):
        count += 1

print(count)