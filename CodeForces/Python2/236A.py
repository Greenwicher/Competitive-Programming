# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 20:06:38 2015

@author: liuweizhi
"""

## version 1
print ['IGNORE HIM!', 'CHAT WITH HER!'][len(set(raw_input())) % 2 == 0]

## version 2
print['CHAT WITH HER!','IGNORE HIM!'][len(set(raw_input()))&1]