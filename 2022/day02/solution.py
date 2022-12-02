with open("input") as f:
    inp = [x.strip() for x in f.readlines()]


rounds = [s.split(" ") for s in inp]
scores = {"A": 1, "B": 2, "C": 3}
convert = {"X": "A", "Y": "B", "Z": "C"}
shapes = ["A", "B", "C"]


def get_scores(ls, part2 = False):
    s1, s2 = ls
    if not part2:
        s2 = convert[s2]
    if s1 == s2:
        return scores[s2] + 3
    if s2 == "A" and s1 == "C":
        return scores[s2] + 6
    if s2 == "B" and s1 == "A":
        return scores[s2] + 6
    if s2 == "C" and s1 == "B":
        return scores[s2] + 6
    else:
        return scores[s2]


# Part 1
print(sum([get_scores(rnd) for rnd in rounds]))


# Part 2
def get_hand(ls):
    win = {"X": -1, "Y": 0, "Z": 1}
    s1, s2 = ls
    s2 = shapes[(shapes.index(s1)+win[s2])%3]
    return [s1, s2]

print(sum([get_scores(get_hand(rnd), part2 = True) for rnd in rounds]))