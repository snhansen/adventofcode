from shapely.geometry.polygon import Polygon

with open("input") as f:
    inp = f.read().strip().split("\n")

# Pick's theorem says: A = i + b/2 - 1, where i is the number of interior points and b is the number of exterior points.
# Thus, i + b = A + b/2 + 1


def solve(part2):
    dirs = {"R": 1, "D": 1j, "L": -1, "U": -1j}
    dirs2 = {0: "R", 1: "D", 2: "L", 3: "U"}
    trench = [0]
    for line in inp:
        if part2:
            temp = line.split(" ")[2]
            dist = int(temp[2:-2], 16)
            dir_ = dirs[dirs2[int(temp[-2])]]
        else:
            dir_ = dirs[line[0]]
            dist = int(line.split(" ")[1])
        trench.append(trench[-1] + dist*dir_)
    
    corners = [(int(p.real), int(p.imag)) for p in trench]
    polygon = Polygon(corners)
    return int(polygon.area + polygon.length/2 + 1)


print(solve(False))
print(solve(True))