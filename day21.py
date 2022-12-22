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

mks={}
while True:
    for l in file_lines:
        l1, l2 = l.split(': ')
        if len(l2.split())==1:
            mks[l1]=int(l2)
            continue
        lhs,op,rhs=l2.split()
        mks[l1]=(op,lhs,rhs)

        if False:
            total += 1

    break

def evalmk(id):
    if isinstance(mks[id],int):
        return mks[id]
    op,lhs,rhs=mks[id]
    if op=='+':
        return evalmk(lhs)+evalmk(rhs)
    elif op=='*':
        return evalmk(lhs)*evalmk(rhs)
    elif op=='/':
        return evalmk(lhs)//evalmk(rhs)
    elif op=='-':
        return evalmk(lhs)-evalmk(rhs)
print(evalmk('root'))

print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')
