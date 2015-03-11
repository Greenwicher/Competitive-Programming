# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 21:14:13 2015

@author: liuweizhi
"""

## version 1 (Time limit exceeded on test 9	)
I=lambda:map(int,raw_input().split())
n,t=I();a=I();b=[0];ans=0
for i in range(n):
    b.append(b[-1]+a[i])
for i in range(n):
    l=i;r=n
    while(l!=r-1):
        m=(l+r)/2
        l=[l,m][b[m]-b[i]<=t]
        r=[r,m][b[m]-b[i]>t]
    ans=max(ans,l*(b[r]-b[i]>t)+r*(b[r]-b[i]<=t)-i)
print ans