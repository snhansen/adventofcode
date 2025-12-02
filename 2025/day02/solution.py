with open("input") as f:
    inp = f.read().strip().split(",")


def split_string(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]

    
def is_invalid(s, part1 = True):
    if len(s) == 1:
        return False
    if part1:
        if len(s) % 2 == 1:
            return False
        if len(set(split_string(s, len(s)//2))) == 1:
            return True
    else:
        for i in range(1, len(s)):
            if len(set(split_string(s, i))) == 1:
                return True
    return False


ans_pt1, ans_pt2 = 0, 0
for s in inp:
    l, r = s.split("-")
    for x in range(int(l), int(r) + 1):
        if is_invalid(str(x), part1 = True):
            ans_pt1 += x
        if is_invalid(str(x), part1 = False):
            ans_pt2 += x

print(ans_pt1, ans_pt2)