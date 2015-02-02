# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 20:23:51 2015

@author: liuweizhi
"""

## version 1
I=lambda:map(int,raw_input().split())
input();d=I();a,b=I()
print sum(d[a-1:b-1])