# -*- coding: utf-8 -*-
"""
Created on Mon Jan  5 18:04:17 2015

@author: liuweizhi
"""

## version 1
print sum([2*('++' in raw_input())-1 for _ in range(input())])

## version 2
print sum([-1,1][raw_input()[1]=="+"] for _ in range(input()))

## version 3
print sum(44-ord(raw_input()[1])for i in[0]*input())