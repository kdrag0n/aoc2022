#!/usr/bin/env python3

import sys

def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], 'r') as f:
    _map, dirs=f.read().split('\n\n')
    file_lines = [l for l in f.read().split('\n')]


in_nums = []

total = 0
result = 0
other = 0

stacks = [None] * 9
for i in range(9):
    stacks[i] = []

while True:
    for l in _map.split('\n')[:-1]:
        for i in range(len(stacks)):
            ti = 1 + 4 * i
            print(l, i, ti)
            ch = l[ti]
            if ch.isalpha():
                stacks[i].insert(0, ch)

    print(stacks)
    for ins in dirs.split('\n'):
        if ins:
            _, count, _, frm, _, to = ins.split()
            count = int(count)
            frm = int(frm)
            to = int(to)
            print(count, frm, to)
            frm -= 1
            to -= 1
            stacks[to].extend(stacks[frm][-count:])
            stacks[frm] = stacks[frm][:-count]
            print(stacks)
    
    print(''.join(s[-1] for s in stacks))
    break



print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')
