# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 19:46:58 2015

@author: liuweizhi
"""

## version 1
n=input();a=sorted(map(int,raw_input().split()))
b=[[]]*3
b[0]=[a[0]]
b[1]=[[a[-1]],[a[1],a[2]]][a[1]*a[2]>0]
b[2]=[a[1:-1],a[3:]][a[1]*a[2]>0]
for i in range(3):
    print len(b[i]),' '.join(map(str,b[i]))

## version 2 (smart use of pop() rather than remove or specifiy the range of array)
I=raw_input;I();a=sorted(I().split());p=a.pop
for l in[p(0)],[p(0),p(0)]if a[1]<'0'else[p()],a:print len(l),' '.join(l):
    
## version 3
input()
a=sorted(raw_input().split())
f=a.pop
n=[f(0)]
p=a[-1]>'0' and [f()] or [f(0),f(0)]
for i in n,p,a: print len(i),' '.join(i)
