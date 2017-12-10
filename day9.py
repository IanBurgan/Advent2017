#!/usr/bin/env python3

import re

myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
contents = re.sub('!.', '', contents)

garbage = re.findall('<([^>]*)>', contents)
part_two = sum(len(x) for x in garbage)

contents = re.sub('<[^>]*>', '', contents)

level = 0
part_one = 0

for i in contents:
    if i == '{':
        level += 1
    elif i == '}':
        part_one += level
        level -= 1

print("Part One:", part_one)
print("Part Two:", part_two)
