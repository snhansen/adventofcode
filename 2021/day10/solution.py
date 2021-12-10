with open('input') as f:
    inp = [x.strip() for x in f.readlines()]


close = {'(': ')', '[': ']', '{': '}', '<': '>'}

# Part 1
chars = []
for s in list(inp):
    opens = []
    for x in s:
        if x in close.keys():
            opens.append(x)
        elif x in close.values():
            y = opens.pop()
            if x != close[y]:
                chars.append(x)
                inp.remove(s)
                break

points = {')': 3, ']': 57, '}': 1197, '>': 25137}
print(sum([points[c] for c in chars]))
    
# Part 2
scores = []
points = {')': 1, ']': 2, '}': 3, '>': 4}
for s in inp:
    opens = []
    for x in s:
        opens.append(x) if x in close.keys() else opens.pop()
    score = 0
    for x in [close[o] for o in reversed(opens)]:
        score = score*5 + points[x]
    scores.append(score)

scores.sort()
print(scores[len(scores)//2])