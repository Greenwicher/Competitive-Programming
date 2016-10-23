#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 17:21:41 2016

@author: liuweizhi
"""

#%%
I = lambda: list(map(int, input().split()))
while(True):
    try:
        N,B,H,W = I()
        cost = B + 1
        for i in range(H):
            p = I()[0]
            a = I()
            for c in a:
                cost = [cost, p*N][N<=c and p*N<=B and p*N<cost]
        print(['stay home', cost][cost!=B+1])
    except:
        break