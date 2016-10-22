# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 14:00:07 2015

@author: liuweizhi
"""

## version 1
I=lambda:map(int,raw_input().split())
n,t,c=I();seq=I();seg=[0]
for i in seq:
    if i<=t:
        seg[-1]+=1
    else:
        seg.append(0)
print sum([max(i-c+1,0) for i in seg])

## version 2
R=lambda:map(int,raw_input().split())
n,t,c=R()
a=R()+[t+1]
u,v=-1,0
for i in range(n+1):
  if a[i]>t:
    if i-u-1>=c:
      v+=i-u-1-c+1
    u=i
print v