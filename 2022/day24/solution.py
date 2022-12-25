from collections import defaultdict, deque
import math

with open("input") as f:
    inp = f.read().strip()

lines = inp.split("\n")
R = len(lines) - 2
C = len(lines[0]) - 2
dirs_dict = {">": 1, "<": -1, "^": -1j, "v": 1j}

blizzards = defaultdict(list)
dirs = []
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c not in [".", "#"]:
            blizzards[0].append((x-1)+(y-1)*1j)
            dirs.append(dirs_dict[c])

for t in range(math.lcm(R, C)-1):
    for p, dir in zip(blizzards[t], dirs):
        blizzards[t+1].append((p.real+dir.real)%C + ((p.imag+dir.imag))%R*1j)
       

def min_steps(start, end, time_start):
    q = deque()
    q.append((time_start, start))
    seen = set()
    while q:
        t, p = q.popleft()
        bliz = blizzards[t%math.lcm(R, C)]
        # Purge if in blizzard.
        if p in bliz:
            continue
        if (t, p) in seen:
            continue
        seen.add((t, p))
        if p == end:
            return t-time_start
            break
        # Wait.
        q.append((t+1, p))
        # Try move in all four directions.
        for dp in [0, -1, 1, 1j, -1j]:
            p_new = p+dp
            if 0 <= p_new.real <= C-1 and 0 <= p_new.imag <= R-1:
                q.append((t+1, p_new))
            elif p_new == end:
                q.append((t+1, p_new))
 

start = 0-1j
end = (C-1) + R*1j 
t1 = min_steps(start, end, 0)
t2 = min_steps(end, start, t1)
t3 = min_steps(start, end, t1+t2)
print(t1)
print(t1+t2+t3)