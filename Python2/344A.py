# -*- coding: utf-8 -*-
"""
Created on Fri Jan  9 12:56:10 2015

@author: liuweizhi
"""

## version 1
n = input()
seq = ''
ans = 0
for i in range(n):
    tmp = raw_input()
    if tmp != seq:
        ans += 1
        seq = tmp
print ans

## version 2
import re
n = input()
seq = ''
for i in range(n):
    seq += raw_input()[0]
print len(re.split('0+', seq)) + len(re.split('1+', seq)) - 2

## version 3 (zip() & bitewise operations)
l=map(raw_input," "*input())
print-~sum(a!=b for a,b in zip(l,l[1:]))

## version 4 (the linkage between groups, think from the other side)
n=input()
s="".join([raw_input() for _ in range(n)])
print s.count('11')+s.count('00')+1

## version 5 (regular expression & linkage)
import re 
print len(re.compile('00|11').split(''.join(raw_input() for _ in [0]*input())))