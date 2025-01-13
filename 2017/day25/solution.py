from collections import defaultdict

blueprint = {}
blueprint["A"] = {0: (1, 1, "B"), 1: (0, -1, "E")}
blueprint["B"] = {0: (1, -1, "C"), 1: (0, 1, "A")}
blueprint["C"] = {0: (1, -1, "D"), 1: (0, 1, "C")}
blueprint["D"] = {0: (1, -1, "E"), 1: (0, -1, "F")}
blueprint["E"] = {0: (1, -1, "A"), 1: (1, -1, "C")}
blueprint["F"] = {0: (1, -1, "E"), 1: (1, 1, "A")}

tape = defaultdict(int)
cursor = 0
state = "A"

for i in range(12208951):
    value = tape[cursor]
    write, move, state = blueprint[state][value]
    tape[cursor] = write
    cursor += move

print(sum(tape.values()))