# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 23:50:15 2016

@author: liuweizhi
"""

#%%
I = lambda: list(map(int, input().split()))
n,m = I()
d = I()
a = I()
c = []
passed = {}
for i in d:
    a.append([-1,1+a[i]][i!=0])
for i in 