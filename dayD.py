#!/usr/bin/env python3

myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip().split('\n')
walls = [x.split(': ') for x in contents]

total = []
for depth, range in walls:
    depth = int(depth)
    range = int(range)

    cycle = 2 * (range - 1)
    if depth % cycle == 0:
        total.append(depth * range)

print("Part One:", sum(total))

found = False
delay = 0

while not found:
    delay += 1
    for depth, range in walls:
        depth = int(depth)
        range = int(range)

        cycle = 2 * (range - 1)
        found = True
        if (depth + delay) % cycle == 0:
            found = False
            break

    if found:
        print("Part Two:", delay)
