#!/usr/bin/env python3

myfile = open('input.txt', 'r')
rules = myfile.readlines()
myfile.close()

class Rule:
    @classmethod
    def rotate(cls, grid):
        rows = reversed(grid.split('/'))
        return '/'.join(''.join(x) for x in zip(*rows))

    @classmethod
    def reflect(cls, grid):
        rows = grid.split('/')
        return '/'.join(x[::-1] for x in rows)

    def __init__(self, text):
        [before, after] = text.split(' => ')
        self.output_grid = after

        self.valid_grids = []
        self.valid_grids.append(before)
        self.valid_grids.append(Rule.reflect(before))

        # create the three rotations, 90, 180, 270
        # and their reflections
        curr_grid = before
        for _ in range(3):
            rotated = Rule.rotate(curr_grid)
            self.valid_grids.append(rotated)
            self.valid_grids.append(Rule.reflect(rotated))
            curr_grid = rotated

    def is_applicable(self, grid):
        return grid in self.valid_grids

def enhance_grid(grid, rules):
    def chunk(item, length):
        return [item[i:i + length] for i in range(0, len(item), length)]

    rows = grid.split('/')
    step = 2 if len(rows) % 2 == 0 else 3

    chunked_rows = [chunk(row, step) for row in rows]
    sub_grids = chunk(chunked_rows, step)
    sub_grids = ['/'.join(x) for y in sub_grids for x in zip(*y)]

    new_grid = []
    for g in sub_grids:
        for r in rules:
            if r.is_applicable(g):
                new_grid.append(r.output_grid.split('/'))
                break
        else:
            raise Exception('Sub grid not found in rules: ' + str(g))

    width = int(len(new_grid) ** 0.5)

    new_grid = chunk(new_grid, width)
    return '/'.join([''.join(x) for y in new_grid for x in zip(*y)])

rules = [Rule(r.strip()) for r in rules]
grid = '.#./..#/###'
for i in range(18):
    grid = enhance_grid(grid, rules)

print(grid.count('#'))
