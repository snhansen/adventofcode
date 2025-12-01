with open("input") as f:
    inp = f.read().strip().split("\n")


# Part 1
dial, c = 50, 0
for line in inp:
    dir_ = line[0]
    n = int(line[1:])
    if dir_ == "R":
        dial += n
    else:
        dial -= n
    dial = dial % 100
    c += (dial == 0)
        
print(c)


# Part 2
dial, c = 50, 0
for line in inp:
    dir_ = line[0]
    n = int(line[1:])
    for _ in range(n):
        if dir_ == "R":
            dial += 1
        else:
            dial -= 1
        dial = dial % 100
        c += (dial == 0)
        
print(c)