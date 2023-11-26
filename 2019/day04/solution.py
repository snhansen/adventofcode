def has_pair(x):
    count = 0
    for i in range(len(x)-1):
        count += (x[i] == x[i+1])
    return count > 0

def is_increasing(x):
    for i in range(len(x)-1):
        if x[i] > x[i+1]:
            return False
    return True

# Part 1
count = 0
for x in range(138241, 674035):
    if has_pair(str(x)) and is_increasing(str(x)):
        count += 1

print(count)

# Part 2
def has_pair2(x):
    count = 0
    count += x[0] == x[1] and x[1] != x[2]
    for i in range(1, len(x)-2):
        count += x[i-1] != x[i] and x[i] == x[i+1] and x[i+1] != x[i+2]
    count += x[len(x)-3] != x[len(x)-2] and x[len(x)-2] == x[len(x)-1]
    return count > 0

#Part 2
count = 0
for x in range(138241, 674035):
    if has_pair2(str(x)) and is_increasing(str(x)):
        count += 1

print(count)