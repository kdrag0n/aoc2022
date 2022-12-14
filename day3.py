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

while True:
    for l in file_lines:
        # half of line
        l1 = l[:len(l)//2]
        # other half of line
        l2 = l[len(l)//2:]

        common = list(set(l1).intersection(set(l2)))[0]
        # a-z -> 1-26
        if common in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            result += ord(common) - 64 + 26
            print('common', common,  ord(common) - 64)
        else:
            result += ord(common) - 96
            print('common', common,  ord(common) - 96 + 26)

        if False:
            total += 1

    break



print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')
