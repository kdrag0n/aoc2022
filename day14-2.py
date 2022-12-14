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

gr={}
mx,my=-1000,-1000
while True:
    for l in file_lines:
        pts=l.split(' -> ')
        _pts=[]
        for pt in pts:
            x,y = map(int, pt.split(','))
            if x > mx:
                mx = x
            if y > my:
                my = y
            _pts.append((x,y))
        # iterate pairs
        for i in range(len(_pts)-1):
            x1,y1 = _pts[i]
            x2,y2 = _pts[i+1]
            # draw line
            if x1 == x2:
                # vertical
                for y in range(min(y1,y2), max(y1,y2)+1):
                    gr[(x1,y)] = '#'
            else:
                # horizontal
                for x in range(min(x1,x2), max(x1,x2)+1):
                    gr[(x,y1)] = '#'

    break

sp=(500,0)
sc=0
steps=0
ylim=my+2
while True:
    x,y = sp
    # if (y > my and x > mx) or (steps > 10000000):
    #     break
    steps+=1
    down_y = y+1
    if (x,down_y) not in gr and down_y < ylim:
        sp=(x,down_y)
        continue
    else:
        # down, left
        if (x-1,down_y) not in gr and down_y < ylim:
            sp=(x-1,down_y)
            continue
        elif (x+1,down_y) not in gr and down_y < ylim:
            sp=(x+1,down_y)
            continue
        else:
            # blocked
            if sp == (500,0):
                break
            gr[sp] = 'o'
            sc+=1
            sp=(500,0)
#print(sum(1 for k,v in gr.items() if v == 'o' else 0))
print(sc+1)
print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')
