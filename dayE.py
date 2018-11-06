#!/usr/bin/env python3

def knot_hash(lengths):
    rope = list(range(256))
    pos = 0
    skip = 0

    for i in range(64):
        for length in lengths + [17, 31, 73, 47, 23]:
            if pos + length <= len(rope):
                begin = rope[:pos]
                middle = rope[pos:pos + length]
                end = rope[pos + length:]
                rope = begin + middle[::-1] + end
            else:
                begin = rope[:(pos + length) % len(rope)]
                middle = rope[(pos + length) % len(rope):pos]
                end = rope[pos:]
                count = len(end)
                sel = end + begin
                sel = sel[::-1]
                rope = sel[count:] + middle + sel[:count]

            pos = (pos + length + skip) % len(rope)
            skip += 1

    dense = ''
    for i in range(0,256,16):
        nums = rope[i:i + 16]
        result = int(eval(' ^ '.join([str(x) for x  in nums])))
        dense += "{:02x}".format(result)

    return dense

def key_to_list(key):
    return [ord(x) for x in key]

def to_bin_hash(s):
    return ''.join([bin(int(x, 16))[2:].zfill(4) for x in s])

def part_one():
    key = "stpzcrnm-"
    total = 0
    for i in range(128):
        k = key + str(i)
        l = key_to_list(k)
        h = knot_hash(l)
        b = to_bin_hash(h)
        total += sum(int(x) for x in b)

    return total

print("Part One:", part_one())

def part_two():
    # open the 128x128 grid as text input
    # the grid can be output by part one
    myfile = open('input.txt', 'r')
    contents = myfile.read()
    myfile.close()

    contents = contents.split()

    visited = set()
    regions = 0

    for row in range(len(contents)):
        for col in range(len(contents[row])):
            if contents[row][col] == '1' and (row, col) not in visited:
                regions += 1

                # bfs over the region
                region = set()
                q = [(row, col)]

                while q:
                    curr = q.pop()
                    if curr not in region:
                        region.add(curr)

                        r, c = curr

                        if r > 0 and contents[r - 1][c] == '1':
                            q.append((r - 1, c))

                        if r < 127 and contents[r + 1][c] == '1':
                            q.append((r + 1, c))

                        if c > 0 and contents[r][c - 1] == '1':
                            q.append((r, c - 1))

                        if c < 127 and contents[r][c + 1] == '1':
                            q.append((r, c + 1))
                # add region to the visited set
                visited.update(region)

    print(regions)

part_two()
