# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 22:07:41 2016

@author: liuweizhi
"""

#%% 
I = lambda: list(map(int, input().split()))
T = I()[0]
for i in range(T):
    s = I()
    print('Case %d: %d' % (i+1, sum(s)-max(s)-min(s)))