from math import lcm
from functools import reduce

with open("input") as f:
    inp = f.read().strip().split("\n")


type_ = {}
dests = {} 
memory = {}
for line in inp:
    from_, dest = line.split(" -> ")
    typ = from_[0]
    name = from_[1:]
    if typ == "b":
        name = from_
        typ = ""
    type_[name] = typ
    dests[name] = dest.split(", ")
    if typ == "&":
        memory[name] = {}
    elif typ == "%":
        memory[name] = 0

for from_, dests_ in dests.items():
    for dest in dests_:
        if dest in type_ and type_[dest] == "&":
            memory[dest][from_] = 0


cycle, n_low, n_high = 0, 0, 0
def press_button():
    global cycle
    global n_low
    global n_high
    q = [("button", "broadcaster", 0)]
    while q:
        from_, to, pulse = q.pop(0)
        n_low += 1-pulse
        n_high += pulse
        if to not in dests:
            continue
        type_to = type_[to]
        dests_to = dests[to]
        if type_to == "":
            for dest in dests_to:
                q.append((to, dest, 0))
        elif type_to == "%":
            if pulse == 0:
                memory[to] = (memory[to]+1)%2
                for dest in dests_to:
                    q.append((to, dest, memory[to]))
        elif type_to == "&":
            memory[to][from_] = pulse
            if to == "jm" and pulse == 1:
                cycles.append(cycle+1)
            if all(x == 1 for x in memory[to].values()):
                for dest in dests_to:
                    q.append((to, dest, 0))
            else:
                for dest in dests_to:
                    q.append((to, dest, 1))
    cycle += 1


# The module "rx" gets a low pulse if and only module "jm" has last been sent high pulses from modules "dh", "lm", "dg" and "db".
# We figure out when each of these send high pulses to "jm" and anticipate a cyclic nature.
cycles = []
while (len(cycles) < 4):
    if cycle == 1000:
        print(n_low*n_high)
    press_button()

print(reduce(lcm, cycles))