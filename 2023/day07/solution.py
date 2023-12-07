from collections import Counter
from functools import cmp_to_key
from itertools import product

with open("input") as f:
    inp = f.read().strip().split("\n")

d = {str(i): i for i in range(2, 10)} | {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
bids = {}

hands = []
for line in inp:
    hand, bid = line.split(" ")
    bids[hand] = int(bid)
    hands.append(hand)
    

# 1: five of a kind, 2: four of a kind, 3: full house, 4: three of a kind,
# 5: two pair, 6: one pair, 7: high card
def get_type(hand):
    c = Counter([d[x] for x in hand])
    vals = sorted(list(c.values()))
    if len(c.keys()) == 1:
        return 1
    if len(c.keys()) == 2:
        if vals[1] == 4:
            return 2
        if vals[1] == 3:
            return 3
    if len(c.keys()) == 3:
        if vals[2] == 3:
            return 4
        return 5
    if len(c.keys()) == 4:
        return 6
    return 7

def compare_hands(hand0, hand1):
    type0, type1 = get_type(hand0), get_type(hand1)
    if type0 < type1:
        return 1
    elif type0 > type1:
        return -1
    else:
        for x, y in zip(hand0, hand1):
            if d[x] < d[y]:
                return -1
            elif d[x] > d[y]:
                return 1
        return 0

# Part 1
res = 0
for i, hand in enumerate(sorted(hands, key = cmp_to_key(compare_hands))):
    res += bids[hand]*(i+1)

print(res)


# Part 2
d["J"] = 1

def get_best_hand(hand):
    if hand == "JJJJJ":
        return "AAAAA"
    hands = []
    indices = [i for i, card in enumerate(hand) if card == "J"]
    if not indices:
        return hand
    for vals in product(list(d.keys()), repeat = len(indices)):
        new_hand = hand
        for j, index in enumerate(indices):
            new_hand = new_hand[:index] + vals[j] + new_hand[(index+1):]
        hands.append(new_hand)
    return sorted(hands, key = cmp_to_key(compare_hands), reverse = True)[0]


def compare_hands2(hand0, hand1):
    hand0, best_hand0 = hand0
    hand1, best_hand1 = hand1
    type0, type1 = get_type(best_hand0), get_type(best_hand1)
    if type0 < type1:
        return 1
    elif type0 > type1:
        return -1
    else:
        for x, y in zip(hand0, hand1):
            if d[x] < d[y]:
                return -1
            elif d[x] > d[y]:
                return 1
        return 0


best_hands = [(hand, get_best_hand(hand)) for hand in hands]
res = 0
for i, (hand, _) in enumerate(sorted(best_hands, key = cmp_to_key(compare_hands2))):
    res += bids[hand]*(i+1)

print(res)