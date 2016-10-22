# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 18:22:58 2015

@author: liuweizhi
"""

## version 1
I=lambda:map(int,raw_input().split())
n=I();d=I();s,t=map(lambda x:x-1,sorted(I()))
print min([sum(d[s:t]),sum(d)-sum(d[s:t])])