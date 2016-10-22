# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 02:40:39 2015

@author: liuweizhi
"""

## version 1
input()
p = map(int, raw_input().split())
q = [0]*len(p)
for i in range(len(p)):
    q[p[i]-1] = i + 1
print ' '.join(map(str, q))

## version 2
a=input()
b=map(int,raw_input().split())
for i in range(a):
    print b.index(i+1)+1,

## version 3
a=input();
b=map(int,raw_input().split())
c=sorted(zip(b, range(1,len(b)+1)))
for i in range(len(c)):
    print c[i][1],