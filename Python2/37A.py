# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 19:45:00 2015

@author: liuweizhi
"""

## version 1
input()
l=map(int,raw_input().split())
s=set(l)
num=[l.count(b) for b in s]
print max(num),len(s)

## version 2
input()
l=raw_input().split()
print max(l.count(i)for i in l),len(set(l))