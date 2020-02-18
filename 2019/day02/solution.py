with open('input') as f:
    inp = list(map(int, f.read().split(',')))

def intcode(a, b, x):
    x = list(x)
    x[1] = a
    x[2] = b
    i = 0
    while True:
        if x[i] == 99:
            break
        elif x[i] == 1:
            x[x[i+3]] = x[x[i+1]] + x[x[i+2]]
        elif x[i] == 2:
            x[x[i+3]] = x[x[i+1]] * x[x[i+2]]
        i += 4
    return x[0]

# Part 1
print(intcode(12, 2, inp))

# Part 2
import itertools 
for a, b in itertools.product(range(100), range(100)):
    if intcode(a, b, inp) == 19690720:
        print(100*a + b)
        break