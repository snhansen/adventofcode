with open("input") as f:
    s = f.read().strip()


def react(s):
    for i in range(len(s) - 1):
        if s[i].lower() == s[i+1].lower() and s[i] != s[i+1]:
            return False, s[:i] + s[i+2:]
    return True, s


def reduce(s):
    while True:
        done, s = react(s)
        if done:
            return s


# Part 1
s = reduce(s)
print(len(s))

# Part 2
letters = (chr(97 + i) for i in range(26))
print(
    min(
        map(
            len,
            (
                reduce(
                    s.replace(letter, "").replace(letter.upper(), ""))
                    for letter in letters
            )
        )
    )
)
