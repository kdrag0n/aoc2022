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
        l1, l2 = l.split(',')
        start1, end1 = ints(l1.split('-'))
        start2, end2 = ints(l2.split('-'))
        # check if any overlap
        if start1 <= end2 and start2 <= end1:
            total += 1
        elif start2 <= end1 and start1 <= end2:
            total += 1

        if False:
            total += 1

    break



print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')
