#!/usr/bin/env python3
import string

myfile = open('input.txt', 'r')
contents = myfile.read().splitlines()
myfile.close()

letters = []

# start at the entrance
row = 0
col = contents[row].find('|')
bearing = 'S' # start by traveling south

curr = contents[row][col]
count = 0
while curr != ' ':
    if bearing == 'N':
        row -= 1
    elif bearing == 'E':
        col += 1
    elif bearing == 'S':
        row += 1
    elif bearing == 'W':
        col -= 1

    curr = contents[row][col]
    if curr == '+':
        if bearing in ('N', 'S'):
            if contents[row][col + 1] == '-':
                bearing = 'E'
            else:
                bearing = 'W'
        else:
            if contents[row - 1][col] == '|':
                bearing = 'N'
            else:
                bearing = 'S'
    elif curr not in ('|', '-'):
        letters.append(curr)

    count += 1

print("Part One:", ''.join(letters))
print("Part Two:", count)
