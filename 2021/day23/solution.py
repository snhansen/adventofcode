from heapq import heappop, heappush
from collections import defaultdict, deque
from functools import reduce


with open('input') as f:
    inp = f.readlines()

pods_start = []
for r, line in enumerate(inp):
    line = line.strip('\n')
    for c, x in enumerate(line):
        if x.isalpha():
            pods_start.append((c+r*1j, x))

pods_start.sort(key = lambda x: x[1]) # Make sure pods are in order A-D.
pods_start = tuple([p for p, _ in pods_start])
hallway = [c+1*1j for c in range(1,12)]
dirs = [-1, 1, -1j, 1j]
energies = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}


# Checks if the pod is in its final destination.
def is_in_place(pods, i): 
    p = pods[i]
    type = get_type[i]
    if p not in home[type]:
        return False
    k = 1
    while True:
        if p+k*1j not in home[type]:
            break
        if p+k*1j in pods and get_type[pods.index(p+k*1j)] != type:
            return False
        k += 1
    return True


# Checks if the home of the pod is clear (not occupied by other pod-types).
def is_home_clear(pods, i):
    p = pods[i]
    type = get_type[i]
    res = list(home[type])
    for j, p2 in enumerate(pods):
        type2 = get_type[j]
        for q in home[type]:
            if p2 == q and type2 != type:
                return None
            if p2 == q:
                res.remove(q)
    return res[-1]


# Returns a list of possible destination places.
def get_destinations(pods, i):
    p = pods[i]
    type = get_type[i]
    dest = is_home_clear(pods, i)
    if dest:
        res = set()
        Q = deque([p])
        while Q:
            q = Q.popleft()
            for new_q in (set([q+dq for dq in dirs]) & (set(hallway + rooms))) - set(pods):
                if new_q == dest:
                    return [dest]
                if new_q not in res:
                    res.add(new_q)
                    Q.append(new_q)
    
    if p in hallway:
        return []
    
    else:
        res = set()
        Q = deque([p])
        while Q:            
            q = Q.popleft()
            for new_q in (set([q+dq for dq in dirs]) & (set(hallway + rooms))) - set(pods):
                if new_q not in res:
                    res.add(new_q)
                    Q.append(new_q)
        return list((res & set(hallway)) - invalid)


# Returns the number of steps needed to go from p1 to p2.
def dist(p1, p2):
    if p1.imag == 1 or p2.imag == 1:
        return int(abs(p1.real-p2.real) + abs(p1.imag-p2.imag))
    else:
        return dist((p1.real+1j), p1) + dist((p1.real+1j), p2)


# Sorts the pods within each type (to avoid a lot of duplicates in the Dijkstra algorithm).
def sort_pods(pods, k):
    res = []
    for i in range(4):
        res += sorted(pods[i*k: i*k + k], key = lambda x: (x.real, x.imag))
    return res



def solve(pods_start, part2 = False):
    global get_type
    global home
    global rooms
    global invalid
    k = len(pods_start) // 4
    home = {}
    for i, type in enumerate('ABCD'):
        home[type] = [3+i*2+(j+2)*1j for j in range(k)]
    
    rooms = reduce(lambda x,y: x+y, home.values())
    invalid = set([p for p in hallway if any(p+dp in rooms for dp in dirs)])
    get_type = 'A'*k + 'B'*k + 'C'*k + 'D'*k
    to_check = []
    to_check.append((0, id(pods_start), pods_start))
    costs = defaultdict(lambda: float('inf'))
    while to_check:
        energy, _, pods = heappop(to_check)  
        if all(p in home[get_type[i]] for i, p in enumerate(pods)):
            return energy
        for i, p in enumerate(pods):
            if is_in_place(pods, i):
                continue
            dests = get_destinations(pods, i)
            type = get_type[i]
            if dests:
                for dest in dests:
                    new_pods = list(pods)
                    new_pods[i] = dest
                    new_pods = sort_pods(new_pods, k)
                    new_pods = tuple(new_pods)
                    steps = dist(dest, p)
                    new_energy = energy+steps*energies[type]
                    if new_energy < costs[new_pods]:
                        heappush(to_check, (new_energy, id(new_pods), new_pods))
                        costs[new_pods] = new_energy


# Part 1
print(solve(pods_start))


# Part 2
temp = []
for i, p in enumerate(pods_start):
    if p.imag == 3:
        temp.append((p+2*1j, get_type[i]))
    else:
        temp.append((p, get_type[i]))

temp += [(3+3*1j, 'D'), (3+4*1j, 'D'), (5+3*1j, 'C'), (5+4*1j, 'B'), (7+3*1j, 'B'), (7+4*1j, 'A'), (9+3*1j, 'A'), (9+4*1j, 'C')]
pods_start = temp
pods_start.sort(key = lambda x: x[1])
pods_start = tuple([p for p, _ in pods_start])

print(solve(pods_start, True))