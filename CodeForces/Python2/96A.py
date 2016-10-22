# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 09:03:55 2015

@author: liuweizhi
"""

## version 1
seq = raw_input()
print ['NO', 'YES']['0'*7 in seq or '1'*7 in seq]

## version 2
print ['NO', 'YES'][map(lambda x: ('0'*7 in x) or ('1'*7 in x), [raw_input()])[0]]

## version 3
import re
print'YES'if re.search("0{7,}|1{7,}",raw_input())else'NO'