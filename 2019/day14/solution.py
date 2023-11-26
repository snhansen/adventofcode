import re
import math


with open('input') as f:
    inp = [x.strip() for x in f.readlines()]

reactions = {}
for line in inp:
    reactions[re.compile('[A-Za-z]+').findall(line)[-1]] = [re.compile('[A-Za-z]+').findall(line)[:-1], list(map(int, re.compile('[0-9]+').findall(line)[:-1])), int(re.compile('[0-9]+').findall(line)[-1])]


def reaction(o_chem, o_qt, d_chems):
    if o_chem in d_chems.keys() and d_chems[o_chem] > 0:
        min_qt = reactions[o_chem][2]
        times = math.ceil(o_qt / min_qt)
        d_chems[o_chem] -= times*min_qt
        for i_chem, i_qt in zip(reactions[o_chem][0], reactions[o_chem][1]):
            if i_chem in d_chems:
                d_chems[i_chem] += i_qt*times
            else:
                d_chems[i_chem] = i_qt*times
    else:
        print(f'You don\'t have any {o_chem}')
    return d_chems


def get_ore(fuel_qt):
    d_chems = {}
    d_chems['FUEL'] = fuel_qt
    chems_non_ore = [chem for chem in d_chems if d_chems[chem] > 0 and chem != 'ORE']
    while chems_non_ore:
        d_chems = reaction(chems_non_ore[0], d_chems[chems_non_ore[0]], d_chems)
        chems_non_ore = [chem for chem in d_chems if d_chems[chem] > 0 and chem != 'ORE']
    return d_chems['ORE']

# Part 1
print(get_ore(1))


# Part 2    
lower = 0
upper = 1000000000000
while lower < upper - 1:
    mid = (lower + upper) // 2
    if get_ore(mid)>1000000000000:
        upper = mid
    else:
        lower = mid

print(lower)
