from collections import defaultdict

with open("input") as f:
    inp = f.read().split("\n")


sizes = defaultdict(int)
path = []
for line in inp:
    if line[0:4] == "$ cd":
        dir_ = line[5:]
        if dir_ != "..":
            path.append(dir_)
        else:
            path.pop()
    if line[0].isnumeric():
        size, _ = line.split(" ")
        size = int(size)
        for i in range(len(path)):
            folder = "/" + "".join([f"{dir}/" for dir in path[1:i+1]])
            sizes[folder] += size

# Part 1
print(sum(size for size in sizes.values() if size <= 100000))

# Part 2
free = 70000000 - sizes["/"]
print(min(size for size in sizes.values() if size + free >= 30000000))