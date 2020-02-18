with open('input') as f:
    inp = [int(x) for x in f.readlines()]

# Part 1
def fuel(x):
    return x//3 - 2

print(sum(map(fuel, inp)))

# Part 2
def total_fuel(x):
    totalfuel = 0
    while True:
        temp = fuel(x)
        if temp > 0:
            totalfuel += temp
            x = temp
        else:
            break
    
    return totalfuel

print(sum(map(total_fuel, inp)))
