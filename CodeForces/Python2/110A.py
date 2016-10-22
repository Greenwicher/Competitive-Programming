# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 21:04:27 2015

@author: liuweizhi
"""

## version 1
number = raw_input()
print ['NO', 'YES'][set(['4','7']) >= set(str(number.count('4')+number.count('7')))]

## version 2 (I think it's wrong)
s=raw_input()
print ['NO','YES'][s.count('4')+s.count('7') in [4,7]]