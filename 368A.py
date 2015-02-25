# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 10:52:07 2015

@author: liuweizhi
"""

## version 1
I=lambda:map(int,raw_input().split())
n,d=I();a=sorted(I());m=input()
print sum(a[:min(n,m)])-d*max(0,m-n)