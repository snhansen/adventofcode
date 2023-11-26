row = 3010
col = 3019

# Part 1
def index(r, c):
    qr = 1 + r*(r-1)//2
    return qr + (c-1)*r+(c-1)*c//2

print(20151125*pow(252533, index(row, col)-1, 33554393) % 33554393)