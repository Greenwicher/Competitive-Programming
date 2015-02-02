# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 19:51:55 2015

@author: liuweizhi
"""

## version 1
input();seq=map(int,raw_input().split())
t=[sum(seq[::3]),sum(seq[1::3]),sum(seq[2::3])]
print ['chest','biceps','back'][t.index(max(t))]

## version 2
input()
l=map(int,raw_input().split())
print["chest","biceps","back"][max(0,1,2,key=lambda i:sum(l[i::3]))]

