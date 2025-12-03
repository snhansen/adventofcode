with open("input") as f:
    inp = f.read().strip().split("\n")


def find_largest_int(s):
    m = max(int(i) for i in s)
    m = str(m)
    return m, s.index(m)


def joltage(s):
    x1, i1 = find_largest_int(s[:-1])
    x2, _ = find_largest_int(s[(i1+1):])
    return int(x1 + x2)


# Part 1    
print(sum(joltage(s) for s in inp))


# Part 2
def joltage2(s):
    res = ""
    i = -1
    for n in range(12):
        start = i + n + 1
        end = n - 11 if n < 11 else None
        x, di = find_largest_int(s[start:end])
        i += di
        res += x
    return int(res)


print(sum(joltage2(s) for s in inp))