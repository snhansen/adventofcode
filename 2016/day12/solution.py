with open("input") as f:
    inp = f.read().strip()

instr = []
for line in inp.split("\n"):
    op, *rest = line.split(" ")
    instr.append((op, rest))
    

def solve(c):
    register = {x: 0 for x in ("a", "b", "c", "d")}
    register["c"] = c
    pointer = 0
    while pointer < len(instr):
        op, rest = instr[pointer]
        if op == "cpy":
            val, target = rest
            register[target] = int(val) if val.isnumeric() else int(register[val])
        elif op == "inc":
            register[rest[0]] += 1
        elif op == "dec":
            register[rest[0]] -= 1
        elif op == "jnz":
            x, y = rest
            decider = int(x) if x.isnumeric() else register[x]
            if decider != 0:
                pointer += int(y)
                continue
        pointer += 1
    return register["a"]

# Part 1
print(solve(0))

# Part 2
print(solve(1))