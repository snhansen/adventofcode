with open("input") as f:
    inp = f.read().strip()


def next_row(s):
    res = ""
    for i in range(len(s)):
        if i == 0:
            tiles = (".", s[0], s[1])
        elif i == len(s) - 1:
            tiles = (s[len(s) - 2], s[len(s) - 1], ".")
        else:
            tiles = (s[i-1], s[i], s[i+1])
        left, center, right = tiles
        if left == "^" and center == "^" and right == ".":
            res += "^"
        elif left == "." and center == "^" and right == "^":
            res += "^"
        elif left == "^" and center == "." and right == ".":
            res += "^"
        elif left == "." and center == "." and right == "^":
            res += "^"
        else:
            res += "."
    return res


rows = [inp]
for i in range(400000 - 1):
    rows.append(next_row(rows[-1]))

# Part 1
print(sum(row.count(".") for row in rows[:40]))

# Part 2
print(sum(row.count(".") for row in rows))