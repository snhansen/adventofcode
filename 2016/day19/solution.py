from collections import deque

inp = 3017957

# Part 1
def one_round(start, end, inc):
    n = (end - start + inc) // inc
    if n % 2 == 0:
        return (start, end - inc, 2*inc)
    else:
        return (start + 2*inc, end, 2*inc)

start, end, inc = 1, inp, 1
while start + inc <= end:
    start, end, inc = one_round(start, end, inc)

print(start)

# Part 2
left = deque(list(range(1, inp // 2 + 2)))
right = deque(list(range(inp // 2 + 2, inp + 1)))

while len(left) + len(right) > 1:
    elf = left.popleft()
    if (len(left) + len(right)) % 2 == 1:
        right.popleft()
    else:
        left.pop()
    right.append(elf)
    left.append(right.popleft())
 
print(left[0])