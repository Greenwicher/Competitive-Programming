# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 01:39:02 2015

@author: liuweizhi
"""

## version 1
def composite(x):
    for i in range(2, x):
        if x % i == 0:
            return 1
    return 0
    
def ans(n):
    for i in range(3, n/2+1):
        if composite(i) and composite(n-i):
            return '%d %d' % (i, n-i)

print ans(input())
    
## version 2
n=input();a=(n%2*5+4);print a,n-a

## version 3
n=input();a=(n%2+2)**2;print a,n-a