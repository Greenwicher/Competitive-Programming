# -*- coding: utf-8 -*-
"""
Created on Sun Jan  4 15:23:40 2015

@author: liuweizhi
"""

## version 1
print reduce(lambda x,y:x*y, map(int, raw_input().split())) / 2

## version 2
print eval(raw_input().replace(" ","*"))/2