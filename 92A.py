# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 12:43:18 2015

@author: liuweizhi
"""

## version 1
n,m=map(int,raw_input().split());k=m%(n*(n+1)/2);i=1
while (i<=n) and (i<=k):
    k=[k-i,k][i>k]
    i+=1
print k