# Part 1
steps = 356
buffer = [0]
pos, c = 0, 1

for _ in range(2017):
    index = 1 + (pos + steps) % len(buffer)
    buffer.insert(index, c)
    pos = index
    c += 1

print(buffer[pos + 1])

# Part 2
pos = 0
steps = 356

for n in range(50000001):
    if n < 2:
        pos = n
    else:
        pos = 1 + (pos + 356) % n
    if pos == 1:
        val = n
    
print(val)