with open("input") as f:
    inp = f.read().strip()

nums = list(map(int, inp.split("\n")))


def move_forwards(prevs, nexts, index, val):
    new_nexts = dict(nexts)
    new_prevs = dict(prevs)
    prev = prevs[index]
    next = nexts[index]    
    new_nexts[prev] = next
    new_prevs[next] = prev
    for _ in range(val-1):
        next = nexts[next]
    new_nexts[next] = index
    new_prevs[index] = next
    nextnext = nexts[next]
    new_nexts[index] = nextnext
    new_prevs[nextnext] = index
    return new_prevs, new_nexts


def move_backwards(prevs, nexts, index, val):
    new_nexts = dict(nexts)
    new_prevs = dict(prevs)
    prev = prevs[index]
    next = nexts[index]
    new_nexts[prev] = next
    new_prevs[next] = prev
    for _ in range(val-1):
        prev = prevs[prev]
    new_prevs[prev] = index
    new_nexts[index] = prev
    prevprev = prevs[prev]
    new_prevs[index] = prevprev
    new_nexts[prevprev] = index
    return new_prevs, new_nexts


def solve(nums, part2 = False):
    n = len(nums)
    prevs = {i: (i-1)%n for i in range(n)}
    nexts = {i: (i+1)%n for i in range(n)}
    runs = 10 if part2 else 1
    if part2:
        nums = [num*811589153 for num in nums]
    for _ in range(runs):
        for index, val in enumerate(nums):
            sgn = (val>0) - (val<0)
            val = abs(val)%(n-1)
            if val == 0:
                continue
            if sgn == 1:
                prevs, nexts = move_forwards(prevs, nexts, index, val)
            else:
                prevs, nexts = move_backwards(prevs, nexts, index, val)
    
    index = nums.index(0)
    res = 0
    for c in range(3000):
        index = nexts[index]
        if (c+1)%1000 == 0:
            res += nums[index]
    return res


# Part 1
print(solve(nums))

# Part 2
print(solve(nums, True))