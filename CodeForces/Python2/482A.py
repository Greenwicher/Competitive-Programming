# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 12:33:05 2015

@author: liuweizhi
"""

## version 1
n,k=map(int,raw_input().split());ans=range(1,n-k)
spiral=range(n-k,n+1);i=0
while(spiral):
    ans.append(spiral.pop(-i))
    i=1-i
for i in ans:
    print i,
    
## version 2
n,k=map(int,raw_input().split())
c=k+2
for i in range((c-1)/2):
    print i+1, c-i-1,
if c%2==0:
    print c/2,
for j in range(c,n+1):
    print j,