# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 14:42:11 2015

@author: liuweizhi
"""

## version 1
n,m=map(int,raw_input().split())
k=[0]*m;a=[[]]*m
for i in range(n):
    s=map(int,list(raw_input()))
    for j in range(m):
        if s[j]>k[j]:
            k[j]=s[j]
            a[j]=[i+1]
        elif s[j]==k[j]:
            a[j].append(i+1)
print len(set(i for q in a for i in q))

## version 2 (looks so brief)
r=raw_input;z=map(r," "*int(r().split()[0]))
print sum(any(i==max(j)for i,j in zip(s,zip(*z)))for s in z)
    