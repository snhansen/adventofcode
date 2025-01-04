with open("input") as f:
    inp = f.read().strip()

instr_init = []
for line in inp.split("\n"):
    op, *rest = line.split(" ")
    instr_init.append((op, rest))

# After inspecting the input, we note that the sequence:
# 
# inc a
# dec c
# jnz c -2
# dec d
# jnz d -5
#
# will add c*d to a and reset c and d to 0. We replace this with a
# new operation caled mlt x y which multiplies registers x and y 
# and adds the result to register a:
#
# mlt c d
# cpy 0 c
# cpy 0 d
# cpy 0 c
# cpy 0 d
#
# The reason we have the two cpy instructions twice is to keep the
# instructions at the same length.

instr_init[5:10] = [
    ("mlt", ["c", "d"]),
    ("cpy", ["0", "c"]),
    ("cpy", ["0", "d"]),
    ("cpy", ["0", "c"]),
    ("cpy", ["0", "d"])
]

    
def solve(a):
    register = {x: 0 for x in ("a", "b", "c", "d")}
    register["a"] = a
    pointer = 0
    instr = list(instr_init)
    while pointer < len(instr):
        op, rest = instr[pointer]
        if op == "cpy":
            val, target = rest
            register[target] = int(val) if val.lstrip("-").isnumeric() else int(register[val])
        elif op == "inc":
            register[rest[0]] += 1
        elif op == "dec":
            register[rest[0]] -= 1
        elif op == "jnz":
            x, y = rest
            decider = int(x) if x.isnumeric() else register[x]
            y = int(y) if y.lstrip("-").isnumeric() else register[y]
            if decider != 0:
                pointer += y
                continue
        elif op == "tgl":
            t_pointer = pointer + register[rest[0]]
            if t_pointer < len(instr):
                t_op, t_rest = instr[t_pointer]
                if t_op == "inc":
                    instr[t_pointer] = ("dec", t_rest)
                elif t_op == "dec":
                    instr[t_pointer] = ("inc", t_rest)
                elif t_op == "tgl":
                    instr[t_pointer] = ("inc", t_rest)
                elif t_op == "jnz":
                    instr[t_pointer] = ("cpy", t_rest)
                elif t_op == "cpy":
                    instr[t_pointer] = ("jnz", t_rest)
        elif op == "mlt":
            register["a"] += register[rest[0]]*register[rest[1]]
        pointer += 1
    return register["a"]


# Part 1
print(solve(7))

# Part 2
print(solve(12))