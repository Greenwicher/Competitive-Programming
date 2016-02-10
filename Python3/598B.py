# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 20:11:03 2016

@author: liuweizhi
"""

#%% Version 1
w = input()
for _ in range(int(input())):
    l,r,k = map(int,input().split())
    k %= r-l+1
    w = w[:l-1]+w[r-k:r]+w[l-1:r-k]+w[r:]
print(w)