# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 20:25:42 2015

@author: liuweizhi
"""

## version 1
def gcd(a,b):
    if (b==0):
        return a
    else:
        return gcd(b, a%b)

a,b,n = map(int, raw_input().split())
simon = 1
while n!=0:
    n -= gcd(a,n)
    simon = 0
    if n!=0:
        n -= gcd(b,n)
        simon = 1
print simon

## version 2
gcd=lambda x,y:gcd(y,x%y) if y else x
wins=lambda a,b,n:1-wins(b,a,n-gcd(n,a)) if n else 1
print wins(*map(int,raw_input().split()))

## version 3
from fractions import gcd
a, b, n = map(int, raw_input().split())
t = 1
while n > 0:
    n -= gcd(a, n)
    t ^= 1
    a, b = b, a
print t