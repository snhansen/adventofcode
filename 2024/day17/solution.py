import re

with open("input") as f:
    inp1, inp2 = f.read().strip().split("\n\n")

registers = {chr(65+i): int(n) for i, n in enumerate(re.findall("\d+", inp1))}
program = list(map(int, re.findall("\d+", inp2)))


class computer:
    def __init__(self, registers, program):
        self.registers = dict(registers)
        self.program = program
        self.instr_pointer = 0
        self.program_len = len(program)
        self.output = []
        
    def set_instr_pointer(self, value):
        self.instr_pointer = value
    
    def combo(self, operand):
        match operand:
            case 0 | 1 | 2 | 3:
                return operand
            case 4:
                return self.registers["A"]
            case 5:
                return self.registers["B"]
            case 6:
                return self.registers["C"]
            case 7:
                raise Exception(f"Bad operand input {operand}.")

    def run(self):
        if self.instr_pointer >= self.program_len:
            return 0
        opcode = self.program[self.instr_pointer]
        operand = self.program[self.instr_pointer + 1]
        if opcode == 0:
            self.registers["A"] = self.registers["A"] // (2**self.combo(operand))
        elif opcode == 1:
            self.registers["B"] = self.registers["B"] ^ operand
        elif opcode == 2:
            self.registers["B"] = self.combo(operand) % 8
        elif opcode == 3:
            if self.registers["A"] != 0:
                self.instr_pointer = operand - 2
        elif opcode == 4:
            self.registers["B"] = self.registers["B"] ^ self.registers["C"]
        elif opcode == 5:
            self.output.append(self.combo(operand) % 8)
        elif opcode == 6:
            self.registers["B"] = self.registers["A"] // (2**self.combo(operand))
        elif opcode == 7:
            self.registers["C"] = self.registers["A"] // (2**self.combo(operand))
        else:
            raise Exception(f"Bad opcode {opcode}!")
        self.instr_pointer += 2
        return 1 if opcode != 5 else 2

    def run_till_halt(self):
        while self.run():
            continue
    
    def run_till_output_or_halt(self):
        while True:
            val = self.run()
            if val != 1:
                break
        return val


# Part 1
comp = computer(registers, program)
comp.run_till_halt()
print(",".join(map(str, comp.output)))

def get_output(A):
    res = []
    while A > 0:
        res.append(((((A % 8) ^ 7) ^ (A // (2 ** ((A % 8) ^ 7)))) ^ 7) % 8)
        A = A // (2**3)
    return res

print(",".join(map(str, get_output(registers["A"]))))

# Part 2
to_check = [0]
for length in range(1, len(program) + 1):
    new_to_check = []
    for num in to_check:
        for newnum in range(8*num, 8*(num + 1)):
            if get_output(newnum) == program[-length:]:
                new_to_check.append(newnum)
    to_check = new_to_check

print(min(to_check))