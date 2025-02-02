# Call the six registers for a, b, c, d, e, f, which
# all hold the value 0. Per our input, the instruction 
# pointer is bound to register f.
#
# After instruction 0, we're sent to instruction 17.
# Then instructions 17 through 25 is carried out leaving
# register d with the value 1025 (11*19*2^2 + 22*8 + 13).
# The other registers doesn't matter for now.
#
# Instruction 25 would increment f by a, but since a 
# in Part 1 is 0, this does nothing, and we continue to
# instruction 26 which resets f to 0 and send us to 
# instruction 1.
#
# Instructions 1 through 16 does the following:
# It loops over b = 1, .., d and c = 1, .., d
# and checks whether d = b*d. If that's the case
# then a is incremented by b (instruction 7).
# Once the loop is over we end at instruction 16
# which send us out of bounds (since f is squared)
# and halts the program.
#
# For Part 2, register a begins with a value of 1
# and so instruction 26 is skipped. After carrying
# out instructions 28 through 34, register d is left
# with the value 10551425 ((27*28+29)*30*14*32 + 1025).


def factors(n):
    return [x for x in range(1, n + 1) if n % x == 0]


# Part 1
print(sum(factors(1025)))

# Part 2
print(sum(factors(10551425)))