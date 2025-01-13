from itertools import count

with open("input") as f:
    inp = f.read().strip().split(",")


def spin(programs, n):
    return programs[-n:] + programs[:(len(programs)-n)]


def exchange(programs, index1, index2):
    programs[index1], programs[index2] = programs[index2], programs[index1]
    return programs


def partner(programs, prg1, prg2):
    index1, index2 = programs.index(prg1), programs.index(prg2)
    return exchange(programs, index1, index2)


def dance(programs):
    new_programs = list(programs)
    for line in inp:
        op = line[0]
        rest = line[1:]
        match op:
            case "s":
                new_programs = spin(new_programs, int(rest))
            case "x":
                index1, index2 = map(int, rest.split("/"))
                new_programs = exchange(new_programs, index1, index2)
            case "p":
                prg1, prg2 = rest.split("/")
                new_programs = partner(new_programs, prg1, prg2)
    return new_programs

# Part 1
programs = list(map(chr, range(97, 113)))
print("".join(dance(programs)))

# Part 2
programs_start = list(programs)
for step in count():
    programs = dance(programs)
    if programs == programs_start:
        cycle = step + 1
        break

remainder = 1000000000 % cycle
programs = list(programs_start)
for step in range(remainder):
    programs = dance(programs)

print("".join(programs))