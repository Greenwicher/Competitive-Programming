# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 17:17:09 2015

@author: liuweizhi
"""

## version 1
input();seq=map(int,raw_input().split())
a=max(seq);b=min(seq);c=seq.count(a);d=seq.count(b)
if a!=b:
    print a-b,c*d
else:
    print 0,c*(c-1)/2