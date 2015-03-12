# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 12:36:50 2015

@author: liuweizhi
"""

## version 1 (Time limit exceeded on test 9)
n=input()
a=zip(*[map(int,raw_input().split()) for _ in range(n)])
for i in range(n):
    t=a[0].count(a[1][i])
    print n-1+t,n-1-t
    
## version 2
n=input()
a=zip(*[map(int,raw_input().split()) for _ in range(n)])
x={}
for i in a[0]:x[i]=x.get(i,0)+1
for i in range(n):
    t=x.get(a[1][i],0)
    print n-1+t,n-1-t