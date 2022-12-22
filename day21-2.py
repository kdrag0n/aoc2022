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
import z3
symmap={}
mks={}
s=z3.Solver()
added=set()
#while True:
addn=0
print('i')
for l in file_lines:
    #if l in added: break
    l1, l2 = l.split(': ')
    print('ln',l)
    if l1=='humn': continue
    if len(l2.split())==1:
        mks[l1]=int(l2)
        symmap[l1]=z3.IntVal(int(l2))
        s.add(z3.Int(l1)==z3.IntVal(int(l2)))
        added.add(l)
        addn+=1
        continue

    lhs,op,rhs=l2.split()
    mks[l1]=(op,lhs,rhs)
    # if lhs not in symmap or rhs not in symmap:
    #     continue
    # if op=='+':
    #     symmap[l1]=symmap[lhs]+symmap[rhs]
    # elif op=='*':
    #     symmap[l1]=symmap[lhs]*symmap[rhs]
    # elif op=='/':
    #     symmap[l1]=symmap[lhs]/symmap[rhs]
    # elif op=='-':
    #     symmap[l1]=symmap[lhs]-symmap[rhs]
    if op=='+':
        print('add', l1, lhs, rhs)
        s.add(z3.Int(l1)==z3.Int(lhs)+z3.Int(rhs))
    elif op=='*':
        print('mul', l1, lhs, rhs)
        s.add(z3.Int(l1)==z3.Int(lhs)*z3.Int(rhs))
    elif op=='/':
        print('div', l1, lhs, rhs)

        s.add(z3.Int(l1)==z3.Int(lhs)/z3.Int(rhs))
    elif op=='-':
        print('sub', l1, lhs, rhs)
        s.add(z3.Int(l1)==z3.Int(lhs)-z3.Int(rhs))
    added.add(l)
    # break
    # if addn==0:
    #     break
root_op, root_lhs, root_rhs = mks['root']
#s.add(symmap[root_lhs]==symmap[root_rhs])
s.add(z3.Int(root_lhs)==z3.Int(root_rhs))
print(s.check())
print(s.model())

print(s.model().eval(z3.Int('humn')))
