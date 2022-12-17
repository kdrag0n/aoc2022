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

rates={}
graph={}
nodes=[]
while True:
    for l in file_lines:
        _, v, _, _, r = l.replace('rate=','').replace(';','').split()[:5]
        edges = ' '.join(l.replace('rate=','').split()[9:]).split(', ')
        r = int(r)
        rates[v] = r
        graph[v] = edges
        nodes+=[v]

        if False:
            total += 1

    break
print(graph)
print(rates)

# from heapq import *
# T_MIN = 30
# def dijkstra(start_node):
#     heap=[]
#     dist = {n: 2147483647 for n in nodes}
#     dist[start_node] = 0
#     heappush(heap, (0, start_node, 1))
#     while heap:
#         d, node, mins = heappop(heap)
#         if d > dist[node]:
#             continue
#         for neigh in graph[node]:
#             neigh_dist =2147483647-(dist[node] + rates[neigh] * (T_MIN-mins))
#             if dist[neigh] > neigh_dist and mins+1 <= T_MIN:
#                 dist[neigh] = neigh_dist
#                 heappush(heap, (dist[neigh], neigh, mins+1))
#     return dist

# dists=dijkstra('AA')
# print(dists)
# print(min(dists.items(), key=lambda x: x[1]))
# print(max(dists.items(), key=lambda x: x[1]))

def dfs(node, path, visited=[],paths=[]):
    paths=[]
    visited = visited + [node]
    for n in graph[node]:
        if visited.count(n) <2:
            paths += [path+[n]]
            paths += dfs(n, path+[n], visited, paths)
    return paths
paths=dfs('AA', ['AA'])
paths=[['AA', 'DD', 'CC', 'BB', 'AA', 'II', 'JJ', 'II', 'AA', 'DD', 'EE', 'FF', 'GG', 'HH', 'GG', 'FF', 'EE', 'DD', 'CC']]
for path in paths:
    prs=0
    open=[]
    # min=1
    # for i, n in enumerate(path):
    #     prs += sum([rates[n] for n in open])
    #     min+=1
    #     if n not in open:
    #         open+=[n]
    #         min+=1
    # for _ in range(0,30-min+1):
    #     prs += sum([rates[n] for n in open])
    p=path[1:]
    min=1
    i=0
    cur = 'AA'
    while min<=30:
        print('min', min)
        print('open', open, 'prs', sum([rates[n] for n in open]))
        prs += sum([rates[n] for n in open])
        if i<len(p):
            cur = p[i]
            print(' MOVE to', cur)
            i+=1
        if cur not in open and rates[cur] > 0:
            min+=1
            prs += sum([rates[n] for n in open])
            print('min', min)
            print('open', open, 'prs', sum([rates[n] for n in open]))
            print(' OPEN ', cur)
            open+=[cur]
        min+=1
        print()
    print(path, prs)
    if prs>result:
        result=prs
        best_path=path
#print(paths)
def dfss(node, path, visited=[],paths=[]):
    paths=[]
    visited = visited + [node]
    for n in graph[node]:
        if visited.count(n) <2:
            paths += [path+[n]]
            paths += dfss(n, path+[n], visited, paths)
    return paths

# TODO: 3D DP https://www.reddit.com/r/adventofcode/comments/zn6k1l/comment/j0ffm47/?utm_source=reddit&utm_medium=web2x&context=3 https://topaz.github.io/paste/#XQAAAQCiDgAAAAAAAAARmknGRw8TogC0aCl9/9FDQbu7KtZE5SXTHaQ0I7zvS2kodZfssACpiw799FqPhI92cDZHBED3ycU9bYQD78PS9PcG3juurjQJbnw0Rxftoau+K7xjvy1rDawLPeLlFblRs+bj+k59ewe3HxLGwPbIaDa1FgmWTsukJPEMTMzHONIFs777a8zeu3woYvv4OwakDzVugbPC/0uH0bNhIHR6weJl7QKwsvlkYAQ6xnpOemljPNg+BJHpmXPmFYqSgn8n0CdvvWJVGHzYvnfaqBTkWpvIzpgU3bVMrVVzhidKY8qBJoUhsLcF79JmMRrEpUeMoM4FSWKE3koylUuCOo++cCZbtsooCkj+AKzXXRj2RQxLCk2D6MFtvSs71ucb0umBXf4ai0MZkPir0VSIuDsnkWgWszr3m7Lr8bOIFl40B/kg08Kp2INNBQtyO7E7A3OI+Nk8slg68usA7QWx6qBJRk/DJDYgYmhzm+4iUAhJ2TOluvYkoXkQMg31Csc6akMaM99OOBTtczfCYXi7fICpkoKzEhaaZS2Q/MB0m2QFgId5xLvRP5YY4fF0DYd4T7t8Ix6FCgx/b+BRi4d3KYH1ZYYGM1jpscyV4VodSf4xiI/dlA5Bk783UuE+oTUUYiNOokW3cLFk7QWeN4b2gowN2MkUJxelBvLdE/B0AynaVzEKbheilcTVtr0emMUPcQCp2uSt3hznNPLLCAPNm4h59XNezmyxEaVthtxYk+eJz32ui8eVwJidbua/dNBUtHnVn8+tLsZdAwUBkcY+UrZup3CzXZtnHavRdWLhC4AWe68t3GEatCuDfnmDw64pD932clLOjfAk3/dZ6SJ73Gqlg0rM0qG84nnFzYJ1P0054yuNkVMEJ9uvzWBz9RtociDCplR0e3kHPF0XItd6w6Jz7iK1mw/XTmpmtABbgEplBgGJRUgUjxWj7Za8ilyIftlRXPLrWvy8jVmxG1gNYO3tGAPFx2SjFCEWGuP54Bd1FczpvQiSzo9JIDq2FqBu1d4ywnW6SJ0dBnLSn5BxNFfTF+OcwKrqH4PQ5YdkniQjgUqCiO4CZx3uIfYn2f2wvhbmQcCn4KxL7R2S8iWJwoejeGV/aow5KAODnXb43BxPZNvKdLmNOc9oWpnK6HcXhrtR/uuVuSyLdNDvTWFpLiD7116syjLd1L9MSYEvkqOy7g2JscD3QP2CFz/pWaYi6Wa2/WKq4j2wENusQ0c2Fk3KGzmcBLGorZODOypguQR/zTUyi59tnrw5dhpoIww9uu4VoYZulTcT02Fc6RgXm9FsUONTWxpY7z0DeHRjVf0Qh/pXDl8NNFCrGiD/mVW0Q/HqrlUbnhz7F3UoCeQBM9XcsiUGdMxhfyVLsWs7QxzDgZ86YBKgJ87Ref0A8RX6JzYIKZPMvrl4MpVJ9/lDavqQYChuY2APdGpbSheTQaOzfe9Z/PxbL020dAlaGpRtzDhaCFFysc/xwQ/nKXU0GGPf/1TdggA=
# time, cur, open = pressure
# only non-zero valves
# bitmask opened valves
print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')
