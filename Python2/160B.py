# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 20:11:17 2015

@author: liuweizhi
"""

## version 1
n=input();a=raw_input()
x=sum(1 for i,j in zip(sorted(a[:n]),sorted(a[n:])) if i>j)
y=sum(1 for i,j in zip(sorted(a[:n]),sorted(a[n:])) if i<j)
print 'YNEOS'[(x-n)*(y-n)!=0::2]

## version 2
n=input();s=raw_input();S=sorted
print"NYOE S"[all(i<j for i,j in zip(*S([S(s[:n]),S(s[n:])])))::2]