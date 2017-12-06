#!/usr/bin/env python3

myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
contents = contents.split('\n')
contents = [x.split() for x in contents]

part_one = 0
part_two = 0

for row in contents:
    row_int = list(map(int, row))
    part_one += max(row_int) - min(row_int)

    for i in range(len(row)):
        for j in range(len(row)):
            if j != i:
                if row_int[i] % row_int[j] == 0:
                    part_two += int(row_int[i] / row_int[j])

print("Part One:", part_one)
print("Part Two:", part_two)
