# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 21:27:18 2015

@author: liuweizhi
"""

## version 1
print len(set(raw_input())-set(['{','}',',',' ']))

## version 2
print len(set(raw_input()+" ,"))-4

## version 3
S = raw_input()
print len(set(S) - set("{} ,"))