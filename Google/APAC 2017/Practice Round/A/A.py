#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 22:07:00 2017

@author: liuweizhi
"""

#%% Version 1
def solve(s):
    if len(s) == 1: return 1
    num = 1
    for i in range(1,len(s)-1):
        num *= len(set([s[i-1], s[i], s[i+1]]))
        num %= 1e9 + 7
    num *= len(set([s[0], s[1]]))
    num *= len(set([s[-1], s[-2]]))
    return num % (1e9 + 7)

f_in = open('A-large-practice.in', 'r')
f_out = open('A-large-practice.out', 'w')
data = [foo.strip() for foo in f_in.readlines()]
for i in range(int(data[0])):
    f_out.write('Case #%d: %d\n'% (i+1, solve(data[i+1])))
    print(data[i+1], solve(data[i+1]), len(data[i+1]))
f_in.close()
f_out.close()

