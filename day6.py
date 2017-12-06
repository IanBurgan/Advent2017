#!/usr/bin/env python3

myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
contents = contents.split()
contents = [int(x) for x in contents]

states = set([])
first_seen = {}
part_one = 0

while True:
    state = ' '.join(str(x) for x in contents)

    if state not in states:
        states.add(state)
        first_seen[state] = part_one
    else:
        part_two = part_one - first_seen[state]
        break

    blocks = max(contents)
    ind = contents.index(blocks)

    contents[ind] = 0
    ind += 1

    while blocks > 0:
        contents[ind % len(contents)] += 1
        blocks -= 1
        ind += 1

    part_one += 1

print("Part One:", part_one)
print("Part Two:", part_two)
