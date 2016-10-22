# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 01:27:49 2015

@author: liuweizhi
"""

## version 1
print sum(1 for _ in range(input()) if -eval(raw_input().replace(' ', '-')) >= 2)
