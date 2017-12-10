#!/usr/bin/env python3

myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()

lengths_one = contents.split(',')
lengths_one = [int(x) for x in lengths_one]

lengths_two = [ord(x) for x in contents] + [17, 31, 73, 47, 23]

def hash_one(lengths):
    rope = list(range(256))
    pos = 0
    skip = 0

    for num in lengths:
        if pos + num <= len(rope):
            begin = rope[:pos]
            middle = rope[pos:pos + num]
            end = rope[pos + num:]
            rope = begin + middle[::-1] + end
        else:
            begin = rope[:(pos + num) % len(rope)]
            middle = rope[(pos + num) % len(rope):pos]
            end = rope[pos:]
            count = len(end)
            sel = end + begin
            sel = sel[::-1]
            rope = sel[count:] + middle + sel[:count]

        pos += (num + skip)
        pos = pos % len(rope)
        skip += 1
    return rope

def hash_two(lengths):
    rope = list(range(256))
    pos = 0
    skip = 0

    for i in range(64):
        for length in lengths:
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

result_one = hash_one(lengths_one)
part_one = result_one[0] * result_one[1]
part_two = hash_two(lengths_two)

print("Part One:", part_one)
print("Part Two:", part_two)
