#!/usr/bin/env python3

import sys

def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], 'r') as f:
    file_lines = [l for l in f.read().strip().split('\n')]



TOTAL = 70000000
TARGET = 30000000

in_nums = []

total = 0
result = 0
other = 0

while True:
    cur_cmd = ''
    cwd = ''
    fs = {}
    for l in file_lines:
        if l.startswith('$ '):
            args = l[2:].split(' ')            
            cur_cmd = args[0]
            args = args[1:]
            print(cur_cmd, args)
            if cur_cmd == 'cd':
                if args[0] == '..':
                    cwd = '/'.join(cwd.split('/')[:-2]) + '/'
                else:
                    cwd += f'{args[0]}/'.replace('//', '/')
            else:
                continue
        if cur_cmd == 'ls':
            sz, name = l.split(' ')
            if sz == 'dir':
                node = {}
            else:
                node = int(sz)
            # convert to tree
            cwd_parts = cwd.split('/')
            cur = fs
            print(cwd, cwd_parts)
            for p in cwd_parts:
                if p == '':
                    continue
                cur = cur[p]
            cur[name] = node


    break

print(fs)
def get_size(node):
    if type(node) == int:
        return node
    else:
        return sum([get_size(n) for n in node.values()])

dir_szs = []
def recurse(root):
    global total
    global dir_szs
    for name, node in root.items():
        if type(node) == int:
            continue
        else:
            recurse(node)
            if get_size(node) <= 100000:
                total += get_size(node)
            dir_szs += [(node, get_size(node))]
recurse(fs)
dir_szs = sorted(dir_szs, key=lambda x: x[1], reverse=False)
USED = get_size(fs)
for node, sz in dir_szs:
    print('opt', sz)
    free = TOTAL - USED
    if free + sz >= TARGET:
        result += sz
        break

print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')
