# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 12:14:20 2015

@author: liuweizhi
"""

## version 1
n=input();k=0;cubes=0;
while cubes<=n: k+=1; cubes=k*(k+1)*(k+2)/6
print k-1

## version 2 (think the other side)
n=input()
k=0
while (k+1)*(k+2)/2<=n:
  k+=1
  n-=k*(k+1)/2
print k