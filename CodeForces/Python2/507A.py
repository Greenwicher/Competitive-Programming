# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 09:48:11 2015

@author: liuweizhi
"""

## version 1
I=lambda:map(int,raw_input().split())
n,k=I();seq=sorted(zip(I(),range(n)));total=0;i=0
while total<=k and i<n:
    total+=seq[i][0]
    i+=1
num=[n,i-1][total>k]
print num
for i in range(num):
    print seq[i][1]+1,

## version 2
R=lambda:map(int,raw_input().split())
n,k=R()
t=[]
for a,b in sorted(zip(R(),range(n))):
  if k>=a:
    t+=[b+1]
    k-=a
print len(t)
print ' '.join(map(str,t))