# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 15:29:13 2016

@author: liuweizhi
"""

#%% version 1
I = lambda: map(int,input().split())
k,n,w = I()
print(max(int((1+w)*w/2*k-n),0))