# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 10:32:27 2015

@author: liuweizhi
"""

## version 1
input();seq=map(int,raw_input().split());a=[-1];b=[10001];
for foo in seq:
    if foo>a[-1]:
        a.append(foo)
    if foo<b[-1]:
        b.append(foo)
print len(a)+len(b)-4

## version 2 (think the other side)
n=input();a=map(int,raw_input().split())
x=a[:1]
for i in a:n-=min(x)<=i<=max(x);x+=[i]
print n

## version 3 (sum())
n=input()
p=map(int,raw_input().split())
print sum(1 for i in xrange(1,n)if max(p[:i])<p[i]or min(p[:i])>p[i])
