# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 20:03:44 2015

@author: liuweizhi
"""

## version 1
I=lambda:map(int,raw_input().split())
n,m,k=I();a=I()
b,p=[a.count(1),a.count(2)]
print b+p-min(b,m)-min(p,k+m-min(b,m))

## version 2
R=lambda:map(int,raw_input().split())
n,m,k=R()
a=R().count(1)
print max(0,max(n-a-k,0)+a-m)