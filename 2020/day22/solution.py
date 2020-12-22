from collections import deque

with open('input') as f:
    inp = [list(map(int, x.splitlines()[1:])) for x in f.read().split('\n\n')]

def get_score(decks):
    return sum([sum([x*y for x, y in zip(reversed(range(1,len(deck)+1)), deck)]) for deck in decks])

# Part 1
decks = [deque(deck) for deck in inp]

while decks[0] and decks[1]:
    cards = [decks[i].popleft() for i in range(2)]
    if cards[0] > cards[1]:
        decks[0].extend(cards)
    else:
        decks[1].extend(reversed(cards))

print(get_score(decks))

# Part 2
decks = [deque(deck) for deck in inp]

def play(decks):
    history = set()
    while decks[0] and decks[1]:
        id = (tuple(decks[0]), tuple(decks[1]))
        if id in history:
            return [deque([0]), deque([])]
        else:
            history.add(id)
            cards = [decks[i].popleft() for i in range(2)]
            if cards[0] <= len(decks[0]) and cards[1] <= len(decks[1]):
                subdecks = [deque(list(decks[i])[:cards[i]]) for i in range(2)]
                res = play(subdecks)
                if len(res[0]) == 0:
                    decks[1].extend(reversed(cards))
                elif len(res[1]) == 0:
                    decks[0].extend(cards)
            else:
                if cards[0] > cards[1]:
                    decks[0].extend(cards)
                elif cards[1] > cards[0]:
                    decks[1].extend(reversed(cards))
    return decks

print(get_score(play(decks)))