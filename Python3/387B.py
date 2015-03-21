# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:24:34 2015

@author: liuweizhi
"""

## version 1
I=lambda:list(map(int,input().split()))
n,m=I();a=I();b=I()
i=j=0
while(i<n and j<m):
    i+=1*(a[i]<=b[j]);j+=1
print(n-i)