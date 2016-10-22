# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 21:38:32 2015

@author: liuweizhi
"""

## version 1
n,m=map(int,raw_input().split())
p=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]
print 'YNEOS'[p[p.index(n)+1]!=m::2]

## version 2
a,b=map(int,raw_input().split())
print ['NO','YES'][min([x for x in xrange(a+1,3*a) if all(x%i for i in xrange(2,x))])==b]