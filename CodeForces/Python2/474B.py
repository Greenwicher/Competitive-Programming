# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 15:47:09 2015

@author: liuweizhi
"""

## version 1
I=lambda:map(int,raw_input().split())
n=input();a=I();m=input();q=I();b=[0]
for i in range(n):
    b.append(b[-1]+a[i])
def f(k,l,r):
    if l==r:
        return l
    else:
        c=(l+r)/2
        if b[c]<k:
            return f(k,c+1,r)
        else:
            return f(k,l,c)    
for i in range(m):
    print f(q[i],0,n)