#!/usr/bin/env python3

myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
contents = contents.split(',')

order = 'abcdefghijklmnop'

def spin(amount):
    loc = -1 * amount
    return order[loc:] + order[:loc]

def exchange(a, b):
    copy = [x for x in order]
    temp = copy[a]
    copy[a] = copy[b]
    copy[b] = temp
    return ''.join(copy)

def partner(a, b):
    copy = order.replace(a, '$')
    copy = copy.replace(b, a)
    return copy.replace('$', b)

# cycle length is 25
for j in range(24):
    for i in contents:
        if i[0] == 's':
            order = spin(int(i.strip('s')))
        if i[0] == 'x':
            a, b = i.strip('x').split('/')
            order = exchange(int(a), int(b))
        if i[0] == 'p':
            a, b = i[1:].split('/')
            order = partner(a, b)

    if j == 0:
        print("Part One:", order)
    elif j == 15: # cycle length is 24, 15 is the same as 1 billion
        print("Part Two:", order)
