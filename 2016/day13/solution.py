from collections import deque


def is_open(x, y):
    res = x*x + 3*x + 2*x*y + y + y*y + 1364
    return bin(res)[2:].count("1") % 2 == 0


# Part 1
sx, sy = 1, 1
ex, ey = 31, 39
seen = set()
q = deque([(0, sx, sy)])
while q:
    steps, x, y = q.popleft()
    if (x, y) == (ex, ey):
        print(steps)
        break
    if (x, y) in seen:
        continue
    seen.add((x, y))
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if nx >= 0 and ny >= 0 and is_open(nx, ny):
            q.append((steps + 1, nx, ny))


# Part 2
sx, sy = 1, 1
seen = set()
q = deque([(0, sx, sy)])
while q:
    steps, x, y = q.popleft()
    if steps > 50:
        continue
    if (x, y) in seen:
        continue
    seen.add((x, y))
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if nx >= 0 and ny >= 0 and is_open(nx, ny):
            q.append((steps + 1, nx, ny))

print(len(seen))