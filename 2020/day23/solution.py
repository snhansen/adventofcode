input = '712643589'
cups = [int(x) for x in input]

def solve(part2 = False):
    next = {}
    iter = 100
    for i in range(1, 10):
        next[i] = cups[(cups.index(i)+1)%len(cups)]
    if part2:
        end = 1000000
        iter = 10000000
        next[cups[len(cups)-1]] = 10
        for i in range(10, end):
            next[i] = i+1
        next[end] = cups[0]
    
    cur = next[len(next)]
    for _ in range(iter):
        pu = [next[cur], next[next[cur]], next[next[next[cur]]]]
        dest = cur - 1 if cur > 1 else len(next)       
        while dest in pu:
            dest -= 1
            if dest == 0:
                dest = len(next)
        next[cur] = next[pu[-1]]
        next[pu[-1]] = next[dest]
        next[dest] = pu[0]
        cur = next[cur]

    if not part2:
        res = ''
        val = 1
        for _ in range(8):
            res += str(next[val])
            val = next[val]
        return res
    else:
        return next[1]*next[next[1]]

# Part 1
print(solve())

# Part 2
print(solve(True))