# The IntCode machine as a class. Heavily inspired by https://github.com/fuglede
from collections import deque
from collections import defaultdict

                
class intcode_machine:
    def __init__(self, program, inputs=[]):
        self.i = 0
        self.l = defaultdict(int, enumerate(program))
        self.inputs = deque(inputs)
        self.opcode = None
        self.output = None
        self.relbase = 0
        
    def __getitem__(self, index):
        return self.l[index]
    
    def __setitem__(self, index, val):
        self.l[index] = val
        
    def set_inputs(self, new_input):
        self.inputs = deque(new_input)
    
    def add_inputs(self, new_input):
        for x in new_input:        
            self.inputs.append(x)
    
    def run(self):
        instr = str(self[self.i]).zfill(5)
        self.opcode = int(instr[3:])
        parmode = instr[0:3]
        address = []
        for k in range(3):
            if int(parmode[2-k]) == 0:
                try:
                    address.append(self[self.i+k+1])
                except IndexError:
                    pass
            elif int(parmode[2-k]) == 1:
                address.append(self.i+k+1)
            elif int(parmode[2-k]) == 2:
                address.append(self[self.i+k+1]+self.relbase)
        
        if self.opcode != 99:
            x0 = self[address[0]]
        if self.opcode in [1, 2, 5, 6, 7, 8]:
            x1 = self[address[1]]
        if self.opcode == 1:
            self[address[2]] = x0 + x1
            self.i += 4
        elif self.opcode == 2:
            self[address[2]] = x0 * x1
            self.i += 4
        elif self.opcode == 3:
            self[address[0]] = self.inputs.popleft()
            self.i += 2
        elif self.opcode == 4:
            self.i += 2
            self.output = x0
        elif self.opcode == 5:
            self.i = x1 if x0 != 0 else self.i + 3
        elif self.opcode == 6:
            self.i = x1 if x0 == 0 else self.i + 3
        elif self.opcode == 7:
            self[address[2]] = 1 if x0 < x1 else 0
            self.i += 4
        elif self.opcode == 8:
            self[address[2]] = 1 if x0 == x1 else 0
            self.i += 4
        elif self.opcode == 9:
            self.relbase += x0
            self.i += 2
    
    def run_till_halt(self):
        while self.opcode != 99:
            self.run()
        return self.output
    
    def run_till_output_or_halt(self):
        while self.opcode not in [4, 99]:
            self.run()
        if self.opcode == 99:
            self.opcode = None
            return 1, self.output
        elif self.opcode == 4:
            self.opcode = None
            return 0, self.output
