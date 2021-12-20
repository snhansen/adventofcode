from collections import defaultdict

algo, input = open('input').read().strip().split('\n\n')
input = input.split('\n')

image = defaultdict(int)
for i, row in enumerate(input):
    for j, s in enumerate(row):
        image[j+i*1j] = int(s == '#')
            

def update_img(d):
    pmin, *_, pmax = d
    xmin, xmax, ymin, ymax  = map(int, (pmin.real, pmax.real, pmin.imag, pmax.imag))
    new_d = defaultdict(lambda: int(algo[511] == '#')) if d[(-1) + (ymin-1)*1j] else defaultdict(lambda: int(algo[0] == '#'))
    for i in range(ymin-2, ymax+3):
        for j in range(xmin-2, xmax+3):
            p = j + i*1j
            bin = ''
            for dp in [-1-1j, -1j, -1j+1, -1, 0, 1, -1+1j, 1j, 1+1j]:
                bin += str(image[p+dp])
            new_d[p] = int(algo[int(bin, 2)] == '#')
        
    return new_d


# Part 1 and 2
for i in range(50):
    image = update_img(image)
    if i in [1, 49]:
        print(sum(image.values()))