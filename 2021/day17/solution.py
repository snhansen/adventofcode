import re

s = open('input').read().strip()
x_min, x_max, y_min, y_max = map(int, re.findall('-?\d+', s))

def hits(vel):
    pos = (0, 0)
    x_vel, y_vel = vel
    y_high = 0
    while True:
        x, y = pos
        x += x_vel
        y += y_vel
        y_high = max(y_high, y)
        if (x_min <= x <= x_max) and (y_min <= y <= y_max):
            return True, y_high
        if x > x_max or y < y_min:
            return False, 0
        
        y_vel -= 1
        if x_vel >= 1:
            x_vel -= 1
        elif x_vel <= -1:
            x_vel += 1
        pos = (x, y)


# Part 1 + 2
y_high = 0
vels = set()
for x_vel in range(x_max+1):
    for y_vel in range(y_min, -y_min):
        h, yh = hits((x_vel, y_vel))
        if h:
            y_high = max(y_high, yh)
            vels.add((x_vel, y_vel))
        
print(y_high)
print(len(vels))