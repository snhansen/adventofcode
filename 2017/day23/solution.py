from collections import defaultdict

with open("input") as f:
    inp = f.read().strip().split("\n")

instr = [line.split(" ") for line in inp]
regs = defaultdict(int)

# Part 1
p, c = 0, 0
while p < len(instr):
    op, x, y = instr[p]
    y = int(y) if y.lstrip("-").isnumeric() else regs[y]
    if op == "set":
        regs[x] = y
    elif op == "sub":
        regs[x] -= y
    elif op == "mul":
        c += 1
        regs[x] *= y
    elif op =="jnz":
        x = int(x) if x.lstrip("-").isnumeric() else regs[x]
        if x != 0:
            p += y
            continue
    p += 1

print(c)

# Part 2

# We initiate register a = 1. The program begins with these instructions:

	# set b 99
	# set c b
	# jnz a 2
	# jnz 1 5
	# mul b 100
	# sub b -100000
	# set c b
	# sub c -17000

# which sets registers b = 109900 and c = 126900.

# Then we run the following instructions:

	# set f 1
	# set d 2
	# set e 2
	# set g d
	# mul g e
	# sub g b
	# jnz g 2
	# set f 0
	# sub e -1
	# set g e
	# sub g b
	# jnz g -8
	# sub d -1
	# set g d
	# sub g b
	# jnz g -13

# At the beginning f is set to 1. Then we go through a loop 
# where d and e both loops from 2 to b. For each combination
# of d and e, we check if b = d*e and set f = 0 if that is the case.
# That is, f = 1 if b is a prime number and f = 0 otherwise.

# The following:

	# jnz f 2
	# sub h -1

# will increment h by 1 if f was not a prime number.

# The remaining instructions
	
	# set g b
	# sub g c
	# jnz g 2
	# jnz 1 3
	# sub b -17
	# jnz 1 -23

# does the following: If b = c we hit "jnz 1 3" and exit the program.
# Otherwise we increment b by 17.

def prime(n):
    return not any(n % i == 0 for i in range(2, n))

b = 100000 + 99*100
c = b + 17000

print(sum(not prime(n) for n in range(b, c + 1, 17)))