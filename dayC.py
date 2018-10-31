#!/usr/bin/env python3

myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
contents = contents.split('\n')

links = {}

for line in contents:
    i = line.split(' <-> ')
    key, value = i[0], i[1].split(', ')

    links[key] = value

# bfs
def bfs(start):
    visited = set()
    q = [x for x in links[start]]

    while q:
        curr = q.pop(0)
        if curr not in visited:
            visited.add(curr)

            q.extend(links[curr])
    return visited

groups = []
visited = set()

first_group = bfs('0')
print("Part One:", len(first_group))

groups.append(first_group)
visited |= first_group

for num in links:
    if num not in visited:
        group = bfs(num)
        groups.append(group)
        visited |= group

print("Part Two:", len(groups))
