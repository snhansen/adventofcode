import numpy as np

inp = np.genfromtxt('input', delimiter = 1, dtype = 'int')
colsum = np.sum(inp, axis = 0)
n_rows = np.shape(inp)[0]

# Part 1
most_common = [int(x) for x in colsum >= (n_rows / 2)]
gamma = ''.join(str(x) for x in most_common)
epsilon = ''.join('1' if x == '0' else '0' for x in gamma)
print(int(gamma,2)*int(epsilon,2))

# Part 2
j = 0
numbers = inp
while(np.shape(numbers)[0] > 1):
    most_common = int(sum(numbers[:,j]) >= (np.shape(numbers)[0] / 2))
    numbers = numbers[numbers[:, j] == most_common]
    j += 1

oxygen = ''.join(str(x) for x in numbers[0,:])

j = 0
numbers = inp
while(np.shape(numbers)[0] > 1):
    most_common = int(sum(numbers[:,j]) < (np.shape(numbers)[0] / 2))
    numbers = numbers[numbers[:, j] == most_common]
    j += 1

co2 = ''.join(str(x) for x in numbers[0,:])

print(int(oxygen, 2)*int(co2, 2))