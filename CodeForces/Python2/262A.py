# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 12:59:01 2015

@author: liuweizhi
"""

## version 1
I=lambda:map(int,raw_input().split())
n,k=I()
print sum(1 for i in I() if str(i).count('4')+str(i).count('7')<=k)