# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 02:03:37 2015

@author: liuweizhi
"""

## version 1
import re
print ['NO', 'YES'][re.findall('h\S*e\S*l\S*l\S*o', raw_input())!=[]]

## version 2
pattern = ['o','l','l','e','h']
judge = False
for w in raw_input():
    if w==pattern[-1]:
        pattern.pop()
    if not pattern:
        judge = True
        break
print ['NO', 'YES'][judge]

## version 3
import re
print"YES"if re.search("h.*e.*l.*l.*o",raw_input())else"NO"