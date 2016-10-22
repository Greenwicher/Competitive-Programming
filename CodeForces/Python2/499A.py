# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 15:31:42 2015

@author: liuweizhi
"""

## version 1
I=lambda:map(int,raw_input().split())
n,x=I();a=[];ans=0
for i in range(n): a.append(I())
a=[[1,0]]+a+[[a[-1][-1]+1,a[-1][-1]+1]]
for i in range(n+1):
    ans+=a[i][1]-a[i][0]+1+(a[i+1][0]-a[i][1]-1)%x
print ans
    
