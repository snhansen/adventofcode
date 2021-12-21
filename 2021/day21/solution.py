from itertools import product
from collections import Counter
from functools import lru_cache

# Part 1
pos = [6, 4]
score = [0, 0]
i = 0
while True:
    roll = (3*i)%100+1 + (3*i+1)%100+1 + (3*i+2)%100+1    
    pos[i%2] += roll
    while pos[i%2] > 10:
        pos[i%2] -= 10
    score[i%2] += pos[i%2]
    if score[i%2] >= 1000:
        print(min(score)*(i+1)*3)
        break
    i += 1


# Part 2
sums = Counter([sum(r) for r in product([1,2,3], repeat=3)])

@lru_cache(maxsize=None)
def get_wins(config): # config = (pos1, pos2, score1, score2, turn)
    if config[2] >= 21:
        return 1, 0
    elif config[3] >= 21:
        return 0, 1
    p1wins, p2wins = 0, 0
    turn = config[4]
    for s in sums:
        new_pos = list(config[:2])
        new_pos[turn] += s
        while new_pos[turn] > 10:
            new_pos[turn] -= 10
        new_score = list(config[2:4])
        new_score[turn] += new_pos[turn]
        new_config = (new_pos[0], new_pos[1], new_score[0], new_score[1], (turn+1)%2)
        p1, p2 = get_wins(new_config)
        p1wins += sums[s]*p1
        p2wins += sums[s]*p2
    return p1wins, p2wins
    
print(max(get_wins((6,4,0,0,0))))