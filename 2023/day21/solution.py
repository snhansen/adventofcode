with open("input") as f:
    inp = f.read().strip().split("\n")

R, C = len(inp), len(inp[0])

grid = {i+j*1j: inp[j][i] for i in range(C) for j in range(R)}

for p, c in grid.items():
    if c == "S":
        start = p
        grid[p] = "."

ps = set()
ps.add(start)

# Let f(n) be the number of gardens after n steps. Let R = C be the height/width of the grid.
# The number of steps is 26501365 = 202300*R + 65. We anticipate that g(m) = f(65+m*R) is quadratic,
# so we find g(m), for m = 0, 1, 2, and fit a quadratic polynomial to (m, g(m)) [m = 0, 1, 2].
# This happens to fit perfectly.

steps = 26501365
rest = steps % R

for m in range(rest+2*R):
    new_ps = set()
    for p in ps:
        for dp in [-1, 1, 1j, -1j]:
            new_p = p + dp
            cor_p = (new_p.real % C) + (new_p.imag % R)*1j
            if grid[cor_p] == ".":
                new_ps.add(new_p)
    ps = new_ps
    if m == 63:
        print(len(ps)) # Part 1
    if (m+1) % R == rest:
        print((m+1)//R, m+1, len(ps)) # Points to fit 


# This is the corresponding polynomial.
def n_gardens(steps):
    return 3738+14836*steps+14696*steps**2


print(n_gardens(steps // R))