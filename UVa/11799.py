#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 17:34:11 2016

@author: liuweizhi
"""

#%%
I = lambda: list(map(int, input().split()))
for i in range(I()[0]):
    c = I()
    print('Case %d: %d' % (i+1, max(c[1:])))