with open("input") as f:
    inp = f.read().strip()

ranges, ids = inp.split("\n\n")
ranges = [(int(x), int(y)) for x, y in (r.split("-") for r in ranges.split("\n"))]
ids = list(map(int, ids.split("\n")))


# Part 1
def is_fresh(id_):
    for x, y in ranges:
        if x <= id_ <= y:
            return True
    return False


print(sum(is_fresh(id_) for id_ in ids))


# Part 2
ranges.sort()

merged = []
cur_x, cur_y = ranges[0]

for x, y in ranges[1:]:
    if x <= cur_y + 1:
        cur_y = max(cur_y, y)
    else:
        merged.append((cur_x, cur_y))
        cur_x, cur_y = x, y

merged.append((cur_x, cur_y))
print(sum(y - x + 1 for x, y in merged))