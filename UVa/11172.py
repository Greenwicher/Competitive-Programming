# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 12:31:06 2016

@author: liuweizhi
"""

#%%
I = lambda: list(map(int, input().split()))
for i in range(I()[0]):
    a,b = I()
    print([['>','<'][a<b],'='][a==b])