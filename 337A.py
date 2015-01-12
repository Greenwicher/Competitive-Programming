# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 11:40:57 2015

@author: liuweizhi
"""

## version 1
n,m=map(int,raw_input().split());diff=1000
seq=sorted(map(int,raw_input().split()))
for i in range(len(seq)-n+1):
    if max(seq[i:i+n])-min(seq[i:i+n])<diff:
        diff=max(seq[i:i+n])-min(seq[i:i+n])
print diff

## version 2
