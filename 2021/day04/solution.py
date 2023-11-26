from collections import deque
import re

with open('input') as f:
    inp =  f.read().split('\n\n')

numbers = deque(list(map(int, inp[0].split(','))))
boards = []
drawn = []
for i in range(1, len(inp)):
    boards.append([list(map(int, re.findall('\d+', inp[i]))), [0]*10])

def draw_number():
    num = numbers.popleft()
    drawn.append(num)
    for board in boards:
        for i in range(len(board[0])):
            if board[0][i] == num:
                board[1][i // 5] += 1
                board[1][5 + (i % 5)] += 1

def check_boards(bs):
    ws = []
    for b in bs:
        for s in b[1]:
            if s == 5:
                ws.append(b)
                bs.remove(b)
                break
    return ws, bs

# Part 1 and 2
j = 0
while numbers:
    draw_number()
    winners, boards = check_boards(boards)
    if winners:
        if j == 0:
            print(sum([x for x in winners[0][0] if x not in drawn])*drawn[-1])
        cur_winners = list(winners)
        cur_drawn = list(drawn)
        j = 1

print(sum([x for x in cur_winners[0][0] if x not in cur_drawn])*cur_drawn[-1])
