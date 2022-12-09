with open("input") as f:
    inp = f.read().strip().split("\n")

sign = lambda a: (a > 0) - (a < 0)

def get_next_pos(h, t):
    if abs(h.real - t.real) <= 1 and abs(h.imag - t.imag) <= 1:
        return t
    else:
        inc = sign(h.real - t.real) + sign(h.imag - t.imag)*1j
        return t + inc


dirs = {"R": 1, "L": -1, "U": -1j, "D": 1j}
visited = [[0 for _ in range(10)]]
for line in inp:
    dir, steps = line.split(" ")
    steps = int(steps)
    for _ in range(steps):
        pos = list(visited[-1])
        pos[0] += dirs[dir]
        for i in range(1,10):
            pos[i] = get_next_pos(pos[i-1], pos[i])
        visited.append(pos)

# Part 1
print(len(set(x[1] for x in visited)))

# Part 2
print(len(set(x[9] for x in visited)))