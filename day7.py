#!/usr/bin/env python3

import re

myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
contents = contents.split('\n')

programs = set()
top_levels = set()
node_map = {}
weights = {}
for line in contents:
    towers = line.replace(',','').split()
    name = towers[0]
    weight = re.sub('[\(\)]', '', towers[1])
    weights[name] = int(weight)
    programs.add(name)
    held = towers[3:]

    if held:
        node_map[name] = held

    for x in held:
        top_levels.add(x)

programs -= top_levels
root = programs.pop()

def search(node):
    holding = node_map[node]
    weights_held = []

    for i in holding:
        weight = 0
        if i in node_map.keys():
            weight = sum(search(i))
        weight += weights[i]

        weights_held.append(weight)

    if len(set(weights_held)) != 1:
        print(node, holding, weights_held)
    return weights_held

print("Part One:", root)
search(root)

# input specific code, determined by output of search
# bad node is in first line of output by search
# print(weights['ltleg'] - (1792 - 1786))
