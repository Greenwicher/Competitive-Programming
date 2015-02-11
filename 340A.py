# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 12:13:32 2015

@author: liuweizhi
"""

## version 1
x,y,a,b=map(int,raw_input().split())
for i in range(1,x*y+1):
    if i%x==0 and i%y==0:
        k=i
        break
print b/k+(-a/k)+1

## version 2
x,y,a,b=map(int,raw_input().split())
from fractions import *
l=x*y/gcd(x,y)
print b/l-(a-1)/l

## version 3
G=lambda x,y:x+y if x*y==0 else G(y,x%y)
x,y,a,b=map(int,raw_input().split())
T=x*y/G(x,y)
print b/T-(a-1)/T