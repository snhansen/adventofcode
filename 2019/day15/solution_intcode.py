import sys
import os
import math
sys.path.insert(1, os.path.dirname(os.getcwd()))
from aoc_functions import maze_robot


with open('input') as f:
    inp = list(map(int, f.read().split(',')))


d = {1: 1j, 2: -1j, 3: -1, 4: 1}


# Part 1.1 (BFS)
def find_shortest_path(pos, robot):
    shortest_path = math.inf
    for dir in [i+1 for i in range(4) if robot.pos + d[i+1] not in robot.visited]:
        clone = robot.clone()
        status = clone.move(dir)
        if status == 2:
            print(pos + d[dir])
            return 1
        elif status == 1:
            shortest_path = min(find_shortest_path(pos + d[dir], clone), shortest_path)
    return shortest_path + 1


robot = maze_robot(inp, [])
print(find_shortest_path(0, robot))


# Part 1.2 (BFS)
def clone(robots):
    new_robots = []
    for robot in robots:
        for dir in [i+1 for i in range(4) if robot.pos + d[i+1] not in robot.visited]:
            clone = robot.clone()
            status = clone.move(dir)
            if status:
                new_robots.append(clone)
    return new_robots


robot = maze_robot(inp, [])
robots = [robot]

coords = []

while True:
    for robot in robots:
        coords.append(robot.pos)
        if robot.status == 2:
            oxy_robot = robot
            break
    robots = clone(robots)
    if robot.status == 2:
        break

print(oxy_robot.pos)
print(len(oxy_robot.dirs))

# Part 2
oxy_pos = oxy_robot.pos
oxy_robot.visited = [oxy_pos]

robots = [oxy_robot]
time = 0
while True:
    robots = clone(robots)
    if not robots:
        break
    time += 1

print(time)
