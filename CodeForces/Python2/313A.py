# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 09:40:10 2015

@author: liuweizhi
"""

## version 1
n=raw_input()
print max(map(int,[n,n[:len(n)-1],n[:len(n)-2]+n[-1]]))

## version 2
print map(lambda n:max(map(int,[n,n[:len(n)-1],n[:len(n)-2]+n[-1]])),[raw_input()])[0]

## version 3
a=input()
print max(a,-(-a//10),-(-a//100*10+(-a)%10))