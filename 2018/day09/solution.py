from itertools import cycle
from collections import defaultdict


class Marble:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


def solve(max_value):
    scores = defaultdict(int)
    players = cycle(range(418))
    circle = [Marble(0)]
    circle[0].next = circle[0]
    circle[0].prev = circle[0]
    player = next(players)
    cur_marble = circle[0]
    for value in range(1, max_value + 1):
        player = next(players)
        if value % 23 == 0:
            scores[player] += value
            for _ in range(7):
                cur_marble = cur_marble.prev
            scores[player] += cur_marble.value
            cur_marble.prev.next = cur_marble.next
            cur_marble.next.prev = cur_marble.prev
            cur_marble = cur_marble.next
        else:
            marble = Marble(value)
            right = cur_marble.next.next
            left = cur_marble.next
            right.prev = marble
            marble.next = right
            left.next = marble
            marble.prev = left
            cur_marble = marble
            circle.append(marble)
    
    return max(scores.values())


# Part 1
print(solve(71339))

# Part 2
print(solve(71339*100))