with open("input") as f:
    inp = f.read().strip()


def get_start(s, d):
    for i in range(d-1,len(s)):
        if len(set(s[i-d+1:i+1])) == d:
            return i + 1

# Part 1
print(get_start(inp, 4))

# Part 2
print(get_start(inp, 14))       