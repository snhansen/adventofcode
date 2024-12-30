def process(s):
    res = ""
    for c in s[::-1]:
        bit = "1" if c == "0" else "0"
        res += bit
    return s + "0" + res


def checksum(s):
    pairs = []
    res = ""
    for i in range(0, len(s), 2):
        pairs.append(s[i:(i + 2)])
        x = "1" if s[i] == s[i + 1] else "0"
        res += x
    if len(res) % 2 == 1:
        return res
    return checksum(res)


def solve(length):
    state = "10111100110001111"
    while len(state) < length:
        state = process(state)
    return checksum(state[:length])


# Part 1
print(solve(272))

# Part 2
print(solve(35651584))