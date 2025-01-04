with open("input") as f:
   inp = f.read().strip()

ranges = [tuple(map(int, line.split("-"))) for line in inp.split("\n")]

# Part 1
candidates = [0] + [end + 1 for _, end in ranges]

min_start = max(start for start, _ in ranges)
for candidate in candidates:
    good = True
    for start, end in ranges:
        if start <= candidate and candidate <= end:
            good = False
    if good:
        min_start = min(min_start, candidate)

print(min_start)

# Part 2
ticks = sorted([p for range in ranges for p in range])
disj_ranges = set()
for start, end in ranges:
    midps = [tick for tick in ticks if start < tick and tick < end]
    if not midps:
        disj_ranges.add((start, end))
    else:
        for p1, p2 in zip([start] + midps, midps + [end]):
            disj_ranges.add((p1, p2))

# Since the endpoints can be in multiple intervals we need to subtract how many times this occur.
blacklist_length = sum(y - x + 1 for x, y in disj_ranges)
endpoints = [p for range in disj_ranges for p in range]
n_blacklist = blacklist_length - (len(endpoints) - len(set(endpoints)))
print(2**32 - n_blacklist)