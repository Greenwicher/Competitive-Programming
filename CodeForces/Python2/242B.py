# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 12:39:17 2015

@author: liuweizhi
"""

## version 1
l=[];r=[];lmin=10**9;rmax=0
for i in range(input()):
    a,b=map(int,raw_input().split())
    if a==lmin: l.append(i)
    if a<lmin: lmin=a;l=[i]
    if b==rmax: r.append(i)
    if b>rmax: rmax=b;r=[i]
ans=set(l) & set(r)
print list(ans)[0]+1 if ans else -1

## version 2
s = [map(int, raw_input().split()) for _ in range(input())]
l = min(zip(*s)[0])
r = max(zip(*s)[1])
print s.index([l, r]) + 1 if [l, r] in s else -1
    