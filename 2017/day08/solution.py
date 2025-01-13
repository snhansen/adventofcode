from collections import defaultdict

with open("input") as f:
    inp = f.read().strip()

reg = defaultdict(int)
reg_max = 0
for instr in inp.split("\n"):
    first, last = instr.split(" if ")
    target, op, val = first.split(" ")
    op = "+=" if op == "inc" else "-="
    rel_reg, rel_op, rel_val  = last.split(" ")
    string = f"if reg[\"{rel_reg}\"] {rel_op} {rel_val}: reg[\"{target}\"] {op} {val}"
    exec(string)
    reg_max= max(max(reg.values()), reg_max)

# Part 1
print(max(reg.values()))

# Part 2
print(reg_max)