from functools import cache

with open("input") as f:
    inp = f.read().strip().split("\n")


@cache
def get_arr(s, n):
    s = s.rstrip(".").lstrip(".")
    if not s and not n:
        return 1
    if not s and n:
        return 0
    if s and not n:
        if s.count("#") > 0:
            return 0
        else:
            return 1
    if s[0] == "?":
        return get_arr("." + s[1:], n) + get_arr("#" + s[1:], n)
    elif s[0] == "#":
        new_s = list(s)
        new_n = list(n)
        n = new_n.pop(0)
        if len(s) < n:
            return 0
        if any(x == "." for x in s[:n]):
            return 0
        try: 
            if s[n] == "#":
                return 0
        except IndexError:
            pass
        new_s = "".join(new_s[(n+1):])
        return get_arr(new_s, tuple(new_n))

# Part 1
res = 0
for line in inp:
    springs, n = line.split()
    n = tuple(map(int, n.split(",")))
    res += get_arr(springs, n)

print(res)

# Part 2
res = 0
for line in inp:
    temp, n = line.split()
    springs = ""
    for _ in range(4):
        springs += temp + "?"
    springs += temp
    n = tuple(list(map(int, n.split(",")))*5)
    res += get_arr(springs, n)

print(res)