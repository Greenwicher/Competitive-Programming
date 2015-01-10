# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 21:01:21 2015

@author: liuweizhi
"""

## version 1
print ['NO', 'YES'][raw_input()==raw_input()[::-1]]

## version 2
print raw_input()==raw_input()[::-1]and'YES'or'NO'

## version 3
r=raw_input;print"YNEOS"[r()!=r()[::-1]::2]