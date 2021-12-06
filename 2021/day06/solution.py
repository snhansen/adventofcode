with open('input') as f:
    ls = list(map(int, f.read().split(',')))

mem = {}
def no_fish(state, days):
    if state >= days:
        return 1
    else:
        if not (state, days) in mem:
            mem[(state, days)] = 1 + sum([no_fish(8, days - (state + 1 + 7*i)) for i in range(0, (days-state+6)//7)])
        return mem[(state, days)]

# Part 1
print(sum([no_fish(x, 80) for x in ls]))        

# Part 2
print(sum([no_fish(x, 256) for x in ls]))

# A somewhat simpler solution.
counts = [ls.count(i) for i in range(9)]

for i in range(256):
    zeros = counts.pop(0)
    counts[6] += zeros
    counts.append(zeros)
    if i + 1 in [80, 256]:
        print(sum(counts))

# A different solution based on a circular array. Here the counts are so that after x days, the number of fish with 0 days left is stored at counts[x%9], the number of fisk with 1 day left is stored at counts[x%9 + 1] etc.
counts = [ls.count(i) for i in range(9)]

for i in range(256):
    counts[(i + 7) % 9] += counts[i % 9]
    if i + 1 in [80, 256]:
        print(sum(counts))