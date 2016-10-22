# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 10:43:18 2015

@author: liuweizhi
"""

## version 1
a,b,c=map(int,raw_input().split())
d=(a*b*c)**(0.5)
print 4*int(d/a+d/b+d/c)