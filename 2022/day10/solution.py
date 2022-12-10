with open("input") as f:
    inp = f.read().strip().split("\n")

vals = [1, 1]
i = 0
while True:
    instr = inp[i%len(inp)]
    val = vals[-1]
    match instr.split(" "):
        case ["noop"]:
            vals.append(val)
        case [_, x]:
            val += int(x)
            vals.append(val)
            vals.append(val)
    i += 1
    if len(vals) > 240:
        break

# Part 1
print(sum((i*vals[i-1] for i in (20, 60, 100, 140, 180, 220))))

# Part 2
screen = []
for row in range(6):
    pixels = []
    for cycle in range(40):
        x = vals[row*40 + cycle]
        sprite = range(x-1,x+2)
        draw = "#" if cycle in sprite else "."
        pixels.append(draw)
    screen.append(pixels)

for row in range(6):
    print("".join(screen[row]))