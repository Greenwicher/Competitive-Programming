# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 10:52:05 2015

@author: liuweizhi
"""

## version 1
a,b,c,d=map(int,raw_input().split())
f=lambda p,t:max(3*p/10,p-p*t/250)
print ['Misha','Vasya'][f(a,c)-f(b,d)<0] if f(a,c)!=f(b,d) else 'Tie'