import re

with open("input") as f:
    inp = f.read().strip().split("\n")

games = []
for line in inp:
    game, grabs = line.split(": ")
    game = re.search("\d+", game).group()
    grabs = grabs.replace(";", ",")
    grabs = grabs.split(", ")
    grabs = [(int(grab.split()[0]), grab.split()[1]) for grab in grabs]
    games.append((int(game), grabs))

# Part 1
def valid_game(ls):
    cubes = {"red": 12, "green": 13, "blue": 14}
    for val, color in ls:
        if val > cubes[color]:
            return False
    return True

print(sum([game for game, grabs in games if valid_game(grabs)]))

# Part 2
def min_cubes(grabs):
    cubes = {"red": 0, "green": 0, "blue": 0}
    for val, color in grabs:
        cubes[color] = max(cubes[color], val)
    return list(cubes.values())

power = 0
for game, grabs in games:
    red, green, blue = min_cubes(grabs)
    power += red*green*blue
    
print(power)