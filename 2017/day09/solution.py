with open("input") as f:
    inp = f.read().strip()

i = 0
group_score = 0
garbage = False
groups = []
c_garbage = 0
while i < len(inp):
    c = inp[i]
    if c == "<" and not garbage:
        garbage = True
        c_garbage -= 1
    elif c == ">" and garbage:
        garbage = False
    elif c == "!" and garbage:
        i += 2
        continue
    elif c == "{" and not garbage:
        group_score += 1
    elif c == "}" and not garbage:
        groups.append(group_score)
        group_score -= 1
    if garbage:
        c_garbage += 1
    i += 1

# Part 1
print(sum(groups))

# Part 2
print(c_garbage)