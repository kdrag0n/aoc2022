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

gr = []
pos = (0,0)
tgt = (0,0)
while True:
    for y,l in enumerate(file_lines):
        r=[]
        for x,c in enumerate(l):
            el = 0
            if c == 'S': el = 0
            elif c == 'E': el = 25
            else: el = ord(c) - ord('a')
            if c == 'S': pos=(x,y)
            if c == 'E': tgt=(x,y)
            r+=[el]
        gr+=[r]


    break
nodes=[]
for y,row in enumerate(gr):
    for x,el in enumerate(row):
        node = (x, y, el)
        if (x, y ) == pos:
            start_node = node
        if (x, y ) == tgt:
            end_node = node
        gr[y][x] = node
        nodes+=[node]
import collections
graph = collections.defaultdict(list)
for y,row in enumerate(gr):
    for x,node in enumerate(row):
        n_ds = [(0,1), (0,-1), (1,0), (-1,0)]
        for dx,dy in n_ds:
            try:
                neigh = gr[y+dy][x+dx]
                nx, ny, nel = neigh
                graph[node] += [neigh]
            except:
                pass

# paths=[]
# def dfs(node, len, visited=[]):
#     global paths
#     if node == end_node:
#         paths+=[len]
#         return len
#     visited = visited + [node]
#     for n in graph[node]:
#         if n[2] <= node[2]+1 and n not in visited:
#             # paths+=[dfs(n, len+1)]n
#             if not paths or len+1 < min(paths):
#                 dfs(n, len+1, visited)
# dfs(start_node, 1)
# print(min(paths))

from heapq import *
def dijkstra(start_node):
    heap=[]
    dist = {n: 2147483647 for n in nodes}
    dist[start_node] = 0
    heappush(heap, (0, start_node))
    while heap:
        d, node = heappop(heap)
        if d > dist[node]:
            continue
        for neigh in graph[node]:
            if neigh[2] <= node[2]+1:
                if dist[neigh] > dist[node] + 1:
                    dist[neigh] = dist[node] + 1
                    heappush(heap, (dist[neigh], neigh))
    return dist[end_node]


ps=[]
for n in nodes:
    if n[2] == 0:
        ps+=[dijkstra(n)]
print(min(ps))
print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')
