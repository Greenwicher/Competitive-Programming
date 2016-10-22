# -*- coding: utf-8 -*-
"""
Created on Sun Jan 11 16:39:39 2015

@author: liuweizhi
"""

## version 1
g=lambda x:-sum(map(int,raw_input().split()))/x*(-1) 
print 'YNEOS'[g(5)+g(10)>input()::2]

## version 2 (另类上取整)
R=lambda:sum(map(int,raw_input().split()))
print ['YES','NO'][(R()+4)/5+(R()+9)/10>input()]