# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 14:05:16 2015

@author: liuweizhi
"""

## version 1
n=input()
a=map(int,raw_input().split())
print n-1
for i in range(n-1):
    k=n-1-a[::-1].index(min(a[i:]))
    a[i],a[k]=a[k],a[i]
    print i,k
    
## version 2
n = input()
a = map(int, raw_input().split())
print n
for i in xrange(n):
    m = a[i:].index(min(a[i:]))
    print i,m+i
    a[i],a[m+i] = a[m+i],a[i]
    