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

SIZE = 200
grid = [[None] * SIZE for _ in range(SIZE)]


def print_gr():
    return
    gr3 = [['.'] * SIZE for _ in range(SIZE)]
    gr3[sp[1]][sp[0]] = 's'
    gr3[hp[1]][hp[0]] = 'H'
    gr3[tp[1]][tp[0]] = 'T'
    print('\n'.join(''.join(l) for l in gr3))
    print()
sp = (SIZE//2, SIZE//2)
knots = [sp] * 10
visited = set()
import math
def update_tail(i):
    #global tp
    hx, hy = knots[i + 1]
    tx, ty = knots[i]
    dx = hx - tx
    dy = hy - ty
    # if dx > 1 
    d2 = (hx - tx) ** 2 + (hy - ty) ** 2
    print('d2', d2)
    if math.sqrt(d2) > math.sqrt(2):
        if hx == tx:
            print('sx')
            if hy > ty:
                ty += 1
            else:
                ty -= 1
        elif hy == ty:
            print('sy')
            if hx > tx:
                tx += 1
            else:
                tx -= 1
        else:
            print('diag', hx, hy, tx, ty)
            if hx > tx:
                tx += 1
            else:
                tx -= 1
            if hy > ty:
                ty += 1
            else:
                ty -= 1
    tp = (tx, ty)
    knots[i] = tp
    if i == 0:
        visited.add(tp)
    print_gr()
def update_tails():
    for i in range(len(knots) - 2, -1, -1):
        update_tail(i)
def set_dhead(dx, dy):
    hp = knots[-1]
    knots[-1] = (hp[0] + dx, hp[1] + dy)
while True:
    for l in file_lines:
        dir, n = l.split()
        n = int(n)
        print(dir, n)
        if dir == 'R':
            for _ in range(n):
                set_dhead(1, 0)
                update_tails()
        elif dir == 'L':
            for _ in range(n):
                set_dhead(-1, 0)
                update_tails()
        elif dir == 'U':
            for _ in range(n):
                set_dhead(0, -1)
                update_tails()
        elif dir == 'D':
            for _ in range(n):
                set_dhead(0, 1)
                update_tails()

        if False:
            total += 1

    break

gr2 = [['.'] * 200 for _ in range(200)]
gr2[sp[1]][sp[0]] = 's'
for x, y in visited:
    gr2[y][x] = '#'
print('\n'.join(''.join(l) for l in gr2))

print(len(visited))
print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')
