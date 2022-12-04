with open("input") as f:
    inp = f.read().split()


# Part 1 and 2

p1, p2 = 0, 0
for line in inp:
    r1, r2 = line.split(",")
    l1, u1 = list(map(int, r1.split('-')))
    l2, u2 = list(map(int, r2.split('-')))
    if (l1 >= l2 and u1 <= u2) | (l2 >= l1 and u2 <= u1):
        p1 += 1
    if l2 <= u1 and u2 >= l1:
        p2 += 1

print(p1, p2)