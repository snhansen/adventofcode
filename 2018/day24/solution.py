import re
from itertools import count

with open("input") as f:
    inp = f.read().strip()

first, second = inp.split("\n\n")


class Group:
    def __init__(self, type_, n, hp, dmg, atype, init, weaks, immunes):
        self.type_ = type_
        self.n = n
        self.hp = hp
        self.dmg = dmg
        self.atype = atype
        self.init = init 
        self.weaks = weaks
        self.immunes = immunes

    def epower(self):
        return self.n * self.dmg


def parse(d, text, type_):
    for i, line in enumerate(text.split("\n")[1:]):
        n, hp, dmg, init = map(int, re.findall("\d+", line))
        temp = re.findall("weak to (.*?)(?=[);]|$)", line)
        weaks = temp[0].split(", ") if temp else []
        temp = re.findall("immune to (.*?)(?=[);]|$)", line)
        immunes = temp[0].split(", ") if temp else []
        atype = re.findall("(\w+)\s+damage", line)[0]
        d[next(c)] = Group(type_, n, hp, dmg, atype, init, weaks, immunes)
    return d


def calc_dmg(grp1, grp2):
    if grp1.atype in grp2.immunes:
        return 0
    elif grp1.atype in grp2.weaks:
        return grp1.epower() * 2
    else:
        return grp1.epower()


def get_targets(groups):
    targets = []
    attackers = sorted([(i, grp.epower(), grp.init) for i, grp in groups.items()], key = lambda x: (-x[1], -x[2]))
    used = set()
    for i, _, _ in attackers:
        attacker = groups[i]
        dmgs = [(j, calc_dmg(attacker, target), target.epower(), target.init) for j, target in groups.items() if j not in used and target.type_ != attacker.type_]
        dmgs = sorted(dmgs, key = lambda x: (-x[1], -x[2], -x[3]))
        if dmgs:
            j, dmg, _, _ = dmgs[0]
            if dmg > 0:
                targets.append((i, j, attacker.init))
                used.add(j)
    return targets


def attack(targets, groups):
    res = 0
    targets = sorted(targets, key = lambda x: -x[2])
    dead = set()
    for i, j, _ in targets:
        if i in dead:
            continue
        attacker = groups[i]
        target = groups[j]
        dmg = calc_dmg(attacker, target)
        d_units = dmg // target.hp 
        res += d_units
        groups[j].n -= d_units
        if groups[j].n <= 0:
            dead.add(j)
            groups.pop(j)
    return res


def get_types(groups):
    res = set()
    for grp in groups.values():
        res.add(grp.type_)
    return res


def get_winner(boost = 0):
    global c 
    c = count()
    groups = parse({}, first, "immune")
    groups = parse(groups, second, "infected")
    for i, grp in groups.items():
        if grp.type_ == "immune":
            grp.dmg += boost
    while True:
        targets = get_targets(groups)
        res = attack(targets, groups)
        if res == 0:
            break
    return get_types(groups), sum(grp.n for grp in groups.values())

# Part 1
_, units = get_winner()
print(units)

# Part 2
low, high = 0, 10000
while (low < high):
    mid = low + (high - low) // 2
    remaining, units = get_winner(boost = mid)
    if len(remaining) > 1:
        low = mid + 1
    else:
        winner = remaining.pop()
        if winner == "immune":
            high = mid
        else:
            low = mid + 1

_, units = get_winner(boost = low)
print(units)