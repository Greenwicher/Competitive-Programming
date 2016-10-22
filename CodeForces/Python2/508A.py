# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 15:02:04 2015

@author: liuweizhi
"""

## version 1 (Time limit exceeded on test 17	)
I=lambda:map(int,raw_input().split())
n,m,k=I();a=set();ans=0
f=lambda a,x,y: (set([(x-1,y-1),(x-1,y),(x,y-1)])<a) or (set([(x-1,y),(x-1,y+1),(x,y+1)])<a) or (set([(x,y-1),(x+1,y),(x+1,y-1)])<a) or (set([(x,y+1),(x+1,y+1),(x+1,y)])<a)
for i in range(k):
    x,y=I()
    if (x,y) not in a:
        a=a.union(set([(x,y)]))
        if f(a,x,y):
            ans=i+1
            break
print ans

## version 2
