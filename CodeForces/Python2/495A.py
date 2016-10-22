# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 11:49:15 2015

@author: liuweizhi
"""

## version 1
x,y=map(int,list(raw_input()))
a=[2,7,2,3,3,4,2,5,1,2]
print a[x]*a[y]

## version 2
g=[2,7,2,3,3,4,2,5,1,2]
n=int(raw_input())
print g[n%10]*g[n/10]