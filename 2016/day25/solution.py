with open("input") as f:
    inp = f.read().strip()

# If x is the input to register a, then the program does the following:
#
# Instructions 0 to 8 is carried out once to yield:
#
#   a = 633*4 + x, b = 0, c = 0, d = 633*4 + x
#
# Instructions 9 to 27 does the following:
#
# - a is halved (rounded down)
# - b is the remainder after division with 2
# - c and d are unaltered (d keeps 633*4 + x throughout the program)
#
# For example, after the first round we get:
#	
#   a = (633*4 + x) // 2, b = (633*4 + x) % 2, c = 0, d = 633*4 + x
#
# This is continued until a is 0 after which the process repeats itself
# because d is copied to a and d holds 633*4 + x.
#
# This means we're looking for a number that, in binary, has the pattern
# 10...10. Since x >= 0, the first such number of the form 633*4 + x is
# 2730 (101010101010), which is obtained when x = 198.

instr = []
for line in inp.split("\n"):
    op, *rest = line.split(" ")
    instr.append((op, rest))

register = {x: 0 for x in ("a", "b", "c", "d")}
register["a"] = 198
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
    elif op == "out":
        print(register[rest[0]])
    pointer += 1