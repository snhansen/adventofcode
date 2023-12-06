times = [50, 74, 86, 85]
dists = [242, 1017, 1691, 1252]

# Part 1
def get_dist(charge, time):
    speed = charge
    dist = speed*(time-charge)
    return dist

res = 1
for time, dist in zip(times, dists):
    n = sum([1 for charge in range(time) if get_dist(charge, time) > dist])
    res *= n

print(res)

# Part 2
time = int(''.join([str(x) for x in times]))
dist = int(''.join([str(x) for x in dists]))

inter = (0, time)
while True:
    if inter[0] == inter[1] - 1:
        break
    charge = inter[0] + (inter[1]-inter[0])//2
    if get_dist(charge, time) > dist:
        inter = (inter[0], charge)
    else:
        inter = (charge, inter[1])

lower = inter[1]
inter = (lower, time)
while True:
    if inter[0] == inter[1] - 1:
        break
    charge = inter[0] + (inter[1]-inter[0])//2
    if get_dist(charge, time) <= dist:
        inter = (inter[0], charge)
    else:
        inter = (charge, inter[1])

upper = inter[0]
print(upper-lower+1)