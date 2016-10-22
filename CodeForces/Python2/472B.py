# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 19:21:51 2015

@author: liuweizhi
"""

## version 1
I=lambda:map(int,raw_input().split())
n,k=I();f=sorted([0]*(k-n%k)+I())[::-1];ans=0
for i in range(-(-n/k)):
    ans+=2*max(f[i*k:i*k+k+1])-2
print ans

## version 2 (after sorting, the max of each group is determined)
k = map(int, raw_input().split())[1]
print 2*sum([x-1 for x in sorted(map(int, raw_input().split()))[::-k]])