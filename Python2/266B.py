# -*- coding: utf-8 -*-
"""
Created on Fri Jan  9 11:22:25 2015

@author: liuweizhi
"""

## version 1
n,t = map(int, raw_input().split())
seq = raw_input()
for i in range(t):
    if seq != seq.replace('BG', 'GB'):
        seq = seq.replace('BG', 'GB')
    else:
        break
print seq

## version 2
r=raw_input;t=int(r()[2:]);l=r()
while t:l=l.replace("BG","GB");t-=1
print l