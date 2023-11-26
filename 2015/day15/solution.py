with open('input') as f:
    inp = [x.strip() for x in f.readlines()]

prop = []  
for x in inp:
    prop.append((int(x.split(' ')[2].strip(',')), int(x.split(' ')[4].strip(',')), int(x.split(' ')[6].strip(',')), int(x.split(' ')[8].strip(',')), int(x.split(' ')[10])))

def score(ls):
    cap = sum([ls[i]*prop[i][0] for i in range(len(prop))])
    dur = sum([ls[i]*prop[i][1] for i in range(len(prop))])
    fla = sum([ls[i]*prop[i][2] for i in range(len(prop))])
    tex = sum([ls[i]*prop[i][3] for i in range(len(prop))])
    cal = sum([ls[i]*prop[i][4] for i in range(len(prop))])
    if cap <= 0 or dur <= 0 or fla <= 0 or tex <= 0:
        return 0, cal
    return cap*dur*fla*tex, cal

# Part 1
max_score = -float('inf')
for i in range(101):
    for j in range(101):
        for k in range(101):
            for l in range(101):
                if i+j+k+l == 100:
                    s, _ = score([i, j, k, l])
                    max_score = max(max_score, s)

print(max_score)

# Part 2
max_score = -float('inf')
for i in range(101):
    for j in range(101):
        for k in range(101):
            for l in range(101):
                if i+j+k+l == 100:
                    s, c = score([i, j, k, l])
                    if c == 500:
                        max_score = max(max_score, s)

print(max_score)
