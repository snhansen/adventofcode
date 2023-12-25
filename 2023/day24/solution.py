from sympy import symbols, Eq, solve
from itertools import combinations

with open("input") as f:
    inp = f.read().strip().split("\n")


init_pos = []
vel = []
hails = []
for line in inp:
    p, v = line.split(" @ ")
    hails.append((list(map(int, p.split(", "))), list(map(int, v.split(", ")))))


def cross_path(hail1, hail2):
    (x1, y1, _), (vx1, vy1, _) = hail1
    (x2, y2, _), (vx2, vy2, _) = hail2
    if vx1/vx2 == vy1/vy2:
        return None
    else:
        t2 = (y2 - y1 - (x2-x1)*(vy1/vx1)) / (vx2*vy1/vx1 - vy2)
        t1 = (x2+vx2*t2-x1)/vx1
        return t1, t2, x1+vx1*t1, y1+vy1*t1


# Part 1
coord_min = 200000000000000
coord_max = 400000000000000

ans = 0
for hail1, hail2 in combinations(hails, 2):
    path = cross_path(hail1, hail2)
    if path is not None:
        t1, t2, x, y = path
        if t1 > 0 and t2 > 0 and x >= coord_min and x <= coord_max and y >= coord_min and y <= coord_max:
            ans += 1

print(ans)

# Part 2
x, y, z, vx, vy, vz, t1, t2, t3 = symbols("x y z vx vy vz t1 t2 t3")

h1, h2, h3 = hails[:3]
(h1x, h1y, h1z), (h1vx, h1vy, h1vz) = h1
(h2x, h2y, h2z), (h2vx, h2vy, h2vz) = h2
(h3x, h3y, h3z), (h3vx, h3vy, h3vz) = h3

eq1 = Eq(x+vx*t1, h1x+h1vx*t1)
eq2 = Eq(y+vy*t1, h1y+h1vy*t1)
eq3 = Eq(z+vz*t1, h1z+h1vz*t1)
eq4 = Eq(x+vx*t2, h2x+h2vx*t2)
eq5 = Eq(y+vy*t2, h2y+h2vy*t2)
eq6 = Eq(z+vz*t2, h2z+h2vz*t2)
eq7 = Eq(x+vx*t3, h3x+h3vx*t3)
eq8 = Eq(y+vy*t3, h3y+h3vy*t3)
eq9 = Eq(z+vz*t3, h3z+h3vz*t3)

solution = solve((eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9), (x, y, z, vx, vy, vz, t1, t2, t3))
print(solution[0][0] + solution[0][1] + solution[0][2])