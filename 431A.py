# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 17:28:47 2015

@author: liuweizhi
"""

## version 1
a=map(int,raw_input().split())
seq=raw_input()
print sum(a[i]*seq.count(str(i+1)) for i in range(4))

## version 2
a = map(int, raw_input().split())
print sum(a[int(c)-1] for c in raw_input())

## version 3
a=map(int,raw_input().split())
print sum(map(lambda x:a[int(x)-1],raw_input()))

## version 4
a=[0]+map(int, raw_input().split())
print sum(map(a.__getitem__, map(int, raw_input())))