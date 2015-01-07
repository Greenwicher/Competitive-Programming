# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 01:12:35 2015

@author: liuweizhi
"""

## version 1
n,m = map(int, raw_input().split())
day = 0
while n != 0:
    n -= 1
    day += 1
    if day % m == 0:
        n += 1
print day

## version 2
n,m=map(int,raw_input().split())
print (m*n-1)/(m-1)

## version 3
n,m=map(int,raw_input().split())
print n+~-n/~-m