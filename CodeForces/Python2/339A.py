# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 19:55:22 2015

@author: liuweizhi
"""

## version 1
print '+'.join(map(str, sorted(map(int, raw_input().split('+')))))

## version 2
print"+".join(sorted(raw_input()[::2]))