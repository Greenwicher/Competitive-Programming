# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 15:28:17 2015

@author: liuweizhi
"""

## version 1
u=[];l=[];even_odd=False
f=lambda x:x%2
for _ in range(input()):
    x,y=map(int,raw_input().split())
    u.append(x);l.append(y)
    even_odd=even_odd or (f(x)+f(y)==1)
c=sum(map(f,map(sum,[u,l])))
print 0*(c==0)+(-1)*(c==1 or (c==2 and not(even_odd)))+1*(c==2 and even_odd)

## version 2 (another type logical expression)
a,b,c=0,0,0
for _ in range(input()):
  x,y=map(int,raw_input().split())
  a+=x;b+=y;c+=(x+y)%2
print (-1,(0,(-1,1)[c>0])[a%2])[a%2==b%2]

## version 3 (more simple expression)
n = input()
u, d, e = 0, 0, 0
for i in range(n):
    x, y = map(lambda x: int(x) & 1, raw_input().split())
    u ^= x
    d ^= y
    e |= x ^ y
print (0, (-1, 1)[u & d & e])[u | d]