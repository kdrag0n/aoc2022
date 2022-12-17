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
rocks='''####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##'''.split('\n\n')
rocks=[[list(s) for s in r.split('\n')[::-1]] for r in rocks]

grid=[['.']*7 for i in range(25000)]
maxy=len(grid)
ptn=list(file_lines[0])
fell=0
j=0
import copy
last_height=0
for i in range(5000):
    rk=rocks[i%len(rocks)]
    w=len(rk[0])
    h=len(rk)
    x0=2
    y0=maxy-4
    done=False
    #if i%1000==0:
        #print('rock',i)
        #print(i+1,len(grid)-maxy)
    def printg():
        return
        gridc = copy.deepcopy(grid)
        for cy,row in enumerate(rk):
            for cx,ch in enumerate(row):
                if ch!='.' and gridc[y0-cy][x0+cx] == '.':
                    gridc[y0-cy][x0+cx]=ch
        print('  '+'\n  '.join(''.join(r) for r in gridc))
    while True:
        printg()
        dir=ptn[j%len(ptn)]
        old_x0=x0
        x0 += 1 if dir=='>' else -1
        # if dir=='>':
        #     print('right')
        # else:
        #     print('left')
        j+=1
        done2=False
        for cy,row in enumerate(rk):
            for cx,ch in enumerate(row):
                #print(x0+cx,y0-cy)
                if ch!='.' and (x0+cx < 0 or x0+cx >= 7 or grid[y0-cy][x0+cx] != '.' ):
                    # collided
                    #print('x collide')
                    done2=True
                    break
            if done2: break
        if done2:
            x0 = old_x0
        printg()

        #print('fall')
        y0+=1
        for cy,row in enumerate(rk):
            for cx,ch in enumerate(row):
                #print(x0+cx,y0-cy)
                if ch!='.' and (y0-cy < 0 or y0-cy>=len(grid) or grid[y0-cy][x0+cx] != '.' ):
                    # collided
                    #print('y collide')
                    fell+=1
                    y0-=1
                    done=True
                    break
            if done: break
        if done: break
        printg()
        #print('[loop]')
    if done:
        # dir=ptn[j]
        # old_x0=x0
        # x0 += 1 if dir=='>' else -1
        # if dir=='>':
        #     print('right')
        # else:
        #     print('left')
        # j+=1
        # done2=False
        # for cy,row in enumerate(rk):
        #     for cx,ch in enumerate(row):
        #         print(x0+cx,y0-cy)
        #         if ch!='.' and (x0+cx < 0 or x0+cx >= 7 or grid[y0-cy][x0+cx] != '.' ):
        #             # collided
        #             print('x collide')
        #             done2=True
        #             break
        #     if done2: break
        # if done2:
        #     x0 = old_x0
        for cy,row in enumerate(rk):
            for cx,ch in enumerate(row):
                if ch!='.' and grid[y0-cy][x0+cx] == '.':
                     grid[y0-cy][x0+cx]=ch
        for y,row in enumerate(grid[::-1]):
            if '#' in row:
                maxy=len(grid)-1-y
    #print('\n'.join(''.join(r) for r in grid))
    height=len(grid)-maxy
    print(f'{i+1},{len(grid)-maxy}')#  d={height-last_height}')
    last_height=height
exit()
print('ans')
#print(maxy)
print(len(grid)-maxy)
#print(len(grid)-(maxy-1))

print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')
