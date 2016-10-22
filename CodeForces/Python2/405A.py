# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 22:23:43 2015

@author: liuweizhi
"""

## version 1
input()
print ' '.join(map(str,sorted(map(int,raw_input().split()))))

## version 2
raw_input()
print ' '.join(sorted(raw_input().split(), key=int))