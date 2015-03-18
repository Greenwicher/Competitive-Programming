# -*- coding: utf-8 -*-
"""
Created on Sun Jan 11 15:36:07 2015

@author: liuweizhi
"""

## version 1
print 'YNEOS'[''.join(sorted(raw_input()+raw_input()))!=''.join(sorted(raw_input()))::2]

## version 2
r=raw_input;s=sorted;print"YNEOS"[s(r()+r())!=s(r())::2]