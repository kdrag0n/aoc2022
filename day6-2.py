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
        for i, ch in enumerate(l):
            if i < 13: continue
            # get leading 14 chars
            chs = l[i-13:i+1]
            print('chs', chs)
            if sorted(list(set(chs))) == sorted(list(chs)):
                print(i+1)
                break
    break



print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')
