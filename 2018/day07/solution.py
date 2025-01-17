import re
from collections import defaultdict

with open("input") as f:
    inp = f.read().strip().split("\n")

reqs = defaultdict(set)
reqs_inv = defaultdict(set)
for line in inp:
    first, second = list(re.findall("(?<=\s)[A-Z](?=\s)", line))
    reqs[second].add(first)
    reqs_inv[first].add(second)


# Part 1
temp = [item for ls in reqs.values() for item in ls]
avail = set()
for item in temp:
    if item not in reqs.keys():
        avail.add(item)

order = []
while avail:
    new_avail = sorted(list(avail))
    order.append(new_avail.pop(0))
    new_avail = set(new_avail)
    for candidate in reqs_inv[order[-1]]:
        if reqs[candidate] <= set(order):
            new_avail.add(candidate)
    avail = new_avail

print("".join(order))

# Part 2
letters = set(order)

steps = 0
done = []
workers = [(0, None)]*5
q = []

while len(done) < len(order):
    for letter in list(letters):
        if reqs[letter] <= set(done):
            q.append(letter)
            letters.remove(letter)

    # Update workers and take in new orders.
    for i, (time, item) in enumerate(workers):        
        if item is not None:
            workers[i] = (time - 1, item)
        else:
            if q:
                item = q.pop(0)
                workers[i] = (ord(item) - 4 - 1, item)
    
    # Check if workers are done.
    for i, (time, item) in enumerate(workers):
        if time == 0 and item is not None:
            done.append(item)
            workers[i] = (0, None)
    steps += 1

print(steps)