# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 17:59:15 2015

@author: liuweizhi
"""

## version 1
n,m=map(int,raw_input().split())
ans=-1
for i in range(1,n+1):
    if i%m==0 and i<=n<=2*i:
        ans=i
        break
print ans

## version 2
n, m = map(int, raw_input().split())
print -1 if m>n else (n+2*m-1)/2/m*m

## version 3
n,m = map( int, raw_input().split() )
ans = n / 2 + n % 2
ans += -ans % m
print -1 if ans > n else ans

## version 4 (reduce the for loop)
n,m=map(int,raw_input().split())
s=n/2+n%2
for t in xrange(s,s+n/2+1):
    if t%m==0:break
else:t=-1
print t