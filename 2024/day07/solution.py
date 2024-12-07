from collections import deque

with open("input") as f:
    inp = f.read().strip()

ls = []

for line in inp.split("\n"):
    target, nums = line.split(": ")
    nums = list(map(int, nums.split(" ")))
    ls.append((int(target), nums))


def evaluate(x, y, oper):
    if oper == "||":
        return int(str(x) + str(y))
    elif oper == "+":
        return x + y
    else:
        return x * y


def get_results(nums, part2 = False):
    operations = ["+", "*"]
    if part2:
        operations += ["||"]
    q = deque([(nums[0], 1)])
    res = set()
    while q:
        part, pos = q.popleft()
        if pos == len(nums):
            res.add(part)
            continue
        for oper in operations:
            q.append((evaluate(part, nums[pos], oper), pos + 1))
    return res


# Part 1
print(sum(target for target, nums in ls if target in get_results(nums)))

# Part 2
print(sum(target for target, nums in ls if target in get_results(nums, part2 = True)))