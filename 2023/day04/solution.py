import re

with open("input") as f:
    inp = f.read().strip().split("\n")

cards = []
for line in inp:
    win, mine = line.split(": ")[1].split(" | ")
    win = set(map(int, re.findall("\d+", win)))
    mine = set(map(int, re.findall("\d+", mine)))
    cards.append(len(win & mine))

# Part 1    
print(sum([int(2**(n-1)) for n in cards if n > 0]))

# Part 2
copies = {i: 1 for i in range(len(cards))}

for i, n in enumerate(cards):
    if n > 0:
        for j in range(i+1, (i+1+n)):
            copies[j] += copies[i]

print(sum(copies.values()))