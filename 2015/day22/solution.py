from collections import deque
from heapq import heappop, heappush

class game:
    def __init__(self, hp, mana, armor, dmg, spells = deque(), diff = 'easy'):
        self.hp = hp[0]
        self.mana = mana
        self.armor = armor
        self.bosshp = hp[1]
        self.bossdmg = dmg
        self.shield = deque()
        self.poison = deque()
        self.recharge = deque()
        self.spells = spells
        self.mana_spent = 0
        self.diff = diff
        self.winner = None
    
    def add_spells(self, ls):
        for l in ls:
            self.spells.append(l)
    
    def throw_spell(self, sp):
        if sp == 0:
            self.mana -= 53
            self.mana_spent += 53
            self.bosshp -= 4
        elif sp == 1:
            self.mana -= 73
            self.mana_spent += 73
            self.bosshp -= 2
            self.hp += 2
        elif sp == 2:
            if self.shield:
                #print('Shield already active')
                return -1
            else:
                self.mana -= 113
                self.mana_spent += 113
                self.shield = deque([7]*5 + [self.armor])
                self.armor += 7
        elif sp == 3:
            if self.poison:
                #print('Poison already active')
                return -1
            else:
                self.mana -= 173
                self.mana_spent += 173
                self.poison = deque([3]*6)
        elif sp == 4:
            if self.recharge:
                #print('Recharge already active')
                return -1
            else:
                self.mana -= 229
                self.mana_spent += 229
                self.recharge = deque([101]*5)
    
    def player_turn(self):
        if self.winner:
            #print(f'Game already decided. Winner was {self.winner}')
            return self.winner
        elif not self.spells:
            #print('No spells to throw')
            return -1
        else:
            if self.diff == 'hard':
                self.hp -= 1
                if self.hp <= 0:
                    self.winner = 'Boss'
                    #print(f'Winner is {self.winner}')
                    return self.winner
            if self.recharge:
                self.mana += self.recharge.popleft()
            if self.shield:
                self.armor = self.shield.popleft()
            if self.poison:
                self.bosshp -= self.poison.popleft()
            mana_cost = [53, 63, 113, 163, 229]
            spell = self.spells.popleft()
            if mana_cost[spell]>self.mana:
                self.winner = 'Boss'
                #print('You cannot afford to cast spell and therefore lose')
                return self.winner
            else:
                x = self.throw_spell(spell)
                if x:
                    #print('Game terminated due to invalid spell sequence')
                    return -1
            if self.bosshp <= 0:
                self.winner = 'You'
                #print(f'Winner is {self.winner}')
                return self.winner
        
    def boss_turn(self):
        if self.winner:
            print(f'Game already decided. Winner was {self.winner}')
            return self.winner
        else:
            if self.recharge:
                self.mana += self.recharge.popleft()
            if self.shield:
                self.armor = self.shield.popleft()
            if self.poison:
                self.bosshp -= self.poison.popleft()
            if self.bosshp <= 0:
                self.winner = 'You'
                #print(f'Winner is {self.winner}')
                return self.winner
            self.hp -= max(self.bossdmg - self.armor, 1)
            if self.hp <= 0:
                self.winner = 'Boss'
                #print(f'Winner is {self.winner}')
                return self.winner
   
    def fight(self):
        while self.spells:
            x = self.player_turn()
            if x:
                return x
                break
            y = self.boss_turn()
            if y:
                return y
                break
    
    def clone(self):
        clone = game([self.hp, self.bosshp], self.mana, self.armor, self.bossdmg)
        clone.spells = deque(self.spells)
        clone.shield = deque(self.shield)
        clone.poison = deque(self.poison)
        clone.recharge = deque(self.recharge)
        clone.diff = self.diff
        clone.mana_spent = self.mana_spent
        clone.winner = self.winner
        return clone

# Part 1
gstart = game([50, 55], 500, 0, 8)
games = [(0, id(gstart), gstart)]
min_mana = float('inf')

while games:
    g = heappop(games)
    for i in range(5):
        c = g[2].clone()
        c.add_spells([i])
        x = c.fight()
        if x == 'You':
            min_mana = min(min_mana, c.mana_spent)
        elif x is None and c.mana_spent<min_mana:
            heappush(games, (c.mana_spent, id(c), c))

print(min_mana)
        

gstart = game([50, 55], 500, 0, 8, diff = 'hard')
games = [(0, id(gstart), gstart)]
min_mana = float('inf')

while games:
    g = heappop(games)
    for i in range(5):
        c = g[2].clone()
        c.add_spells([i])
        x = c.fight()
        if x == 'You':
            min_mana = min(min_mana, c.mana_spent)
        elif x is None and c.mana_spent<min_mana:
            heappush(games, (c.mana_spent, id(c), c))

print(min_mana)