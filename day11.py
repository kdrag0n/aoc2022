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

mks = []
while True:
    for _l in file_lines:
        ls=_l.split('\n')
        mi=int(ls[0].split()[1].replace(':',''))
        items = ls[1].replace('  Starting items: ', '').split(', ')
        items = [int(i) for i in items]
        op = ls[2].replace('  Operation: ', '')
        testn = ls[3].split()[-1]
        testn = int(testn)
        to_true = ls[4].split()[-1]
        to_true = int(to_true)
        to_false = ls[5].split()[-1]
        to_false = int(to_false)
        mks += [{
            'mi': mi,
            'items': items,
            'op': op,
            'testn': testn,
            'to_true': to_true,
            'to_false': to_false,
        }]

    break


inscs = [0] * len(mks)
for _ in range(20):
    for mi, mk in enumerate(mks):
        print(f'Monkey {mi}')
        for item in list(mk['items']):
            print(f'  Item {item}')
            old = item
            new = -1
            exec(mk['op'])
            inscs[mi] +=1
            new //= 3
            print(f' . worry {old} ->{new}')
            if new % mk['testn'] == 0:
                to = mk['to_true']
            else:
                to = mk['to_false']
            print(f' . to {to}')
            mks[to]['items'].append(new)
            mks[mi]['items'] = mks[mi]['items'][1:]

print(inscs)
a, b=sorted(inscs)[-2:]
print(a*b)


print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')
