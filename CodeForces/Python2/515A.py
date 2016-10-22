# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 14:26:53 2015

@author: liuweizhi
"""

## version 1
a,b,s=map(int,raw_input().split())
print 'YNEOS'[1-(s>=abs(a)+abs(b) and (s-abs(a)-abs(b))%2==0)::2]