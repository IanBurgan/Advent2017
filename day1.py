#!/usr/bin/env python3

myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()

part_one = 0
part_two = 0

for i in range(len(contents) - 1):
    if contents[i] == contents[i + 1]:
        part_one += int(contents[i])

if contents[-1] == contents[0]:
    part_one += int(contents[-1])

for i in range(len(contents)):
    if contents[i] == contents[int(i + len(contents) / 2) % len(contents)]:
        part_two += int(contents[i])


print(part_one)
print(part_two)
