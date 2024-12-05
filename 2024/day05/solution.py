from collections import defaultdict

with open("input") as f:
    inp = f.read().strip()

inp1, inp2 = inp.split("\n\n")

rules = defaultdict(set)
for line in inp1.split("\n"):
    x, y = map(int, line.split("|"))
    rules[x].add(y)

updates = [list(map(int, line.split(","))) for line in inp2.split("\n")]


def right_order(update):
    for i, page in enumerate(update):
        if not (set(update[i+1:]) <= rules[page]):
            return False
    return True


# Part 1
print(sum(update[len(update)//2] for update in updates if right_order(update)))

# Part 2
def correct_order(update):
    while not right_order(update):
        for i, page in enumerate(update):
            if not (set(update[i+1:]) <= rules[page]):
                update.append(update.pop(i))
                break
    return update


corrected_updates = [correct_order(update) for update in updates if not right_order(update)]
print(sum(update[len(update)//2] for update in corrected_updates))