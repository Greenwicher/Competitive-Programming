# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 11:11:06 2015

@author: liuweizhi
"""

## version 1 (Wrong answer on test 8)
I=lambda:map(int,raw_input().split())
n,x,y=I();ans=set()
for _ in range(n):
    a,b=I()
    if x!=a:
        ans|={str(round(float(b-y)/(a-x),6))}
    else:
        ans|={'inf'}
print len(ans)

## version 2
I=lambda:map(float,raw_input().split())
n,x,y=I();ans=set()
for _ in range(int(n)):
    a,b=I()
    if x!=a:
        ans.add((b-y)/(a-x))
    else:
        ans.add(float('inf'))
print len(ans)