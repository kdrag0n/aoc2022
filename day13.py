#!/usr/bin/env python3

import sys

def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], 'r') as f:
    file_lines = [l for l in f.read().strip().split('\n\n')]


in_nums = []

total = 0
result = 0
other = 0

def cmp(l,r):
    print(l,r)
    if isinstance(l, int) and isinstance(r, int):
        if l==r: return -1
        return l<r
    elif isinstance(l, list) and isinstance(r, list):
        # if len(l)==0: return True
        # if len(r)==0: return False
        for i in range(max(len(l), len(r))):
            print('l', l, 'r', r)
            if i >= len(l): return True
            if i >= len(r): return False
            res= cmp(l[i], r[i])
            if  res == False:
                return False
            elif res == True:
                return True
        print('ERR')
        return -1
    elif isinstance(l, list):
        return cmp(l, [r])
    elif isinstance(r, list):
        return cmp([l], r)
    print('ERR')
    return -1
while True:
    for i,_l in enumerate(file_lines):
        l, r = _l.split('\n')
        l = eval(l)
        r = eval(r)
        res = cmp(l, r)
        if res == True:
            print('=TRUE')
            print('ai', i+1)
            print()
            result+=i+1
        elif res == False:
            print('=FALSE')
            print()
            other+=i+1
        else:
            print('UNDEF')

    break



print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')
