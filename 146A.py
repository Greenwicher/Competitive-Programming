# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 18:46:00 2015

@author: liuweizhi
"""

## version 1
n=input();a=raw_input()
f=lambda x:eval('+'.join(list(x)))
print 'YNEOS'[(not(set('47')>=set(a)))or(f(a[:n/2])!=f(a[n/2:]))::2]

## version 2
n, t = input(), raw_input()
print ['NO', 'YES'][set(t)<=set('47') and sorted(t[:n/2]*2)==sorted(t)]
