#!/usr/bin/env python3
import re

myfile = open('input.txt', 'r')
contents = myfile.read().strip().splitlines()
myfile.close()

# manually search for part 1 answer, it will be one of the indexes
# print([i for i, vals in enumerate(contents) if 'a=<0,0,0>' in vals])

# part two
def reformat(line):
    return '|'.join(re.findall(r'<(.*?)>', line))

def update(p_string):
    vals = p_string.split('|')
    positions = [int(i) for i in vals[0].split(',')]
    velocities = [int(i) for i in vals[1].split(',')]
    accelerations = [int(i) for i in vals[2].split(',')]

    velocities = list(map(sum, zip(velocities, accelerations)))
    positions = map(sum, zip(positions, velocities))

    pos = ','.join(map(str, positions))
    vel = ','.join(map(str, velocities))
    acc = ','.join(map(str, accelerations))

    return '|'.join([pos, vel, acc])

def get_position(p_string):
    return p_string.split('|')[0]


# reformat strings and add to set
particles = [reformat(line) for line in contents]

for i in range(100):
    survivors = {}
    for i, p in enumerate(particles):
        updated = update(p)
        pos = get_position(updated)
        if pos not in survivors:
            survivors[pos] = [updated]
        else:
            survivors[pos].append(updated)

    particles = []
    for value in survivors.values():
        # if there is only one particle at a position
        if len(value) == 1:
            # add the single particle back into the population
            particles.extend(value)

print(len(particles))
