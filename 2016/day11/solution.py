from itertools import combinations
from collections import deque


def bad_state(chips, generators):
    for chip, gen in zip(chips, generators):
        for other_gen in generators:
            if gen == other_gen:
                continue
            if chip == other_gen and chip != gen:
                return True
    return False


def solve(chips, generators):
    q = deque([(0, 1, chips, generators)])
    seen = set()
    while q:
        steps, floor, chips, generators = q.popleft()
        if (floor, chips, generators) in seen:
            continue
        seen.add((floor, chips, generators))
        if all(chip == 4 for chip in chips) and all(gen == 4 for gen in generators):
            return steps
        # Purge wrong states: if any chip is at a floor with another generator but not its own generator, then we purge.
        if bad_state(chips, generators):
            continue
        # Need to move one or two items to a floor above or below.
        avail_items = [i for i, x in enumerate(chips) if x == floor]
        avail_items += [i + len(chips) for i, x in enumerate(generators) if x == floor]
        for new_floor in {floor - 1, floor + 1} & {1, 2, 3, 4}:
            for items in combinations(avail_items + [None], 2):
                new_chips = list(chips)
                new_generators = list(generators)
                for item in items:
                    if item is not None:
                        if item < len(chips):
                            new_chips[item] = new_floor
                        else:
                            new_generators[item - len(chips)] = new_floor
                q.append((steps + 1, new_floor, tuple(new_chips), tuple(new_generators)))

# Part 1
print(solve((1, 1, 3, 2, 2), (1, 1, 2, 2, 2)))

# Part 2
print(solve((1, 1, 3, 2, 2, 1, 1), (1, 1, 2, 2, 2, 1, 1)))