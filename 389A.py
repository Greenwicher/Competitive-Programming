# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 14:12:34 2015

@author: liuweizhi
"""

## version 1 (wrong answer on test 27)
n=input();x=sorted(map(int,raw_input().split()))
print n*min([x[i+1]-x[i] for i in range(n-1) if x[i+1]>x[i]]+[x[0]])

## version 2
n=input();x=map(int,raw_input().split())
for i in range(min(x),0,-1):
    if all([j%i==0 for j in x]):
        break
print i*n

## version 3 (easy way to calculate the gcd)
from fractions import*
print input()*reduce(gcd,map(int,raw_input().split()))

## version 4 (simulate the procedure)
n = int(raw_input())
x = map(int, raw_input().split())
x.sort()
while x[0] != x[-1]:
  x[-1] -= x[0]
  x.sort()
print sum(x)