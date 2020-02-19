with open('input') as f:
    inp = f.read().split('\n')

w1 = inp[0].split(',')
w2 = inp[1].split(',')

def coords(w):
    coords = [[0, 0]]
    for i, c in enumerate(w):
        direction = c[0]
        steps = int(c[1:])
        if direction == 'R':
            xsteps = steps
            ysteps = 0
        elif direction == 'L':
            xsteps = -steps
            ysteps = 0
        elif direction == 'D':
            xsteps = 0
            ysteps = steps
        elif direction == 'U':
            xsteps = 0
            ysteps = -steps
        coords.append([coords[i][0] + xsteps, coords[i][1] + ysteps])
    return coords

def linescross(c1, c2):
    x1 = c1[0][0]
    y1 = c1[0][1]
    x2 = c1[1][0]
    y2 = c1[1][1]
    x3 = c2[0][0]
    y3 = c2[0][1]
    x4 = c2[1][0]
    y4 = c2[1][1]
    denom = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
    if denom != 0:
        px = ( (x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4) ) / ( (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4) ) 
        py = ( (x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4) ) / ( (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4) )
    if denom != 0 and min(x1, x2) <= px <= max(x1, x2) and min(x3, x4) <= px <= max(x3, x4) and min(y1, y2) <= py <= max(y1, y2) and min(y3, y4) <= py <= max(y3, y4):
        return [int(px), int(py)]
    else:
        return None
    
def getintersections(w1, w2):
    intersects = []
    positions = []
    for i in range(len(w1) - 1):
        for j in range(len(w2) - 1):
            temp = linescross([w1[i], w1[i+1]], [w2[j], w2[j+1]])
            if temp and not (temp[0] == 0 and temp[1] == 0):
                intersects.append(temp)
                positions.append([i, j])
    return intersects, positions

def manhattan(p1, p2 = [0,0]):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) 

# Part 1
w1_coords = coords(w1)
w2_coords = coords(w2) 
intersections, positions = getintersections(w1_coords, w2_coords)
print(min(list(map(manhattan, intersections))))


# Part 2
def distance(w1, w2, p, index):
    dist = 0
    for i in range(index[0]):
        dist += manhattan(w1[i], w1[i+1])
    for i in range(index[1]):
        dist += manhattan(w2[i], w2[i+1])
    dist += manhattan(p, w1[index[0]]) + manhattan(p, w2[index[1]])
    return dist


distances = []
for intersect, pos in zip(intersections, positions):
    distances.append(distance(w1_coords, w2_coords, intersect, pos))

print(min(distances))
