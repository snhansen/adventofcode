with open("input") as f:
    inp = f.read().strip().split(",")

dirs =  {"n": -1j, "ne": 1-1j, "nw": -1-1j, "s": 1j, "se": 1+1j, "sw": -1+1j}
p = 0
max_steps = 0
for d in inp:
    p += dirs[d]
    max_steps = max(max_steps, int(max(p.real, p.imag)))

# Part 1
print(int(max(p.real, p.imag)))

# Part 2
print(max_steps)