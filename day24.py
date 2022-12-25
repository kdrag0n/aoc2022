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

gr=[]
blzs=[]
snapshots={}
dirs={
    'up':(0,-1),
    'down':(0,1),
    'left':(-1,0),
    'right':(1,0),
    'wait':(0,0),
}
while True:
    for y,row in enumerate(file_lines):
        gr+=[list(row)]
        for x,c in enumerate(row):
            if c=='^':
                blzs+=[(x,y,'up')]
            elif c=='v':
                blzs+=[(x,y,'down')]
            elif c=='<':
                blzs+=[(x,y,'left')]
            elif c=='>':
                blzs+=[(x,y,'right')]

    break

minx=1
maxx=len(gr[0])-2
miny=1
maxy=len(gr)-2
newgr={}
for x in range(minx,maxx+1):
    for y in range(miny,maxy+1):
        newgr[(x,y)]=gr[y][x]
snapshots[0]=newgr
for t in range(1,3000):
    for i,(x,y,dir) in enumerate(blzs):
        dx,dy=dirs[dir]
        nx,ny=x+dx,y+dy
        if nx<minx or nx>maxx or ny<miny or ny>maxy:
            # wrap around
            if nx<minx:
                nx=maxx
            elif nx>maxx:
                nx=minx
            if ny<miny:
                ny=maxy
            elif ny>maxy:
                ny=miny
        #newblzs+=[(nx,ny,dir)]
        blzs[i]=(nx,ny,dir)
    # newgr={}
    # for x in range(minx,maxx+1):
    #     for y in range(miny,maxy+1):
    #         newgr[(x,y)]='.'
    # for x,y,dir in newblzs:
    #     newgr[(x,y)]='x'
    # snapshots[t]=newgr
    # blzs=newblzs
    newset=set()
    for x,y,dir in blzs:
        newset.add((x,y))
    snapshots[t]=newset
#rint(snapshots)
#print(gr)
# for snap in snapshots.values():
#     ng=[[snap[(x,y)] for x in range(minx,maxx+1)] for y in range(miny,maxy+1)]
#     for row in ng:
#         print(''.join(row))
#     print()
endy=len(gr)-1
endx=gr[-1].index('.')
startx=gr[0].index('.')
starty=0
print('start',startx,starty)
print('end',endx,endy)
print('min',minx,miny)
print('max',maxx,maxy)
def srch(t,x,y):
    minr=10000
    #print(x,y)
    if t+1>len(snapshots):
        return minr
    if x==endx and y==endy:
        print('et',t)
        return t
    for dir in dirs:
        dx,dy=dirs[dir]
        nx,ny=x+dx,y+dy
        #print(f'[{t}] test',nx,ny,dir)
        if (nx,ny) == (endx,endy) or (nx,ny) == (startx,starty) or (nx >= minx and nx <= maxx and ny >= miny and ny <= maxy):
            #print('pass')
            #print('sn',snapshots[t])
            #print('looj',snapshots[t][(nx,ny)])
            if (nx,ny) not in snapshots[t]:
                minr=min(minr,srch(t+1,nx,ny))
    nx,ny=x,y
    #print(f'[{t}] test',nx,ny,'wait')
    minr=min(minr,srch(t+1,nx,ny))
    return minr
import heapq
def sbfs():
    #states=[(0,startx,starty)]
    # states=set()
    states=set()
    nstates=set()
    #heapq.heappush(states,(0,startx,starty))
    states.add((0,startx,starty))
    t=0
    snapshot=set()
    while states:
        # t+=1
        # if t%10==0:
        #     print(t, len(states))
        # # if t+1>len(snapshots):
        #     # break
        # for i,(x,y,dir) in enumerate(blzs):
        #     dx,dy=dirs[dir]
        #     nx,ny=x+dx,y+dy
        #     if nx<minx or nx>maxx or ny<miny or ny>maxy:
        #         # wrap around
        #         if nx<minx:
        #             nx=maxx
        #         elif nx>maxx:
        #             nx=minx
        #         if ny<miny:
        #             ny=maxy
        #         elif ny>maxy:
        #             ny=miny
        #     #newblzs+=[(nx,ny,dir)]
        #     blzs[i]=(nx,ny,dir)
        # newgr={}
        # for x in range(minx,maxx+1):
        #     for y in range(miny,maxy+1):
        #         newgr[(x,y)]='.'
        # for x,y,dir in newblzs:
        #     newgr[(x,y)]='x'
        # snapshots[t]=newgr
        # blzs=newblzs
        # newset=set()
        # for x,y,dir in blzs:
        #     newset.add((x,y))
        # snapshot=newset

        #nstates=set()
        # for _,x,y in states:
        #t,x,y=heapq.heappop(states)
        t,x,y=states.pop()
        #t,x,y=heapq.heappop(states)
        if x==endx and y==endy:
            return t
        for dir in dirs:
            dx,dy=dirs[dir]
            nx,ny=x+dx,y+dy
            if (nx,ny) == (endx,endy) or (nx >= minx and nx <= maxx and ny >= miny and ny <= maxy):
                if (nx,ny) not in snapshots[t]:
                    #nstates+=[(t+1,nx,ny)]
                    states.add((t+1,nx,ny))
                    # heapq.heappush(states,(t+1,nx,ny))
        #states=nstates
#print(srch(0,startx,starty))
print(sbfs())

print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')
