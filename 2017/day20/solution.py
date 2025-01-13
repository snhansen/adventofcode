import re
from copy import deepcopy

with open("input") as f:
    inp = f.read().strip().split("\n")

particles_init = []
for line in inp:
    nums = list(map(int, re.findall("-?\d+", line)))
    particles_init.append([nums[0:3], nums[3:6], nums[6:9]])


def update(particles):
    particles = deepcopy(particles)
    for particle in particles:
        pos, vel, acc = particle
        for i in range(len(vel)):
            vel[i] += acc[i]
            pos[i] += vel[i]
        particle[0] = pos
        particle[1] = vel
    return particles


def closest(particles):
    id_ = None
    min_dist = float("inf")
    for i, particle in enumerate(particles):
        pos, _, _ = particle
        d = sum(map(abs, pos))
        if d < min_dist:
            min_dist = d
            id_ = i
    return id_

# Part 1
# We experiment with the number of frames needed to
# to find the closest particle. 500 frames is enough.
particles = particles_init
for _ in range(500):
    particles = update(particles)

print(closest(particles))

# Part 2
# We experiment with the number of frames needed to
# to detect all collisions. 50 frames is enough.
def remove_collisions(particles):
    new_particles = []
    for i in range(len(particles)):
        add = True
        for j in range(len(particles)):
            if i == j:
                continue
            if particles[i][0] == particles[j][0]:
                add = False
                break
        if add:
            new_particles.append(particles[i])
    return new_particles


particles = particles_init
for _ in range(50):
    particles = update(particles)
    particles = remove_collisions(particles)

print(len(particles))