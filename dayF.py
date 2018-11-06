#!/usr/bin/env python3

start_a = 883
start_b = 879

def next_num(prev, mult):
    return (prev * mult) % 2147483647

def next_a(prev):
    return next_num(prev, 16807)

def next_b(prev):
    return next_num(prev, 48271)

def part_one():
    prev_a = start_a
    prev_b = start_b
    total = 0
    for i in range(40 * 1000 * 1000):
        prev_a = next_a(prev_a)
        prev_b = next_b(prev_b)

        result = prev_a ^ prev_b

        if result & 4294901760 == result:
            total += 1

    return total

print("Part One:", part_one())

def part_two():
    prev_a = start_a
    prev_b = start_b
    total = 0
    for i in range(5 * 1000 * 1000):
        prev_a = next_a(prev_a)
        while prev_a % 4 != 0:
            prev_a = next_a(prev_a)

        prev_b = next_b(prev_b)
        while prev_b % 8 != 0:
            prev_b = next_b(prev_b)

        result = prev_a ^ prev_b

        if result & 4294901760 == result:
            total += 1
    return total

print("Part Two:", part_two())
