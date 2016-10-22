# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 11:02:59 2015

@author: liuweizhi
"""

## version 1
n=input();t=map(int,raw_input().split())
ans=0
for i in range(1,11):
    ans+=t.count(i)*t.count(-i)
print ans+t.count(0)*(t.count(0)-1)/2


## version 2
input()
f=map(int,raw_input().split()).count
print (f(0)*f(0)-f(0)>>1) + sum(f(i)*f(-i) for i in range(1,11))