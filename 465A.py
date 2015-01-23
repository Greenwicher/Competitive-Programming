# -*- coding: utf-8 -*-
"""
Created on Fri Jan 23 10:49:18 2015

@author: liuweizhi
"""

## version 1
n=input();bit=raw_input()
for i in range(n):
    if bit[i]=='0':
        break
print [n,i+1][bit[i]=='0']

## version 2
print min(input(),len(raw_input().split('0')[0])+1)