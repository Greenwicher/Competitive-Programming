# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 12:45:28 2015

@author: liuweizhi
"""

## version 1
for i in range(input()):
    print 'YNEOS'[360%(180-input())!=0::2]
    
## version 2 (exec)
I=input;exec I()*"print'YNEOS'[360%(180-I())>0::2];"