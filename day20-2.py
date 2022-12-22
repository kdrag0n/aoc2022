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

class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = None

    def __repr__(self):
        return f'Node({self.val}, {self.next})'

ns=ints(file_lines)
ns=[n*811589153 for n in ns]
ons=ns
nodes = [Node(v) for v in ons]
zid=ns.index(0)
#n,id
ns=[(n,i) for i,n in enumerate(ns)]
idmap={i:ns[i][0] for i in range(len(ns))}

print('init',[n[0] for n in ns])
for id in range(len(ns)):
    exp=(idmap[id],id)
    i = ns.index(exp)
    val,_=exp
    new_i = i+val
    new_i %= len(ns)
    # if val>0:
    #     new_i += 1
    if val == 0:continue
    #print('new_i',new_i)
    # move to new_i in ns
    #print('move',val,'from',i,'to',new_i,'before',ns[new_i][0],'after',ns[new_i+1][0])
    old_exp='asd'
    ns[i]=old_exp
    ns.remove(old_exp)
    if val<0:
        new_i -= 1
    new_i %= len(ns)
    ns.insert(new_i,exp)
    # ns.remove(exp)
    # if new_i > i:
    #     new_i -= 1
    # ns.insert(new_i+1,exp)
    #print('step',id,[n[0] for n in ns])
#print('end',[n[0] for n in ns])
zi=ns.index((0,zid))
print('n1',ns[(zi+1000)%len(ns)][0])
print('n2',ns[(zi+2000)%len(ns)][0])
print('n3',ns[(zi+3000)%len(ns)][0])
total=ns[(zi+1000)%len(ns)][0]+ns[(zi+2000)%len(ns)][0]+ns[(zi+3000)%len(ns)][0]

def print_list(start):
    cur = start
    while cur.next != start:
        print(cur.val, end=', ')
        cur = cur.next
    print(cur.val)
vnodes=nodes[:]
for i in range(len(nodes)):
    nodes[i].next = nodes[(i+1)%len(nodes)]
    nodes[i].prev = nodes[(i-1)%len(nodes)]
znode=nodes[zid]
for _ in range(10):
    for node in vnodes:
        val=node.val
        #print('curv',val)
        #if val<0: val = -val

        newlen=len(vnodes)-1
        count=abs(val)%newlen
        if count == 0:
            continue

        cur=node
        before_cur=cur.prev
        after_cur=cur.next


        before_cur.next=after_cur
        after_cur.prev=before_cur

        tgt = node
        if val>0:
            for i in range(count):
                tgt = tgt.next
        else:
            for i in range(count+1):
                tgt = tgt.prev
        #print_list(znode)

        # move node to tgt
        # node.prev.next = node.next
        # node.next.prev = node.prev
        # node.next = tgt.next
        # node.prev = tgt
        # tgt.next.prev = node
        # tgt.next = node
        cur=node
        before_cur=cur.prev
        after_cur=cur.next
        before_tgt=tgt.prev
        after_tgt=tgt.next

        tgt.next=cur
        cur.prev=tgt
        cur.next=after_tgt
        after_tgt.prev=cur

#print_list(znode)

def find_at(i):
    cur = znode
    for _ in range(i):
        cur = cur.next
    return cur.val
n1=find_at(1000)
n2=find_at(2000)
n3=find_at(3000)
print('n1',n1)
print('n2',n2)
print('n3',n3)
total=n1+n2+n3

# tsq=[4, -2, 5, 6, 7, 8, 9]
# testl=[Node(v) for v in tsq]
# for i in range(len(testl)):
#     testl[i].next = testl[(i+1)%len(testl)]
#     testl[i].prev = testl[(i-1)%len(testl)]

# node = testl[tsq.index(-2)]
# fnode=testl[0]
# val=node.val
# tgt = node
# if val>0:
#     for i in range(val):
#         tgt = tgt.next
#     # move node to tgt
#     node.prev.next = node.next
#     node.next.prev = node.prev
#     node.next = tgt.next
#     node.prev = tgt
#     tgt.next.prev = node
#     tgt.next = node
# else:
#     for i in range(-val):
#         tgt = tgt.prev
#     # move node to tgt
#     node.prev.next = node.next
#     node.next.prev = node.prev
#     node.next = tgt
#     node.prev = tgt.prev
#     tgt.prev.next = node
#     tgt.prev = node
# print_list(fnode)
print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')
