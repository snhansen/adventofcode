with open('input') as f:
    inp = [x.strip() for x in f.readlines()]

def light_rect(c, r, screen):
    for i in range(c):
        for j in range(r):
            screen[i+1j*j] = 1
    return screen

def rotate_col(c, v, screen):
    new_screen = dict(screen)
    for j in range(n_row):
        new_screen[c+1j*((j+v) % n_row)] = screen[c+1j*j]
    return new_screen

def rotate_row(r, v, screen):
    new_screen = dict(screen)
    for i in range(n_col):
        new_screen[((i+v) % n_col)+1j*r] = screen[i+1j*r]
    return new_screen

def print_screen(s):
    dict = {1: chr(0x2588), 0: ' '}
    for j in range(n_row):
        print(''.join([dict[screen[i+1j*j]] for i in range(n_col)]))

# Part 1
n_col, n_row = 50, 6
screen = {}
for i in range(n_col):
    for j in range(n_row):
        screen[i+1j*j] = 0
        
for x in inp:
    if 'rect' in x:
        screen = light_rect(int(x.split(' ')[1].split('x')[0]), int(x.split(' ')[1].split('x')[1]), screen)
    elif 'row' in x:
        screen = rotate_row(int(x.split(' ')[2].split('=')[1]), int(x.split(' ')[4]), screen)
    elif 'col' in x:
        screen = rotate_col(int(x.split(' ')[2].split('=')[1]), int(x.split(' ')[4]), screen)

print(sum(screen.values()))

# Part 2
print_screen(screen)