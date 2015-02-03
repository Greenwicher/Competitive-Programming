# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 13:25:50 2015

@author: liuweizhi
"""

## version 1
I=lambda:map(int,raw_input().split())
n,m=I();a=I();k=b=0
for i in range(n):
    k+=[0,1][b+a[i]>m]
    b=[b+a[i],a[i]][b+a[i]>m]
print k+1