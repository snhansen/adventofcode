# The IntCode machine as a class. Heavily inspired by https://github.com/fuglede
from collections import defaultdict, deque

                
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

class maze_robot(intcode_machine):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.pos = 0
        self.visited = [0]
        self.status = 0
        self.dir_history = deque([])
    
    def clone(self):
        clone = maze_robot([])
        clone.i = self.i
        clone.l = defaultdict(int, self.l.items())
        clone.relbase = self.relbase
        clone.pos = self.pos
        clone.visited = list(self.visited)
        clone.dir_history = deque(self.dir_history)
        return clone
    
    def move(self, dir):
        coord = {1: 1j, 2: -1j, 3: -1, 4: 1}
        self.add_inputs([dir])
        _, status = self.run_till_output_or_halt()
        if status:
            self.status = status
            self.pos = self.pos + coord[dir]
            self.visited.append(self.pos)
            self.dir_history.append(dir)
        return status
        
    def get_dirs(self):
        o = {1: 2, 2: 1, 3: 4, 4: 3}
        dirs = []
        for dir in range(1,5):
            self.add_inputs([dir])
            _, status = self.run_till_output_or_halt()
            if status:
                dirs.append(dir)
                self.add_inputs([o[dir]])
                self.run_till_output_or_halt()
        return dirs

class droid(intcode_machine):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.items = []
        self.items_col = []
        self.msg = ''
        self.dirs = []
        self.dir_history = deque([])
    
    def run_till_prompt(self):
        outp = []
        while True:
            try:
                halt, output = self.run_till_output_or_halt()
            except IndexError:
                break
            if halt:
                break
            outp.append(output)
            outp_str = ''.join(chr(x) for x in outp)
        dirs = [dir for dir in ['north', 'west', 'east', 'south'] if dir in outp_str]
        try:
            items = [x.split('- ')[1] for x in outp_str.split('Items here:')[1].split('\n') if '- ' in x]
        except IndexError:
            items = None
        
        return outp_str, dirs, items
    
    def initialize(self):
        outp, dirs, items = self.run_till_prompt()
        self.msg = outp
        self.dirs = dirs
        self.items = items
    
    def move(self, dir):
        coord = {'north': 1j, 'south': -1j, 'east': 1, 'west': -1}
        self.add_inputs(list(map(ord, dir + '\n')))
        outp, dirs, items = self.run_till_prompt()
        self.msg = outp
        self.dirs = dirs
        self.items = items
        self.dir_history.append(dir)
        
    def clone(self):
        clone = droid([])
        clone.i = self.i
        clone.l = defaultdict(int, self.l.items())
        clone.relbase = self.relbase
        clone.items = self.items
        clone.dirs = self.dirs
        clone.msg = self.msg
        clone.items_col = list(self.items_col)
        clone.dir_history = deque(self.dir_history)
        return clone
    
    def take(self, item):
        if item not in self.items:
            print('Item not available')
        else:
            self.add_inputs(list(map(ord, f'take {item}\n')))
            outp, dirs, items = self.run_till_prompt()
            self.items_col.append(item)
            self.items = items
            self.msg = outp
    
    def drop(self, item):
        if item not in self.items_col:
            print('Item not in your possession')
        else:
            self.add_inputs(list(map(ord, f'drop {item}\n')))
            outp, dirs, items = self.run_till_prompt()
            self.items_col.remove(item)
            self.items = items
            self.msg = outp
        