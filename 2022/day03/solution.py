with open("input") as f:
    inp = [x.strip() for x in f.readlines()]


p1 = {chr(i): i-96 for i in range(97, 123)}
p2 = {chr(i): i-38 for i in range(65, 91)}
priority = p1 | p2

def get_common(ls):
    res = set.intersection(*ls)
    return list(res)[0]

# Part1
c = 0
for s in inp:
    ls = [set(s[:len(s)//2]), set(s[len(s)//2:])]
    c += priority[get_common(ls)]

print(c)

# Part 2
c = 0
for i in range(len(inp)//3):
    ls = [set(inp[i*3+j]) for j in range(3)]
    c += priority[get_common(ls)]

print(c)