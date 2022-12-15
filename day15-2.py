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
global_xmin, global_xmax = 0, 0
global_ymin, global_ymax = 0, 0
for d,sx,sy,bx,by in sensors:
    r =d
    ymin, ymax = sy - r, sy + r
    xmin, xmax = sx - r, sx + r
    if xmin < global_xmin:
        global_xmin = xmin
    if xmax > global_xmax:
        global_xmax = xmax
    if ymin < global_ymin:
        global_ymin = ymin
    if ymax > global_ymax:
        global_ymax = ymax
# limits
LIM = 4000000
#LIM=20
if global_xmin < -LIM:
    global_xmin = -LIM
if global_xmax > LIM:
    global_xmax = LIM
if global_ymin < -LIM:
    global_ymin = -LIM
if global_ymax > LIM:
    global_ymax = LIM
global_xmin = max(global_xmin, 0)
global_ymin = max(global_ymin, 0)
global_xmax = min(global_xmax, LIM)
global_ymax = min(global_ymax, LIM)
for y in range(LIM+1):
    if not (y >= global_ymin and y <= global_ymax):
        continue
    ranges=[]
    #row=[0]*(LIM+1)
    #print(f'start_y({y});')
    for d,sx,sy,bx,by in sensors:
        r =d
        ymin, ymax = sy - r, sy + r
        if y >= ymin and y <= ymax:
            # find x at this y level
            dy = abs(y - sy)
            xmin, xmax = sx - (r - dy), sx + (r - dy)
            #for x in range(xmin, xmax+1):
            #print(f'fill_x({max(xmin, global_xmin)}, {min(xmax, global_xmax)+1});')
            #for x in range(max(xmin, global_xmin), min(xmax, global_xmax)+1):
                #row[x] = 1
            ranges.append((max(xmin, global_xmin), min(xmax, global_xmax)))
    b = []
    for begin,end in sorted(ranges):
        if b and b[-1][1] >= begin - 1:
            b[-1][1] = max(b[-1][1], end)
        else:
            b.append([begin, end])
    unions = b
    if y % 10000 == 0:
        print(y,'=',len(unions))
    #if len(unions)>1:
        # find hole
    if len(unions)==2:
        end1,begin2 = unions[0][1],unions[1][0]
        x = end1+1
        print(x,y,'=', x*4000000+y)
        exit()
    #print(f'[{y}]  ' + ''.join(['#' if x else '.' for x in row]))
    #print(y)
    # for x in range(global_xmin, global_xmax+1):
    #     if not row[x]:
    #         print(x,y,'=', x*4000000+y)
    #         exit()

print(sum(row.values()))
print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')
