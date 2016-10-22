# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 21:31:42 2015

@author: liuweizhi
"""

## version 1
n=input()
print ' '.join(map(str,[n]+range(1,n)))

## version 2
n=input()
for i in range(n):print i or n,