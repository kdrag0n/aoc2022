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

gr=set()
while True:
    for l in file_lines:
        x,y,z=l.split(',')
        x,y,z=ints([x,y,z])
        gr.add((x,y,z))

    break

dsides=[(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]
for x,y,z in gr:
    con=0
    for dx,dy,dz in dsides:
        if (x+dx,y+dy,z+dz) in gr:
            total-=1
    total+=

print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')
