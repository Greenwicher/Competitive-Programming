# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 13:03:22 2015

@author: liuweizhi
"""

## version 1
p,n=map(int,raw_input().split());hash=[]
for i in range(n):
    mod=input()%p
    if mod in hash:
        print i+1
        break
    else:
        hash.append(mod)
else:
    print -1 