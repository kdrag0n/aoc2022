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
import itertools
nmap={'2':2,'1':1,'0':0,'-':-1,'=':-2}
nmap_recv={2:'2',1:'1',0:'0',-1:'-',-2:'='}
def dec_to_snafu(n):
    on=n
    s=''
    rem=0
    val=1
    extra=0
    while n>0:
        dig=n%5
        if rem:
            dig+=1
            rem=0
            extra+=val-rem
        if dig in nmap_recv:
            s+=nmap_recv[dig]
        else:
            s+='?'
            rem+=val*dig
        n//=5
        val*=5
    print('rem', rem)
    print('extra',extra)
    s=s[::-1]
    ss=list(s)
    nqs=[]
    for i,c in enumerate(ss):
        copy=ss[:]
        if c=='?':
            nqs+=[i]
    for perm in itertools.product(['-','=','0'], repeat=len(nqs)):
        copy=ss[:]
        for _i, c in enumerate(perm):
            copy[nqs[_i]]=c
        if snafu_to_dec(''.join(copy))==on:
            print(''.join(copy))
            return ''.join(copy)


    print('NONE')
    return s[::-1]

def snafu_to_dec(st):
    n=0
    for i, c in enumerate(st[::-1]):
        n+=nmap[c]*(5**i)
    return n
sum=0
while True:
    for l in file_lines:
        sum+=snafu_to_dec(l)

    break
print(sum)
print(dec_to_snafu(sum))


print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')
