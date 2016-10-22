# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 21:05:48 2015

@author: liuweizhi
"""

## version 1
I=lambda:map(int,raw_input().split())
n,c=I();seq=I();ans=0
for i in range(n-1):
    ans=max(ans,seq[i]-seq[i+1]-c)
print ans

## version 2
I=lambda:map(int,raw_input().split())
n,c=I()
x=I()
print max(c,*(i-j for i,j in zip(x,x[1:])))-c