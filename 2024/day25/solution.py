with open("input") as f:
    inp = f.read().strip()

locks = []
keys = []
for line in inp.split("\n\n"):
    rows = line.split("\n")
    res = [sum(1 for i in range(0, 7) if rows[i][j] == "#") for j in range(5)]
    if all(cell == "#" for cell in rows[0]):
        locks.append(res)
    else:
        keys.append(res)

# Part 1
print(sum(1 for lock in locks for key in keys if all(x + y <= 7 for x, y in zip(lock, key))))