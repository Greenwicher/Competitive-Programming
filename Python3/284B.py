# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 17:49:55 2015

@author: liuweizhi
"""

## version 1
n=int(input());s=input()
a=s.count('A');b=s.count('I')
print([a,[1,0][b!=1]][b!=0])

## version 2
n=int(input());s=input()
print([s.count('A'),1,0][min(s.count('I'),2)])