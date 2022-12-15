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

sensors=[]
while True:
    for l in file_lines:
        p1,p2 = l.replace('Sensor at ', '').replace('closest beacon is at ', '').replace('x=','').replace('y=','').split(': ')
        sx,sy = ints(p1.split(','))
        bx,by = ints(p2.split(','))
        dist = abs(sx-bx) + abs(sy-by)
        sensors.append((dist, sx, sy, bx, by))

    break


y=2000000
#y=10
row={}
for d,sx,sy,bx,by in sensors:
    r =d
    ymin, ymax = sy - r, sy + r
    if y >= ymin and y <= ymax:
        # find x at this y level
        dy = abs(y - sy)
        xmin, xmax = sx - (r - dy), sx + (r - dy)
        for x in range(xmin, xmax+1):
            if not (x == bx and y == by):
                row[x] = 1

print(sum(row.values()))
print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')
