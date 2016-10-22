# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 19:54:29 2015

@author: liuweizhi
"""

## version 1
I=lambda:map(int,raw_input().split())
n,d=I();s=I();t=(n-1)*10+sum(s)
print -1 if t>d else 2*(n-1)+(d-t)/5

## version 2
I=lambda:map(int,raw_input().split())
n,d=I()
s=sum(I())
print[-1,(d-s)/5][10*~-n+s<=d]