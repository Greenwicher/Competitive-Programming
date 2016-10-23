# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 16:20:21 2013

@author: Administrator
"""
f = [1]*100000
i = 1
while(f[i]<=4000000):
    f[i+1] = f[i] + f[i-1]
    i = i+1
print sum([s for s in f if s%2==0])    
    
    