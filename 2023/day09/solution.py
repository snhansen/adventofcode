import re

with open("input") as f:
    inp = f.read().strip().split("\n")

seqs = [list(map(int, re.findall("-?\d+", line))) for line in inp]


def get_diffs(diff):
    ls = []
    while any(x != 0 for x in diff):
        diff = [x-y for x, y in zip(diff[1:], diff[:-1])]
        ls.append(diff)
    return ls


def get_prediction(seq):
    inc = sum([d[-1] for d in get_diffs(seq)])
    return seq[-1] + inc


# Part 1
print(sum([get_prediction(seq) for seq in seqs]))

# Part 2
def get_prediction2(seq):
    inc = sum([d[0]*(-1)**k for k, d in enumerate(get_diffs(seq))])
    return seq[0] - inc

print(sum([get_prediction2(seq) for seq in seqs]))