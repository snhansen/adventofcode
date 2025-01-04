from itertools import permutations

with open("input") as f:
    inp = f.read().strip().split("\n")


def swapposition(s, index1, index2):
    s[index1], s[index2] = s[index2], s[index1]
    return s


def swapletter(s, letter1, letter2):
    return swapposition(s, s.index(letter1), s.index(letter2))


def rotateleft(s, steps):
    assert steps <= len(s)
    s = s[steps:] + s[:steps]
    return s


def rotateright(s, steps):
    s = rotateleft(s[::-1], steps)
    return s[::-1]


def rotatebased(s, letter):
    steps = s.index(letter) + 1
    if steps >= 5:
        steps += 1
    steps %= len(s)
    return rotateright(s, steps)


def reversepositions(s, index1, index2):
    sub_s = s[index1:(index2 + 1)]
    return s[:index1] + sub_s[::-1] + s[(index2 + 1):]


def moveposition(s, index1, index2):
    s.insert(index2, s.pop(index1))
    return s


def scramble(s):
    s = list(s)
    for line in inp:
        parts = line.split(" ")
        operation = parts[0] + parts[1]
        match operation:
            case "swapposition":
                s = swapposition(s, int(parts[2]), int(parts[5]))
            case "swapletter":
                s = swapletter(s, parts[2], parts[5])
            case "rotateleft":
                s = rotateleft(s, int(parts[2]))
            case "rotateright":
                s = rotateright(s, int(parts[2]))
            case "rotatebased":
                s = rotatebased(s, parts[6])
            case "reversepositions":
                s = reversepositions(s, int(parts[2]), int(parts[4]))
            case "moveposition":
                s = moveposition(s, int(parts[2]), int(parts[5]))
    return "".join(s)

# Part 1
pw = "abcdefgh"
print(scramble(pw))

# Part 2
for s in permutations(pw, len(pw)):
    s = "".join(s)
    if scramble(s) == "fbgdceah":
        print(s)
        break