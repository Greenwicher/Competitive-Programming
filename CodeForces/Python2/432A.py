# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 13:03:24 2015

@author: liuweizhi
"""

## version 1
I=lambda:map(int,raw_input().split())
n,k=I();t=I()
print sum(1 for i in t if 5-i>=k)/3