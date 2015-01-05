# -*- coding: utf-8 -*-
"""
Created on Mon Jan  5 15:03:04 2015

@author: liuweizhi
"""

## version 1
n = input()
ans = 0
for _ in range(n):
    ans += (eval(raw_input().strip().replace(' ', '+')) >= 2)
print ans

## version 2
print sum(1 for i in range(input()) if raw_input().count('1') > 1)