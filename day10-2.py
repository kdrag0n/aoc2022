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

time = 1
reg = 1
grid = [['.' for i in range(40)] for j in range(6)]
cpos = 0
def check():
    global total
    global cpos
    if time == 20 or time == 60 or time == 100 or time == 140 or time == 180 or time == 220:
        print(time, reg, time*reg)
        total+= time*reg
    x, y = cpos % 40, cpos // 40
    if x >= reg-1 and x <= reg+1:
        grid[y][x] = '#'
    cpos += 1
    print('cyc %d, reg %d, pos %d, %d' % (time, reg, x, y))
    print('\n'.join([''.join(l) for l in grid]))
while True:
    for l in file_lines:
        parts = l.split()
        ins = parts[0]
        if ins == 'noop':
            check()
            time+=1
            continue
        elif ins == 'addx':
            arg = int(parts[1])
            check()
            time+=1
            check()
            time+=1
            reg += arg

        if False:
            total += 1
    check()

    break


print('\n'.join([''.join(l) for l in grid]))
print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')
