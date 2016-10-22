# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 13:42:04 2015

@author: liuweizhi
"""

## version 1
I=lambda:map(int,raw_input().split())
n,x=I();c=sorted(I());ans=0
for i in range(n):
    ans+=c[i]*max(x,1)
    x-=1
print ans

## version 2
I=lambda:map(int,raw_input().split())
n,x=I()
print sum(i*max(1,x-j) for i,j in zip(sorted(I()),range(n)))