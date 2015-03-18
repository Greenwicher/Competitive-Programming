# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 13:43:47 2015

@author: liuweizhi
"""

## version 1
n=input()
if n>2:
    print ' '.join(map(str,[n-1]+range(1,n)[::-1]))
else:
    print -1
    
## version 2
n=input()-2
print -1 if n<1 else '2 3','1 '*n