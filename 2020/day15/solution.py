from collections import defaultdict

inp = [19, 0, 5, 1, 10, 13]
    
def solve(stop):
    mem = defaultdict(list)
    i = 1
    for x in inp:
        mem[x].append(i)
        last = x
        i += 1
    while True:
        if len(mem[last]) == 1:
            last = 0
            mem[0].append(i)
        else:
            last = mem[last][-1] - mem[last][-2]
            mem[last].append(i)
        if i == stop:
            return last
        i += 1

# Part 1
print(solve(2020))

# Part 2
print(solve(30000000))

    