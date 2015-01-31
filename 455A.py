# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 11:09:40 2015

@author: liuweizhi
"""

## version 1
n=input();a=sorted(map(int,raw_input().split()))
b=[[i,a.count(i)] for i in set(a)]
f=lambda b,k: sum([p[0]*p[1] for p in b[k::2]])
print max(f(b,0),f(b,1))
