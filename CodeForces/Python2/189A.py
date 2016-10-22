# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 11:05:31 2015

@author: liuweizhi
"""

## version 1
n,a,b,c=map(int,raw_input().split())
f=[0]+[-1e9]*5000 # smart initialization
for i in range(1,n+1):
    f[i]=max(f[i-a],f[i-b],f[i-c])+1
print f[n]

## version 2
n,a,b,c=map(int,raw_input().split())
v=[-n*3]*(n+max(a,b,c))
v[0]=0
for x in [a,b,c]:
  for i in range(n): v[i+x]=max(v[i+x],v[i]+1)
print v[n]