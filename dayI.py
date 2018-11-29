#!/usr/bin/env python3
from collections import defaultdict

myfile = open('input.txt', 'r')
contents = myfile.read().strip().split('\n')
myfile.close()

reg = defaultdict(int)

def get(val):
    try:
        return int(val)
    except:
        return reg[val]

def part_one():
    recent_sound = None
    pc = 0
    while True:
        args = contents[pc].split()
        if (len(args) > 2):
            op, addr, val = args
        else:
             op, addr = args

        if op == 'snd':
            recent_sound = regs[addr]
        elif op == 'set':
            regs[addr] = get(val)
        elif op == 'add':
            regs[addr] += get(val)
        elif op == 'mul':
            regs[addr] *= get(val)
        elif op == 'mod':
            regs[addr] %= get(val)
        elif op == 'rcv':
            if get(val) != 0:
                print('Part One:', recent_sound)
                break
        elif op == 'jgz':
            if get(addr) > 0:
                pc += get(val)
                continue

        pc += 1

def part_two():
    total = 0
    pr = 0
    regs = [defaultdict(int), defaultdict(int)]
    regs[1]['p'] = 1

    def get2(val):
        try:
            return int(val)
        except:
            return regs[pr][val]

    pc = [0, 0]
    data = [[], []]
    deadlock = False
    while True:
        args = contents[pc[pr]].split()
        if (len(args) > 2):
            op, addr, val = args
        else:
             op, addr = args

        if op == 'snd':
            deadlock = False
            if pr == 1:
                total += 1
            data[1 - pr].append(get2(addr))
        elif op == 'set':
            regs[pr][addr] = get2(val)
        elif op == 'add':
            regs[pr][addr] += get2(val)
        elif op == 'mul':
            regs[pr][addr] *= get2(val)
        elif op == 'mod':
            regs[pr][addr] %= get2(val)
        elif op == 'rcv':
            if len(data[pr]) > 0:
                regs[pr][addr] = data[pr].pop(0)
            else:
                if deadlock:
                    break

                pr = 1 - pr
                deadlock = True
                continue # avoid increment

        elif op == 'jgz':
            if get2(addr) > 0:
                pc[pr] += get2(val) - 1

        pc[pr] += 1

    print("Part Two: ", total)

part_two()
