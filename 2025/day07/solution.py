from functools import cache

with open("input") as f:
    inp = f.read().strip().split("\n")


splitters = set()
for y, line in enumerate(inp):
    for x, c in enumerate(line):
        if c == "^":
            splitters.add(x + y*1j)
        elif c == "S":
            start = x + y*1j


# Part 1
cur = [start]
beam = set()
splitters_hit = set()
while cur:
    p = cur.pop(0)
    if p in beam:
        continue
    beam.add(p)
    p += 1j
    if p.imag > len(inp):
        continue
    elif p in splitters:
        cur.append(p - 1)
        cur.append(p + 1)
        splitters_hit.add(p)
    else:
        cur.append(p)

print(len(splitters_hit))


# Part 2
@cache
def no_timelines(p):
    if p.imag > len(inp):
        return 1
    p += 1j
    if p in splitters:
        return no_timelines(p + 1) + no_timelines(p - 1)
    else:
        return no_timelines(p)


print(no_timelines(start))