# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 10:32:40 2015

@author: liuweizhi
"""

## version 1
n,x,y=map(int,raw_input().split())
a=y/100.0*n-x
print [0,[int(a)+1,int(a)][a-int(a)==0]][a>0]

## version 2
n,x,y=map(int,raw_input().split())
print-min(0,-n*y/100+x)

## version 3
n,x,y=map(int,raw_input().split())
print max(0,(n*y+99)/100-x)