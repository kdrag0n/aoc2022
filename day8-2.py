#!/usr/bin/env python3

import sys

def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], 'r') as f:
    file_lines = [l for l in f.read().strip().split('\n')]


in_nums = []

total = 0
result = 0
other = 0

grid = []
while True:
    for l in file_lines:
        grid += [list(map(int, l))]

    break
import copy
g2 = copy.deepcopy(grid)
scores = []
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        cur_h = cell
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        vis = False
        sc = 1
        for dx, dy in dirs:
            i = 0
            x2, y2 = x, y
            print('  check dir', dx, dy)
            blocked = False
            while True:
                x2 += dx
                y2 += dy
                if x2 < 0 or y2 < 0 or x2 >= len(row) or y2 >= len(grid):
                    break
                i += 1
                print('    check cell', x2, y2, grid[y2][x2])
                if grid[y2][x2] >= cur_h:
                    print('      blocked')
                    blocked = True
                    break
            #if not blocked:
            sc *= i
        scores += [sc]
        print(x, y, cell, vis)
        if vis:
            total += 1
            g2[y][x] = 'X'

print('\n'.join([''.join([str(c) for c in r]) for r in g2]))
print(max(scores))

print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')
