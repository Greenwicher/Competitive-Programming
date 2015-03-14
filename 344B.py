# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 19:46:19 2015

@author: liuweizhi
"""

## version 1
a,b,c=map(int,raw_input().split())
d=[(a-c+b)/2,(b-a+c)/2,(a-b+c)/2]
e=[(a-c+b)%2,(b-a+c)%2,(a-b+c)%2]
print ' '.join(map(str,d)) if min(d)>-1 and d.count(0)<2 and e.count(0)==3 else 'Impossible'