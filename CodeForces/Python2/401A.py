# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 19:36:55 2015

@author: liuweizhi
"""

## version 1
I=lambda:map(int,raw_input().split())
n,x=I();c=I()
print -(-abs(sum(c))/x)

## version 2
I=lambda:map(int,raw_input().split())
n,x=I()
print ~-abs(sum(I()))/x+1