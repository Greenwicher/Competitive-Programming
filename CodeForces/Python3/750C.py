#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 21:58:22 2016

@author: liuweizhi
"""

I = lambda: list(map(int, input().split()))
n = I()[0]
c, d = [[0] * n for _ in range(2)]
for i in range(n):
    _c, _d = I()
    c[i] = _c
    d[i] = _d
lb, ub, change = -1e100, 1e100, 0
for i in range(n)[::-1]:
    change -= c[i] 
    if d[i] == 1:
        lb = max(lb, 1900 - change)
    else:
        ub = min(ub, 1899 - change)
    if lb > ub:
        print('Impossible')
        break
if ub == 1e100:
    print('Infinity')    
elif lb <= ub:
    print(ub)
    