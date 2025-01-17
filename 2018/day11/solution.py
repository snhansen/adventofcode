from itertools import product
from functools import cache


def power(x, y, serial):
    temp = ((x + 10)*y + serial)*(x + 10)
    return int(str(temp // 100)[-1]) - 5


serial = 2187
grid = {}
for x in range(1, 301):
    for y in range(1, 301):
        grid[(x, y)] = power(x, y, serial)


max_power = 0
for x in range(1, 299):
    for y in range(1, 299):
        power = sum(grid[(x + dx, y + dy)] for dx, dy in product([0, 1, 2], repeat = 2))
        if power > max_power:
            max_power = power
            location = (x,y)


print(",".join((str(n) for n in location)))

# Part 2
@cache
def largest_divisor(n):
    res = n
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            res = i
    return res


@cache
def square(x, y, d):
    div = largest_divisor(d)
    if div == d:
        return sum(grid[x + dx, y + dy] for dx, dy in product(list(range(d)), repeat = 2))
    else:
        k = d // div
        return sum(square(x + i*div, y + j*div, div) for i in range(k) for j in range(k))


max_power = 0
for x in range(1, 301):
    for y in range(1, 301):
        max_d = min(300 - x, 300 - y)
        max_d = min(max_d, 20) # we anticipate that a square of at most 20 pixel is sufficient
        for d in range(max_d + 1):
            power = square(x, y, d)
            if power > max_power:
                location = (x, y, d)
                max_power = power

print(",".join((str(n) for n in location)))