# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 12:33:17 2015

@author: liuweizhi
"""

## version 1
n=input()
if n%2!=0:
    print -1
else:
    for i in range(n/2):
        print 2*(i+1),2*i+1,

## version 2
n=input();print [' '.join(map(str,range(n,0,-1))),-1][n&1]