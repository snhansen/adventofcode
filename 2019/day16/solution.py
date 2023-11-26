import numpy as np
import math

with open('input') as f:
    inp = list(map(int, f.read().strip()))


# Part 1
k = len(inp)
m = np.ones((k, k))
for i in range(k):
    m[i] = np.tile(np.repeat([0, 1, 0, -1], i+1), math.ceil((len(inp)+1)/(4*(i+1))))[1:k+1]


def get_output(x):
    return abs(x) % 10


output = inp
for _ in range(100):
    output = np.apply_along_axis(get_output, 0, np.matmul(m, output))

print(''.join(str(int(x)) for x in output[0:8]))


# Part 2
offset = int(''.join(str(x) for x in inp[0:7]))
signal = list(map(int, inp))
print(f'offset is in latter half of input: {offset > len(signal)*5000}')
signal = np.tile(signal, 10000)[offset:]


def run(inp):
    outp = []
    outp.append(inp[-1])
    for i in range(1, len(inp)):
        outp.append(outp[-1] + inp[len(inp)-i-1])
    outp = list(map(lambda x: abs(x) % 10, outp))
    outp.reverse()
    return outp


for _ in range(100):
    signal = run(signal)

print(''.join(str(int(x)) for x in signal[0:8]))
