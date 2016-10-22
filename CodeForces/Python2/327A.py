# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 20:26:09 2015

@author: liuweizhi
"""

## version 1
n=input();a=map(int,raw_input().split());
b=sum(a);ans=-1
for i in range(1,n+1):
    for j in range(n+1-i):
        ans=max(ans,b-a[j:j+i].count(1)+a[j:j+i].count(0))
print ans
        
## version 2