# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 12:22:42 2015

@author: liuweizhi
"""
## version 1
I=lambda:map(int,raw_input().split())
n,l=I();a=sorted(I())
print max([(j-i)/2.0 for i,j in zip(a[:-1],a[1:])]+[a[0],l-a[-1]])
