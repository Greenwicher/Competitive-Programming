# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 17:01:50 2015

@author: liuweizhi
"""

## version 1
n=input();
a=[[0+1*(i==0 or j==0) for j in range(n)] for i in range(n)]
for i in range(1,n):
    for j in range(1,n):
        a[i][j]=a[i-1][j]+a[i][j-1]
print a[n-1][n-1]

## version 2 (elegant formula)
import math
n = input()
print math.factorial((n-1)*2)/(math.factorial(n-1)*math.factorial(n-1))

## version 3 (one dimensional reduction, memorylization)
n=input()
a=[1]*n
for i in range(1,n):
  for j in range(1,n):
    a[j]+=a[j-1]
print a[-1]