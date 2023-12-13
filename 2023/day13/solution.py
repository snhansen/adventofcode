from copy import deepcopy

with open("input") as f:
    inp = f.read().strip().split("\n\n")


def print_(pattern):
    for row in pattern:
        print("".join(row))


def split(pattern, r, mode):
    n_cols = len(pattern[0])
    n_rows = len(pattern)
    if mode == 0:
        left = [[pattern[i][j] for i in range(n_rows)] for j in range(r)]
        right = [[pattern[i][j] for i in range(n_rows)] for j in range(r, n_cols)]
        return left, right
    else:
        return pattern[:r], pattern[r:]


def is_reflection(left, right):
    for x, y in zip(reversed(left), right):
        if x != y:
            return False
    return True


def get_reflection(pattern, old = None):
    ranges = {0: len(pattern[0]), 1: len(pattern)}
    for mode in [0, 1]:
        for r in range(1, ranges[mode]):
            left, right = split(pattern, r, mode = mode)
            if is_reflection(left, right):
                reflection = (len(left), mode)
                if old and reflection == old:
                    continue
                return len(left), mode


# Part 1
patterns = [[list(x) for x in pattern.split()] for pattern in inp]
res = [get_reflection(pattern) for pattern in patterns]
print(sum([num*(100 if mode else 1) for num, mode in res]))

# Part 2
def find_smudge(pattern):
    opposite = {"#": ".", ".": "#"}
    reflection = get_reflection(pattern)
    n_cols = len(pattern[0])
    n_rows = len(pattern)
    for row in range(n_rows):
        for col in range(n_cols):
            new_pattern = deepcopy(pattern)
            new_pattern[row][col] = opposite[pattern[row][col]]
            new_reflection = get_reflection(new_pattern, old = reflection)
            if new_reflection:
                return new_reflection
            
            
reflections = [find_smudge(pattern) for pattern in patterns]
print(sum([num*(100 if mode else 1) for num, mode in reflections]))