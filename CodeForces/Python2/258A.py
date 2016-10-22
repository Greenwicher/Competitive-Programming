# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 16:46:13 2015

@author: liuweizhi
"""

## version 1
a=raw_input()
try:
    print a[:a.index('0')]+a[a.index('0')+1:]
except:
    print a[1:]
    
## version 2
a=raw_input()
f=a.find('0')
if f<0:f=0
print(a[0:f:]+a[f+1::])
