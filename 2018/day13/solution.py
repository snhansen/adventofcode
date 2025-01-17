with open("input") as f:
    inp = f.read().split("\n")


cart_dirs = {">": 1, "<": -1, "^": -1j, "v": 1j}
cart_to_rail = {">": "-", "<": "-", "^": "|", "v": "|"}
track = {}
carts = []
for y, line in enumerate(inp):
    for x, c in enumerate(line):
        p = x + y*1j
        if c in cart_dirs:
            carts.append((p, cart_dirs[c], 0))
            c = cart_to_rail[c]
        track[p] = c


def print_(carts):
    cart_dirs_inv = {v: k for k, v in cart_dirs.items()}
    xmin = int(min(p.real for p in track))
    xmax = int(max(p.real for p in track))
    ymin = int(min(p.imag for p in track))
    ymax = int(max(p.imag for p in track))
    for y in range(ymin, ymax + 1):
        line = ""
        for x in range(xmin, xmax + 1):
            p = x + y*1j
            c = track[p] if p in track else " "
            for pc, dc, _ in carts:
                if p == pc:
                    c = cart_dirs_inv[dc]
            line += c
        print(line)


def update(carts):
    global first
    new_carts = []
    carts = sorted(carts, key = lambda x: (x[0].imag, x[0].real))
    #for pc, dc, ic in carts:
    while carts:
        collision = False
        pc, dc, ic = carts.pop(0)
        t = track[pc]
        # If at an intersection, change direction.
        if t == "+":
            dc *= dirs[ic]
            ic = (ic + 1) % len(dirs)
        # Move forward one step
        pc += dc
        # If we land on a curve, then we change direction accordingly.
        newt = track[pc]
        match [newt, dc]:
            case ["/", -1j] | ["\\", 1] | ["/", 1j] | ["\\", -1]:
                dc *= 1j
            case ["/", -1] | ["\\", 1j] | ["/", 1] | ["\\", -1j]:
                dc *= -1j
        # Before proceeding we check for collisions against any moved and non-moved carts.
        for i, (p, _, _) in enumerate(carts):
            if p == pc:
                carts.pop(i)
                collision = True
                break
        for i, (p, _, _) in enumerate(new_carts):
            if p == pc:
                new_carts.pop(i)
                collision = True
                break
        if collision and first:
            print(f"{int(pc.real)},{int(pc.imag)}")
            first = False
        if not collision:
            new_carts.append((pc, dc, ic))
    return new_carts


dirs = [-1j, 1, 1j]
first = True
while len(carts) > 1:
    carts = update(carts)

print(f"{int(carts[0][0].real)},{int(carts[0][0].imag)}")