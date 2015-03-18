# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 21:21:02 2015

@author: liuweizhi
"""

## version 1
year = input() + 1
while len(set(str(year))) != len(str(year)):
    year += 1
print year

