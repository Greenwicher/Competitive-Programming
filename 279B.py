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

## version 2 （two pointer）
''' loop the possible right pointer and update the left pointer'''
I=lambda:map(int,raw_input().split())
n,t=I();a=I();b=[0];ans=0;l=0
for i in range(n):
    b.append(b[-1]+a[i])
for r in range(n+1):
    ans=max(ans,(r-l)*(b[r]-b[l]<=t))
    while b[r]-b[l]>t: l+=1
print ans


## version 3
''' same with version but more elegant '''
R=lambda:map(int,raw_input().split())
n,t=R()
a=R()
u=s=z=0
for v in range(n):
  s+=a[v]
  while s>t:s-=a[u];u+=1
  z=max(z,v-u+1)
print z

## version 4
''' bisect package '''
from bisect import *
r = lambda: map(int, raw_input().split())
n, t = r()
a = [0] + r()
for i in xrange(1, n):
  a[i + 1] += a[i]
print max(bisect_right(a, a[i] + t) - i for i in xrange(n)) - 1
