# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 18:13:24 2016

@author: liuweizhi
"""

#%% Version 1
x1,x2,x3 = list(map(int, input().split()))
print(max(x1,x2,x3)-min(x1,x2,x3))