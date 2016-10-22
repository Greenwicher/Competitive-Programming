# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 01:56:09 2015

@author: liuweizhi
"""

## version 1
print 4 - len(set(map(int, raw_input().split())))

## version 2
print 4-len(set(raw_input().split()))