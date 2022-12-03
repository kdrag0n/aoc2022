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
    for i in range(0, len(file_lines), 3):
        l1 = file_lines[i]
        l2 = file_lines[i+1]
        l3 = file_lines[i+2]
        common = list(set(l1).intersection(set(l2)).intersection(set(l3)))[0]
        # a-z -> 1-26
        if common in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            result += ord(common) - ord('A') + 1 + 26
            print('common', common,  ord(common) - ord('A') + 1)
        else:
            result += ord(common) - ord('a') + 1
            print('common', common,  ord(common) - ord('a') + 1 + 26)

        if False:
            total += 1

    break



print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')
