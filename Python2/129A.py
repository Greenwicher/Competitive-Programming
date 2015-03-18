# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 13:38:07 2015

@author: liuweizhi
"""

## version 1
n=input();a=map(int,raw_input().split())
print sum(1 for i in a if (sum(a)-i)%2==0)

## version 2
r=raw_input;r();a=map(int,r().split());print sum(1^sum(a)-i&1for i in a)