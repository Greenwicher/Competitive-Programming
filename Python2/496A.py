# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 12:14:09 2015

@author: liuweizhi
"""

## version 1
n=input();a=map(int,raw_input().split());gap=1000
b=[a[i+1]-a[i] for i in range(n-1)];k=max(b)
for i in range(n-2):
    gap=min(gap,max(b[i]+b[i+1],k))
print gap

## version 2
input()
a=map(int,raw_input().split())
D=lambda v,k:[v[i]-v[i-k] for i in range(k,len(v))]
print max(min(D(a,2)),max(D(a,1)))