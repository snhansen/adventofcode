from functools import cache

with open("input") as f:
    inp1, inp2 = f.read().strip().split("\n\n")

patterns = inp1.split(", ")
designs = inp2.split("\n")


@cache
def no_ways(design):
    if design == "":
        return 1
    return sum(no_ways(design[len(pattern):]) for pattern in patterns if design[:len(pattern)] == pattern)

# Part 1
print(sum(no_ways(design) > 0 for design in designs))

# Part 2
print(sum(no_ways(design) for design in designs))