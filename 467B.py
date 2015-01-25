# -*- coding: utf-8 -*-
"""
Created on Sun Jan 25 14:04:29 2015

@author: liuweizhi
"""

## version 1
n,m,k=map(int,raw_input().split())
seq=[input() for i in range(m+1)]
print sum(1 for i in range(m) if bin(seq[m]^seq[i]).count('1')<=k)

