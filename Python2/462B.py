# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 12:09:41 2015

@author: liuweizhi
"""

## version 1
n,k=map(int,raw_input().split());ans=i=0
s=raw_input()
a=sorted([s.count(foo) for foo in set(s)])[::-1]
while i<len(a) and sum(a[0:i+1])<=k:
    ans+=a[i]**2
    i+=1
if i<=len(a): ans+=(k-sum(a[0:i]))**2
print ans
    
    
