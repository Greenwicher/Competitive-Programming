# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 20:44:19 2015

@author: liuweizhi
"""

## version 1
f=lambda n:n*(n-1)/2
n,m=map(int,raw_input().split())
print (n%m)*f(n/m+1)+(m-n%m)*f(n/m),f(n-m+1)

## version 2
n,m=map(int,raw_input().split())
a=n/m
print m*a*(a-1)/2+a*(n%m),(n-m)*(n-m+1)/2
