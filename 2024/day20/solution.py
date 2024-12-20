from itertools import combinations

with open("input") as f:
    inp = f.read().strip().split("\n")


track = set()
for i, l in enumerate(inp):
    for j, x in enumerate(l):
        if x != "#":
            track.add(j + i*1j)
        if x == "S":
            start = j + i*1j
        if x == "E":
            end = j + i*1j

dirs = [1, -1, 1j, -1j]
times = {start: 0}
q = [start]
while q:
    p = q.pop()
    for dp in dirs:
        if p + dp not in track or p + dp in times.keys():
            continue
        times[p + dp] = times[p] + 1
        q.append(p + dp)

pt1, pt2 = 0, 0
for p1, p2 in combinations(times.keys(), 2):
    dist = abs(p1.real - p2.real) + abs(p1.imag - p2.imag)
    if dist <= 2:
        pt1 += (times[end] - (times[p1] + times[end] - times[p2] + dist) >= 100)
    if dist <= 20:
        pt2 += (times[end] - (times[p1] + times[end] - times[p2] + dist) >= 100)

print(pt1, pt2)