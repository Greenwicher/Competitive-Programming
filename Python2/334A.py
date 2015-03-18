# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 22:18:46 2015

@author: liuweizhi
"""

## version 1
n=input()
for i in range(1,n+1):
    a=i
    for j in range(n):
       print a,
       a=[a+n+1,a+1][a%n==0]
    print 
    
## version 2
n=int(input())
for i in range(n*n/2): print i+1,n*n-i,

## version 3
n=input()
for i in range(n):
 for j in range(n/2):print-~j+i*n,n*n-i*n-j,
 print