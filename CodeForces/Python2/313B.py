# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 21:25:08 2015

@author: liuweizhi
"""

## version 1 (Time limit exceeded on test 10)
s=' '+raw_input()
for _ in range(input()):
    l,r=map(int,raw_input().split())
    print sum(1 for i,j in zip(s[l:r],s[l+1:r+1]) if i==j)
    
## version 2 (Time limit exceeded on test 10)
s=raw_input()
d=[1*(i==j) for i,j in zip(s[:-1],s[1:])]
for _ in range(input()):
    l,r=map(int,raw_input().split())
    print sum(d[l-1:r-1])
    
## version 3
s=raw_input();d=[0 for _ in range(len(s))]
for i in range(1,len(s)):
    d[i]=d[i-1]+1*(s[i-1]==s[i])
for _ in range(input()):
    l,r=map(int,raw_input().split())
    print d[r-1]-d[l-1]