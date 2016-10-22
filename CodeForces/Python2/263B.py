# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 12:48:44 2015

@author: liuweizhi
"""

## version 1
I=lambda:map(int,raw_input().split())
n,k=I();a=sorted(I())[::-1]
print -1 if n<k else ' '.join([str(a[k-1])]*2)
