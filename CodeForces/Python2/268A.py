# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 21:36:07 2015

@author: liuweizhi
"""

## version 1
n=input();h=[0]*n;a=[0]*n;ans=0
for i in range(n):
    h[i],a[i]=map(int,raw_input().split())
for i in range(len(h)):
    for j in range(len(a)):
        if i!=j and h[i]==a[j]:
            ans+=1
print ans

## version 2 (sum()，主场客场球衣颜色本来就不同)
a=[raw_input().split()for i in range(input())]
print sum(i[0]==j[1]for i in a for j in a)

## version 3
from collections import Counter as C
a=C();b=C();s=0
for i in[0]*input():x,y=raw_input().split();s+=a[y]+b[x];a[x]+=1;b[y]+=1
print s

## version 4
a,b = zip(*[map(int, raw_input().split()) for _ in [0]*input()])
print sum([b.count(i) for i in a])
