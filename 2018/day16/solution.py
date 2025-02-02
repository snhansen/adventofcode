import re
from collections import defaultdict

with open("input") as f:
    first, last = f.read().strip().split("\n\n\n\n")


first = first.split("\n\n")
samples = []
for section in first:
    nums = list(map(int, re.findall("\d+", section)))
    samples.append((nums[:4], nums[4:8], nums[8:]))


def addr(regs, a, b, c):
    regs = list(regs)
    regs[c] = regs[a] + regs[b]
    return regs


def addi(regs, a, b, c):
    regs = list(regs)
    regs[c] = regs[a] + b
    return regs


def mulr(regs, a, b, c):
    regs = list(regs)
    regs[c] = regs[a]*regs[b]
    return regs


def muli(regs, a, b, c):
    regs = list(regs)
    regs[c] = regs[a]*b
    return regs


def banr(regs, a, b, c):
    regs = list(regs)
    regs[c] = regs[a] & regs[b]
    return regs


def bani(regs, a, b, c):
    regs = list(regs)
    regs[c] = regs[a] & b
    return regs


def borr(regs, a, b, c):
    regs = list(regs)
    regs[c] = regs[a] | regs[b]
    return regs


def bori(regs, a, b, c):
    regs = list(regs)
    regs[c] = regs[a] | b
    return regs


def setr(regs, a, b, c):
    regs = list(regs)
    regs[c] = regs[a]
    return regs


def seti(regs, a, b, c):
    regs = list(regs)
    regs[c] = a
    return regs


def gtir(regs, a, b, c):
    regs = list(regs)
    regs[c] = int(a > regs[b])
    return regs


def gtri(regs, a, b, c):
    regs = list(regs)
    regs[c] = int(regs[b] > b)
    return regs


def gtrr(regs, a, b, c):
    regs = list(regs)
    regs[c] = int(regs[a] > regs[b])
    return regs


def eqir(regs, a, b, c):
    regs = list(regs)
    regs[c] = int(a == regs[b])
    return regs


def eqri(regs, a, b, c):
    regs = list(regs)
    regs[c] = int(regs[a] == b)
    return regs


def eqrr(regs, a, b, c):
    regs = list(regs)
    regs[c] = int(regs[a] == regs[b])
    return regs


ops = {addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr}
functions = defaultdict(lambda: set(ops))
ans = 0
for sample in samples:
    res = set()
    regs_bef, instr, regs_aft = sample
    n, a, b, c = instr
    res = {op for op in ops if regs_aft == op(regs_bef, a, b, c)}
    if len(res) >= 3:
        ans += 1
    functions[n] &= res

print(ans)

# Part 2
opcodes = {}
while len(opcodes) < len(ops):
    for n, fcts in functions.items():
        if len(fcts) == 1:
            opcodes[n] = fcts.pop()
    for fcts in functions.values():
        fcts -= set(opcodes.values())

regs = [0]*4
for line in last.split("\n"):
    nums = list(map(int, re.findall("\d+", line)))
    n, a, b, c = nums
    regs = opcodes[n](regs, a, b, c)

print(regs[0])