# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:40:17 2015

@author: liuweizhi
"""

## version 1
I=lambda:map(int,input().split())
n,k=I();a=list(I());b=list(range(1,n*k+1))
for i in a:b.remove(i)
for i in range(k):
    print(' '.join(map(str,[a[i]]+b[i*(n-1):i*(n-1)+n-1])))