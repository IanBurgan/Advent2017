#!/usr/bin/env python3

step = 354
buff = [0]
pos = 0

for i in range(1, 2018):
    move = step % len(buff)
    pos = (pos + move) % len(buff) + 1
    buff.insert(pos, i)

print("Part One:", buff[buff.index(2017) + 1])

buff = [0]
buff_len = 1
ans = 1
i = 0
while i < 50000000:
    i += 1
    move = step % buff_len
    pos = (pos + move) % buff_len + 1
    if (pos == 1):
        ans = i
    buff_len += 1

print("Part Two:", ans)
