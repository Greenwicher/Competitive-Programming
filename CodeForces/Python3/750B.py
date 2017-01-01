#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 21:57:54 2016

@author: liuweizhi
"""

I = lambda: list(map(int, input().split()))
n = I()[0]
t, dir = [[] for _ in range(2)]
for _ in range(n):
    _t, _dir = input().split()
    t.append(int(_t))
    dir.append(_dir)
position = 0
flag = True
for i in range(n):
    _t = t[i]
    _dir = dir[i]
    if (position == 0) and (_dir != 'South'):
        flag = False
        break
    if (position == 20000) and (_dir != 'North'):
        flag = False
        break
    position += _t * (1 * (_dir == 'South') - 1 * (_dir == 'North'))
    if (position > 20000) or (position < 0):
        flag = False
        break    
if flag and (position == 0):
    print('YES')
else:
    print('NO')

        