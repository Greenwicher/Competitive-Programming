#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 21:53:05 2016

@author: liuweizhi
"""

I = lambda: list(map(int, input().split()))
n,k = I()
valid = [i for i in range(n+1) if k + 5*i*(i+1)/2 <= 240]
if valid:
    print(valid[-1])
else:
    print(0)

