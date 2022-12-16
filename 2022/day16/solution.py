import re
import functools

with open("input") as f:
    inp = f.read().strip().split("\n")

dest = {}
flow = {}
for line in inp:
     _, valve, *ls = re.findall("[A-Z]+", line)
     x = re.findall("\d+", line)[0]
     flow[valve] = int(x)
     dest[valve] = {pos: 1 for pos in ls}

dest["start"] = {"AA": 0}
flow["start"] = 0

for cur in dest.keys():
    if cur == "start" or flow[cur] > 0:
        ls = list(dest[cur].items())
        new_dest = {}
        i = 0
        seen = set()
        while ls:
            valve, cost = ls.pop(0)
            if valve == cur:
                continue
            if flow[valve] > 0:
                new_dest[valve] = cost
            else:
                for v, c in dest[valve].items():
                    if v not in seen:
                        ls.append((v, c + cost))
                        seen.add(v)
        dest[cur] = new_dest

for cur in list(dest.keys()):
    if cur != "start" and flow[cur] == 0:
        del dest[cur]

            
# Part 1
@functools.lru_cache(maxsize = None)
def max_pressure(pos, timeleft, on):
    if timeleft == 0:
        return 0
        
    res = 0
    if pos not in on:
        new_on = tuple(sorted(on + (pos,)))
        res = max(res, max_pressure(pos, timeleft-1, new_on)) + flow[pos]*(timeleft - 1)
    
    dests = dest[pos]
    for d, s in dests.items():
        if timeleft-s >= 0:
            res = max(res, max_pressure(d, timeleft-s, on))
    return res


print(max_pressure("start", 30, ()))

# Part 2
@functools.lru_cache(maxsize = None)
def max_pressure2(pos, timeleft, on):    
    if timeleft == 0:
        return max_pressure("start", 26, on)
        
    res = 0
    if pos not in on:
        new_on = tuple(sorted(on + (pos,)))
        res = max(res, max_pressure2(pos, timeleft-1, new_on)) + flow[pos]*(timeleft - 1)
    
    dests = dest[pos]
    for d, s in dests.items():
        if timeleft-s >= 0:
            res = max(res, max_pressure2(d, timeleft-s, on))
    return res


print(max_pressure2("start", 26, ()))