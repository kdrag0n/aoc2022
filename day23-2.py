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

grid=set()
while True:
    for y,row in enumerate(file_lines[::-1]):
        for x,c in enumerate(row):
            if c=='#':
                grid.add((x,y))

    break

dirs=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
dir_names=['N','S','E','W','NE','SE','NW','SW']
rules=[
    ('N','NE','NW'),
    ('S','SE','SW'),
    ('W','NW','SW'),
    ('E','NE','SE'),
]
import collections
rs=1
while True:
    moves=[]
    targets=collections.defaultdict(lambda: 0)
    for x,y in grid:
        n=0
        for dx,dy in dirs:
            if (x+dx,y+dy) in grid:
                n+=1
        if not n:
            continue
        for rule in rules:
            n=0
            for dir in rule:
                dx,dy=dirs[dir_names.index(dir)]
                if (x+dx,y+dy) not in grid:
                    n+=1
            if n==3:
                dx,dy=dirs[dir_names.index(rule[0])]
                moves.append((x,y,x+dx,y+dy))
                targets[(x+dx,y+dy)] +=1
                break
    for x,y,tx,ty in moves:
        if targets[(tx,ty)]!=1:
            continue
        grid.remove((x,y))
        grid.add((tx,ty))
    frule=rules[0]
    rules = rules[1:]+[frule]
    if not moves:
        break
    rs+=1
print('f',rs)
exit(1)
minx,miny,maxx,maxy=0,0,0,0
for x,y in grid:
    minx=min(minx,x)
    miny=min(miny,y)
    maxx=max(maxx,x)
    maxy=max(maxy,y)
for y in range(miny,maxy+1):
    for x in range(minx,maxx+1):
        if (x,y) in grid:
            print('#',end='')
        else:
            total+=1
            print('.',end='')
    print()
print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')
