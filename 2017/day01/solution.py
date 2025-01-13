with open("input") as f:
    inp = f.read().strip()

# Part 1
print(sum(int(x) for x, y in zip(inp, inp[1:] + inp[0]) if x == y))

# Part 2
ans = 0
for i in range(len(inp)):
    if inp[i] == inp[(i + len(inp)//2) % len(inp)]:
        ans += int(inp[i])

print(ans)