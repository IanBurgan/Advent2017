#!/usr/bin/env python3

myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
contents = contents.split('\n')
contents = [x.split() for x in contents]

part_one = 0
part_two = 0
for i in contents:
    if len(set(i)) == len(i):
        part_one += 1

    n = []
    for j in i:
        m = sorted(j)
        n.append(''.join(m))
    if len(set(n)) == len(n):
        part_two += 1

print("Part One:", part_one)
print("Part Two:", part_two)
