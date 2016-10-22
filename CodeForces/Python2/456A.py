# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 10:55:00 2015

@author: liuweizhi
"""

## version 1
a=sorted([map(int,raw_input().split()) for _ in range(input())])
b=[a[i][1] for i in range(len(a))]
print ['Poor Alex','Happy Alex'][b!=sorted(b)]

## version 2 (注意题目限定)
for i in range(input()):
	a,b=raw_input().split()
	if a!=b:print "Happy Alex";exit()
print "Poor Alex"