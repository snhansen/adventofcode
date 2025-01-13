from collections import defaultdict, deque

with open("input") as f:
    inp = f.read().strip().split("\n")

instr = [line.split(" ") for line in inp]


class program:
    def __init__(self, program):
        self.program = program
        self.snd = deque([])
        self.rcv = deque([])
        self.p = 0
        self.regs = defaultdict(int)
        self.regs["p"] = program
        self.sent = 0


    def run(self):
        op, *rest = instr[self.p]
        if op not in ["snd", "rcv"]:
            x, y = rest
            y = int(y) if y.lstrip("-").isnumeric() else self.regs[y]
        else:
            x,  = rest
        if op == "set": 
            self.regs[x] = y
        elif op == "add":
            self.regs[x] += y
        elif op == "mul":
            self.regs[x] *= y
        elif op == "mod":
            self.regs[x] %= y
        elif op == "jgz":
            decider = int(x) if x.lstrip("-").isnumeric() else self.regs[x]
            if decider > 0:
                self.p += y - 1
        elif op == "snd":
            val = int(x) if x.lstrip("-").isnumeric() else self.regs[x]
            self.snd.append(val)
            self.sent += 1
        elif op == "rcv":
            if len(self.rcv) == 0:
                return 1
            self.regs[x] = self.rcv.popleft()
        self.p += 1


    def run_till_rcv_needed(self):
        while True:
            is_empty = self.run()
            if is_empty:
                break

            
def update_snd_rcv(prg0, prg1):
    while prg0.snd:
        prg1.rcv.append(prg0.snd.popleft())
    while prg1.snd:
        prg0.rcv.append(prg1.snd.popleft())


# Part 1
prg0 = program(0)
prg0.run_till_rcv_needed()
print(prg0.snd[-1])

# Part 2
prg0 = program(0)
prg1 = program(1)

prg0.run_till_rcv_needed()
prg1.run_till_rcv_needed()
while len(prg0.snd) + len(prg1.snd) > 0:
    update_snd_rcv(prg0, prg1)
    prg0.run_till_rcv_needed()
    prg1.run_till_rcv_needed()

print(prg1.sent)