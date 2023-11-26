with open('input') as f:
    img = f.read().strip('\n')

w = 25
h = 6
s = len(img)
layers = [img[i:i+w*h] for i in range(0, s, w*h)]

# Part 1
layer = min(layers, key=lambda x: x.count('0'))     
print(layer.count('1')*layer.count('2'))

# Part 2
result = ''
for i in range(w*h):
    j = 0
    while True:
        if int(layers[j][i]) == 1:
            result += 'x'
            break
        elif int(layers[j][i]) == 0:
            result += ' '
            break
        j += 1

for i in range(0, w*h, w):
    print(result[i:i+w])