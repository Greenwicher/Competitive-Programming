# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 13:24:18 2015

@author: liuweizhi
"""

## version 1
x,y=map(int,raw_input().split())
k=2*(x*y<0)-1
if x-y/k>0:
    print 0,y-k*x,x-y/k,0 
else:
    print x-y/k,0,0,y-k*x