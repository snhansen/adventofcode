from collections import defaultdict
from itertools import count

with open("input") as f:
    inp = f.read().strip().split("\n")


def rotate(s):
    n = int(len(s.replace("/", "")) ** 0.5)
    ls = [s[i*n:(i+1)*n] for i in range(n)]
    res = []
    for j in range(n):
        res.append("".join(ls[n-1-i][j] for i in range(n)))
    return "".join(res)


def flip(s):
    n = int(len(s.replace("/", "")) ** 0.5)
    ls = [s[i*n:(i+1)*n] for i in range(n)]
    res = []
    for j in range(n):
        res.append("".join(ls[n-1-j][i] for i in range(n)))
    return "".join(res)


def versions(s):
    res = set()
    for _ in range(4):
        res.add(s)
        res.add(flip(s))
        s = rotate(s)
    return res


def print_(s):
    n = int(len(s.replace("/", "")) ** 0.5)
    ls = [s[i*n:(i+1)*n] for i in range(n)]
    for line in ls:
        print(line)


rules = {}
for line in inp:
    left, right = line.split(" => ")
    for pattern in versions(left.replace("/", "")):
        rules[pattern] = right.replace("/", "")


def disassemble(s, size):
    n = int(len(s) ** 0.5)
    assert n % size == 0
    chunks = [s[i*size:(i+1)*size] for i in range(len(s) // size)]
    k = n // size
    squares = []
    for i in range(k):
        subchunks = chunks[i*k*size: (i+1)*k*size]
        for j in range(k):
            res = ""
            for m in range(size):
                res += subchunks[j + m*k]
            squares.append(res)
    return squares


def assemble(ls):
    size = int(len(ls[0]) ** 0.5)
    n = int((len(ls[0])*len(ls)) ** 0.5)
    k = n // size
    s = ""
    for i in range(k):
        squares = ls[i*k: (i+1)*k]
        for m in range(size):
            for j in range(k):
                s += squares[j][m*size:(m+1)*size]
    return s
        

def process(s):
    n = int(len(s) ** 0.5)
    if n % 2 == 0:
        squares = disassemble(s, 2)
    elif n % 3 == 0:
        squares = disassemble(s, 3)
    new_squares = [rules[square] for square in squares]
    s = assemble(new_squares)
    return s


s = ".#...####"
for t in count():
    s = process(s)
    if t in [4, 17]:
        print(s.count("#"))
    if t == 17:
        break