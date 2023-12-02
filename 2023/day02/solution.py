with open("input") as f:
    inp = f.read().strip().split("\n")

games = []
for game, line in enumerate(inp):
    _, grabs = line.split(": ")
    grabs = grabs.replace(";", ",")
    grabs = grabs.split(", ")
    grabs = [(int(grab.split()[0]), grab.split()[1]) for grab in grabs]
    games.append((game+1, grabs))

# Part 1
def valid_game(ls):
    cubes = {"red": 12, "green": 13, "blue": 14}
    return all(val <= cubes[color] for val, color in ls)

print(sum([game for game, grabs in games if valid_game(grabs)]))

# Part 2
def power(grabs):
    cubes = {"red": 0, "green": 0, "blue": 0}
    for val, color in grabs:
        cubes[color] = max(cubes[color], val)
    vals = list(cubes.values())
    return vals[0]*vals[1]*vals[2]

print(sum([power(grabs) for _, grabs in games]))