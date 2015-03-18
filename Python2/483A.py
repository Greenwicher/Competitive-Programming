# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 14:10:07 2015

@author: liuweizhi
"""

## version 1
l,r=map(int,raw_input().split())
f=lambda x,y:any([x%i==0 and y%i==0 for i in range(2,min(x,y)+1)])
for i in range(l,r-1):
    for j in range(i+1,r):
        for k in range(j+1,r+1):
            if (not f(i,j)) and (not f(j,k)) and f(i,k):
                print i,j,k
                exit(0)
print -1