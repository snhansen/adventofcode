from functools import cache

with open("input") as f:
    inp = f.read().strip().split("\n")


@cache
def get_arr(s, n):
    s = s.rstrip(".").lstrip(".")
    if not s:
        return not n
    if not n:
        return "#" not in s
    if s[0] == "?":
        return get_arr("." + s[1:], n) + get_arr("#" + s[1:], n)
    elif s[0] == "#":
        n = list(n)
        n0 = n.pop(0)
        if len(s) < n0:
            return 0
        if any(x == "." for x in s[:n0]):
            return 0
        try: 
            if s[n0] == "#":
                return 0
        except IndexError:
            pass
        s = "".join(s[(n0+1):])
        return get_arr(s, tuple(n))


# Part 1 + 2
res = 0
part1, part2 = 0, 0
for line in inp:
    springs, n = line.split()
    n = list(map(int, n.split(",")))
    part1 += get_arr(springs, tuple(n))
    springs = "?".join([springs]*5)
    n = n*5
    part2 += get_arr(springs, tuple(n))

print(part1)
print(part2)