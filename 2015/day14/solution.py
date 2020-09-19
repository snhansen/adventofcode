with open('input') as f:
    inp = [x.strip() for x in f.readlines()]

ls = []
for x in inp:
    ls.append((int(x.split(' ')[3]), int(x.split(' ')[6]), int(x.split(' ')[13])))

def get_length(speed, duration, pause, secs):
    n = secs // (duration + pause)
    rem = secs % (duration + pause)
    return(n*duration*speed + min(rem, duration)*speed)

# Part 1
time = 2503
print(max([get_length(l[0], l[1], l[2], time) for l in ls]))

# Part 2
points = [0]*len(ls)
for t in range(time):
    lead = [get_length(l[0], l[1], l[2], t+1) for l in ls]
    winners = [i for i in range(len(lead)) if lead[i] == max(lead)]
    for i in winners:
        points[i] += 1

print(max(points))
