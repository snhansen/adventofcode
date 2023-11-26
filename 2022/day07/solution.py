from collections import defaultdict

with open("input") as f:
    inp = f.read().split("\n")


sizes = defaultdict(int)
path = []
for line in inp:
    match line.split():
        case ["$", "cd", ".."]:
            path.pop()
        case ["$", "cd", dir_]:
            path.append(dir_)
        case [x, _] if x.isnumeric():
            for i in range(len(path)):
                folder = "/" + "".join([f"{dir_}/" for dir_ in path[1:i+1]])
                sizes[folder] += int(x)


# Part 1
print(sum(size for size in sizes.values() if size <= 100000))

# Part 2
free = 70000000 - sizes["/"]
print(min(size for size in sizes.values() if size + free >= 30000000))