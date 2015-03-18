# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 14:01:46 2015

@author: liuweizhi
"""

## version 1
x,y=map(int,raw_input().split());n=input()
f=[x,y,y-x,-x,-y,x-y][n%6-1]
print f%(10**9+7)