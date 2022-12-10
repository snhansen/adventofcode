with open("input") as f:
    inp = f.read().strip().split("\n")

vals = [1]
for instr in inp:
    val = vals[-1]
    vals.append(val)
    match instr.split(" "):
        case [_, x]:
            vals.append(val + int(x))

# Part 1
print(sum((i*vals[i-1] for i in (20, 60, 100, 140, 180, 220))))

# Part 2
screen = []
for row in range(6):
    pixels = []
    for cycle in range(40):
        x = vals[row*40 + cycle]
        draw = "█" if abs(cycle - x) <= 1 else " "
        pixels.append(draw)
    screen.append(pixels)

for row in range(6):
    print("".join(screen[row]))