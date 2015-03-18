# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 14:49:56 2015

@author: liuweizhi
"""

## version 1
I=lambda:raw_input().split()
n,m=map(int,I());d={}
for i in range(m):
    a,b=I()
    d[a]=[a,b][len(b)<len(a)]
s=I()
print ' '.join([d[i] for i in s])
