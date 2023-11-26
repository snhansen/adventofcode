import re

with open('input') as f:
    inp = [x.strip() for x in f.readlines()]

pps = []
pp = {}
for l in inp:
    if l == '':
        pps.append(pp)
        pp = {}
    else:
        fields = l.split(' ')
        for f in fields:
            pp[f.split(':')[0]] = f.split(':')[1]

pps.append(pp)

# Part 1
print(len([pp for pp in pps if 'byr' in pp and 'iyr' in pp and 'eyr' in pp and 'hgt' in pp and 'hcl' in pp and 'ecl' in pp and 'pid' in pp]))

# Part 2
def is_valid(pp):
    if not ('byr' in pp and 'iyr' in pp and 'eyr' in pp and 'hgt' in pp and 'hcl' in pp and 'ecl' in pp and 'pid' in pp):
        return False
    if not (1920 <= int(pp['byr']) <= 2002):
        return False
    if not (2010 <= int(pp['iyr']) <= 2020):
        return False
    if not (2020 <= int(pp['eyr']) <= 2030):
        return False
    hgt = int(re.search('\d+',pp['hgt'])[0])
    if not (('cm' in pp['hgt'] and 150 <= hgt <= 193) or ('in' in pp['hgt'] and 59 <= hgt <= 76)):
        return False
    if not (pp['hcl'][0] == '#' and len(pp['hcl']) == 7 and len(re.findall('[a-f,0-9]', pp['hcl'])) == 6):
        return False
    if not (pp['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
        return False
    if not (len(pp['pid']) == 9 and len(re.findall('[0-9]', pp['pid'])) == 9):
        return False
    return True
        
print(sum([is_valid(pp) for pp in pps]))      