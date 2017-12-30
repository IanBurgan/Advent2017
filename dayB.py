#!/usr/bin/env python3

myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
contents = contents.split(',')

def calc_dist(x, y):
    return max(abs(x), abs(y), abs(x + y))

x, y = 0, 0
dist = 0

for i in contents:
    if i == 'n':
        y -= 1
    elif i == 's':
        y += 1
    elif i == 'nw':
        x -= 1
    elif i == 'ne':
        x += 1
        y -= 1
    elif i == 'sw':
        x -= 1
        y += 1
    elif i == 'se':
        x += 1

    dist = max(dist, calc_dist(x, y))

print("Part One:", calc_dist(x, y))
print("Part Two:", dist)
