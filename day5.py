#!/usr/bin/env python3

myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
contents = contents.split()
contents = [int(x) for x in contents]
# True to solve part two
part_two = False

steps = 0
place = 0
while place < len(contents) and place > -1:
    steps += 1
    old = place
    jump = contents[place]
    place += jump

    if part_two:
        if jump > 2:
            contents[old] -= 1
        else:
            contents[old] += 1
    else:
        contents[old] += 1

print("Solution:", steps)
