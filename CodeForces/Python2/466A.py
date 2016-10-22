# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 12:29:26 2015

@author: liuweizhi
"""

## version 1 (decision trees)
n,m,a,b=map(int,raw_input().split())
print min(n*a, n*(-1)/m*(-1)*b, n/m*b+(n-n/m*m)*a)

## version 2
n,m,a,b=map(int,raw_input().split())
print min(a*n,(n/m)*b+n%m*a,(n/m)*b+b)