# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 14:13:44 2015

@author: liuweizhi
"""

## version 1 (Time limit exceeded on test 7)
I=lambda:map(int,raw_input().split())
n,k=I();h=I();a=2*(10**7);m=-1
for i in range(n-k+1):
    if sum(h[i:i+k])<a:
        a=sum(h[i:i+k])
        m=i
print m+1

## version 2
I=lambda:map(int,raw_input().split())
n,k=I();h=I();a=2*(10**7)
b=sum(h[:k]);m=-1
for i in range(n-k+1):
    a=[a,b][b<a]
    m=[m,i][b==a]
    b=b-h[i]+h[min(i,n-k-1)+k]
print m+1

## version 3
R=lambda:map(int,raw_input().split())
n,k=R()
a=[0]+R()
for i in range(n):a[i+1]+=a[i]
j=0
for i in range(n-k+1):
  if a[i+k]-a[i]<a[j+k]-a[j]:
    j=i
print j+1