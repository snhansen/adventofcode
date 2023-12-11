from itertools import combinations

with open("input") as f:
    inp = f.read().strip().split("\n")


def solve(n):
    dxs = []
    dx = 0
    for x in range(len(inp[0])):
        if all(inp[y][x] == "." for y in range(len(inp))):
            dx += n
        dxs.append(dx)

    dys = []
    dy = 0
    for y in range(len(inp)):
        if all(inp[y][x] == "." for x in range(len(inp[0]))):
            dy += n
        dys.append(dy)

    galaxies = set()
    for x in range(len(inp[0])):
        for y in range(len(inp)):
            if inp[y][x] == "#":
                galaxies.add((x+dxs[x], y+dys[y]))
        
    return(sum(abs(p[0]-q[0]) + abs(p[1]-q[1]) for p, q in combinations(galaxies, r = 2)))


# Part 1
print(solve(1))    

# Part 2
print(solve(999999))