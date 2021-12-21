from itertools import product
from collections import Counter
from functools import lru_cache

# Part 1
pos = [6, 4]
score = [0, 0]
i = 0
while True:
    roll = (3*i)%100+1 + (3*i+1)%100+1 + (3*i+2)%100+1    
    pos[i%2] = ((pos[i%2] - 1 + roll) % 10) + 1
    score[i%2] += pos[i%2]
    if score[i%2] >= 1000:
        print(min(score)*(i+1)*3)
        break
    i += 1


# Part 2
sums = Counter([sum(r) for r in product([1,2,3], repeat=3)])

@lru_cache(maxsize=None)
def get_wins(p1, p2, s1, s2, turn):
    if s1 >= 21:
        return 1, 0
    elif s2 >= 21:
        return 0, 1
    p1wins, p2wins = 0, 0
    turn
    for s in sums:
        new_pos = [p1, p2]
        new_pos[turn] = ((new_pos[turn] - 1 + s) % 10) + 1
        new_score = [s1, s2]
        new_score[turn] += new_pos[turn]
        p1sub, p2sub = get_wins(new_pos[0], new_pos[1], new_score[0], new_score[1], (turn+1)%2)
        p1wins += sums[s]*p1sub
        p2wins += sums[s]*p2sub
    return p1wins, p2wins
    
print(max(get_wins(6,4,0,0,0)))