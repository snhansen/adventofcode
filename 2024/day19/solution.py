from functools import cache

with open("input") as f:
    inp1, inp2 = f.read().strip().split("\n\n")

patterns = inp1.split(", ")
designs = inp2.split("\n")


@cache
def no_ways(design):
    if design == "":
        return 1
    to_check = []
    for pattern in patterns:
        if design[:len(pattern)] == pattern:
            to_check.append(pattern)
    if not to_check:
        return 0
    else:
        return sum(no_ways(design[len(pattern):]) for pattern in to_check)

# Part 1
print(sum(no_ways(design) > 1 for design in designs))

# Part 2
print(sum(no_ways(design) for design in designs))