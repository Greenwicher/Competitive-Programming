# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 17:34:18 2015

@author: liuweizhi
"""

## version 1
print ['NO', 'YES'][map(lambda x: 'H' in x or 'Q' in x or '9' in x or '+' in x, [raw_input()])[0]]

## version 2
print"YNEOS"[not set('HQ9')&set(raw_input())::2]