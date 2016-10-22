# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 18:43:15 2015

@author: liuweizhi
"""

## version 1
n,k=map(int,raw_input().split())
for i in range(1,k+2)[::-1]+range(k+2,n+1):
    print i,