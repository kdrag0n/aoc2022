#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np
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

xmin,xmax=1000,-1000
ymin,ymax=1000,-1000
zmin,zmax=1000,-1000
for x,y,z in gr:
    if x<xmin:
        xmin=x
    if x>xmax:
        xmax=x
    if y<ymin:
        ymin=y
    if y>ymax:
        ymax=y
    if z<zmin:
        zmin=z
    if z>zmax:
        zmax=z
print('x',xmin,xmax)
print('y',ymin,ymax)
print('z',zmin,zmax)
gr_inv=set()
# find the outline
outlines=set()
for z in range(zmin, zmax+1):
    for y in range(ymin, ymax+1):
        # from the left
        x=xmin-1
        while (x,y,z) not in gr and x>=xmin-1 and x<=xmax+1:
            print('chk', x,y,z)
            x+=1
        print('end', x,y,z)
        if (x,y,z) in gr:
            outlines.add((x,y,z))
        else:
            print('NOT FOUND')
            continue
        leftx = x
        # from the right
        x=xmax+1
        while (x,y,z) not in gr and x>=xmin-1 and x<=xmax+1:
            x-=1
        print('end', x,y,z)
        if (x,y,z) in gr:
            outlines.add((x,y,z))
        else:
            print('NOT FOUND')
            continue
        rightx = x
        print('left', leftx, 'right', rightx)
        # add the middle
        for x in range(leftx, rightx+1):
            print('  FILL IN', x, y,z)
            #gr.add((x,y,z))
            if (x,y,z) not in gr:
                gr_inv.add((x,y,z))
    for x in range(xmin, xmax+1):
        # from the top
        y=ymin-1
        while (x,y,z) not in gr and y>=ymin-1 and y<=ymax+1:
            y+=1
        if (x,y,z) in gr:
            outlines.add((x,y,z))
        else:
            print('NOT FOUND')
            continue
        topy = y
        # from the bottom
        y=ymax+1
        while (x,y,z) not in gr and y>=ymin-1 and y<=ymax+1:
            y-=1
        if (x,y,z) in gr:
            outlines.add((x,y,z))
        else:
            print('NOT FOUND')
            continue
        bottomy = y
        # add the middle
        for y in range(topy, bottomy+1):
            #gr.add((x,y,z))
            if (x,y,z) not in gr:
                gr_inv.add((x,y,z))
for x in range(xmin, xmax+1):
    for y in range(ymin, ymax+1):
        # from the front
        z=zmin-1
        while (x,y,z) not in gr and z>=zmin-1 and z<=zmax+1:
            z+=1
        if (x,y,z) in gr:
            outlines.add((x,y,z))
        else:
            print('NOT FOUND')
            continue
        frontz = z
        # from the back
        z=zmax+1
        while (x,y,z) not in gr and z>=zmin-1 and z<=zmax+1:
            z-=1
        if (x,y,z) in gr:
            outlines.add((x,y,z))
        else:
            print('NOT FOUND')
            continue
        backz = z
        # add the middle
        for z in range(frontz, backz+1):
            #gr.add((x,y,z))
            if (x,y,z) not in gr:
                gr_inv.add((x,y,z))
print(outlines)

print('outlines',len(outlines))
area1=0
dsides=[(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]
for x,y,z in gr:
    con=0
    for dx,dy,dz in dsides:
        if (x+dx,y+dy,z+dz) in gr:
            con+=1
    area1+=6-con

area2=0
dsides=[(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]
for x,y,z in gr_inv:
    con=0
    for dx,dy,dz in dsides:
        if (x+dx,y+dy,z+dz) in gr_inv:
            con+=1
    area2+=6-con
print(area1,area2)
print(area1-area2)

ax=plt.figure().add_subplot(projection='3d')
nfilled = np.zeros((xmax+1,ymax+1,zmax+1))
for x,y,z in outlines:
    nfilled[x,y,z]=1
ax.voxels(nfilled)
#plt.show()

# nfilled = np.zeros((xmax+1,ymax+1,zmax+1))
# for x,y,z in gr:
#     nfilled[x,y,z]=1
# ax=plt.figure().add_subplot(projection='3d')
# ax.voxels(nfilled)
# plt.show()

# plt.cla()
# ax=plt.figure().add_subplot(projection='3d')
# nfilled = np.zeros((xmax+1,ymax+1,zmax+1))
# for x,y,z in gr_inv:
#     nfilled[x,y,z]=1
# ax.voxels(nfilled)
# plt.show()
round=[(-1,-1,-1)]
gr_reached=set()
while True:
    nround=[]
    for x,y,z in round:
        for dx,dy,dz in dsides:
            if (x+dx,y+dy,z+dz) not in gr and x+dx >= xmin-1 and x+dx <= xmax+1 and y+dy >= ymin-1 and y+dy <= ymax+1 and z+dz >= zmin-1 and z+dz <= zmax+1 and (x+dx,y+dy,z+dz) not in gr_reached:
                nround.append((x+dx,y+dy,z+dz))
                gr_reached.add((x+dx,y+dy,z+dz))
    if len(nround)==0:
        break
    round = nround
gr_reached_inv = set()
for x in range(xmin-1, xmax+2):
    for y in range(ymin-1, ymax+2):
        for z in range(zmin-1, zmax+2):
            if (x,y,z) not in gr_reached:
                gr_reached_inv.add((x,y,z))
print('gr_reached', len(gr_reached))
ax=plt.figure().add_subplot(projection='3d')
nfilled = np.zeros((xmax+2,ymax+2,zmax+2))
for x,y,z in gr_reached:
    nfilled[x,y,z]=1
ax.voxels(nfilled)
plt.show()
area1=0
dsides=[(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]
for x,y,z in gr_reached_inv:
    con=0
    for dx,dy,dz in dsides:
        if (x+dx,y+dy,z+dz) in gr_reached_inv:
            con+=1
    area1+=6-con
print('AR', area1)
print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')
