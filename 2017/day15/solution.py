# Part 1
multa, multb = 16807, 48271
div = 2147483647

preva, prevb = 591, 393
ans = 0
for _ in range(40000000):
    cura = preva*multa % div
    curb = prevb*multb % div
    if cura % 2**16 == curb % 2**16:
        ans += 1
    preva, prevb = cura, curb
print(ans)    

# Part 2
ans = 0
preva, prevb = 591, 393
for _ in range(5000000):
    while True:
        cura = preva*multa % div
        if cura % 4 == 0:
            preva = cura
            break
        preva = cura
    while True:
        curb = prevb*multb % div
        if curb % 8 == 0:
            prevb = curb
            break
        prevb = curb
    if cura % 2**16 == curb % 2**16:
        ans += 1
print(ans)