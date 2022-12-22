#!/usr/bin/env python3

import sys

def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], 'r') as f:
    file_lines = [l for l in f.read().split('\n\n')]
pos=(0,0)
grid={}
for y,l in enumerate(file_lines[0].split('\n')):
    if y==0:
        pos=(l.index('.'),y)
    for x,c in enumerate(l):
        if c=='#':
            grid[(x,y)]='#'
        elif c=='.':
            grid[(x,y)]='.'
SIZE=4
graph={
    1: [2, 6, 4, 3],
    2: [1, 3, 5, 6],
    3: [1, 4, 5, 2],
    4: [1, 6, 5, 3],
    5: [4, 6, 2, 3],
    6: [4, 1, 2, 5]
}
#minx maxx miny maxy
bounds = {
    1: (8, 12, 0, 4),
    2: (0, 4, 4, 8),
    3: (4, 8, 4, 8),
    4: (8, 12, 4, 8),
    5: (8, 12, 8, 12),
    6: (12, 16, 8, 12),
}
# 0: up
# 1: right
# 2: down
# 3: left
dirs=[(0,-1),(1,0),(0,1),(-1,0)]
dir=1
dirmarks=['^','>','v','<']
marks={}
def print_grid(pos):
    return
    gr=[[' ']*40 for i in range(40)]
    for x,y in grid:
        gr[y][x]=grid[(x,y)]
    for x,y in marks:
        gr[y][x]=marks[(x,y)]
    if pos:
        gr[pos[1]][pos[0]]='X'
    for l in gr:
        print(''.join(l))
path=file_lines[1].strip()
print_grid(None)
face=1
while path:
    print('rem path',path)
        # extract leading int
    i=0
    while i<len(path) and path[i].isdigit():
        i+=1
    n=int(path[:i])
    path=path[i:]
    print('move',n)
    
    for i in range(n):
        # move
        cx,cy=pos
        dx,dy=dirs[dir]
        npos=(pos[0]+dx,pos[1]+dy)
        nx,ny=npos
        if npos not in grid:
            wrapto=graph[face][dir]
            dirfrom=graph[wrapto].index(face)
            newdir=(dirfrom+2)%4

            # wrap
            if dx!=0:
                minx=100000
                maxx=-100000
                for x,y in grid:
                    if y==cy:
                        minx=min(minx,x)
                        maxx=max(maxx,x)
                refdx=nx-minx
                refdx %= maxx-minx+1
                npos=(minx+refdx,ny)
                nx=minx+refdx
            elif dy!=0:
                minx=100000
                maxx=-100000
                for x,y in grid:
                    if x==cx:
                        minx=min(minx,y)
                        maxx=max(maxx,y)
                refdy=ny-minx
                refdy %= maxx-minx+1
                npos=(nx,minx+refdy)
                ny=minx+refdy
        print('test',npos,grid[npos])
        if grid[npos]=='.':
            pass
        elif grid[npos]=='#':
            break
        marks[npos]=dirmarks[dir]
        print_grid(npos)
        pos=npos

    # turn
    if path:
        print('turn',path[0])
        if path[0]=='R':
            # 90 deg clockwise
            dir=(dir+1)%4
        elif path[0]=='L':
            # 90 deg counterclockwise
            dir=(dir-1)%4
        path=path[1:]

x,y=pos
print('row',y+1)
print('col',x+1)
print('facing',dir,'translate',(dir-1)%4)
print(4*(x+1)+1000*(y+1)+(dir-1)%4)
