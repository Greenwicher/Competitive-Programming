# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 22:04:58 2015

@author: liuweizhi
"""

## version 1
I=lambda:map(int,raw_input().split())
n,s=I();a=sorted(I())
print 'YNEOS'[sum(a[:-1])>s::2]