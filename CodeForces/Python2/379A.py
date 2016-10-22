# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 20:15:24 2015

@author: liuweizhi
"""

## version 1
a,b = map(int, raw_input().split())
ans = a * (a<b)
a = a * (a>=b)
while a>=b:
    ans += b
    a = a - b +1
ans += a
print ans
    
## version 2
a,b=map(int,raw_input().split())
print a+~-a/~-b

## version 3
a,b=map(int,raw_input().split())
print (a*b-1)/(b-1)

## version 4
a,b=map(int,raw_input().split())
c,d=0,0
while a>0:
  c+=a
  d+=a
  a=d/b
  d%=b
print c