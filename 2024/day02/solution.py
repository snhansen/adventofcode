with open("input") as f:
    inp = f.read().strip().split("\n")

inp = [list(map(int, line.split(" "))) for line in inp]


def is_safe(ls):
    dif = [(y - x) for x, y in zip(ls[1:], ls[:-1])]
    if all(x > 0 for x in dif) or all(x < 0 for x in dif):
        if all((abs(x) > 0) and (abs(x) < 4) for x in dif):
            return True
    return False


# Part 1
print(sum(is_safe(x) for x in inp))

# Part 2
ans = 0
for line in inp:
    for i in range(len(line)):
        temp = line[:i] + line[(i+1):]
        if is_safe(temp):
            ans += 1
            break

print(ans)
