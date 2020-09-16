with open('input') as f:
    inp = [x.strip() for x in f.readlines()]

# Part 1
print(sum([len(x) for x in inp]) - sum([len(bytes(x, "utf-8").decode("unicode_escape"))-2 for x in inp]))

# Part 2
print(sum([len(x)+2+x.count('"')+x.count('\\') for x in inp]) - sum([len(x) for x in inp]))

