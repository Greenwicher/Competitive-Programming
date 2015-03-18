# -*- coding: utf-8 -*-
"""
Created on Sun Jan 11 16:10:32 2015

@author: liuweizhi
"""

## version 1
n=input();a=b=c=0;l=lambda x:x!=0
for i in range(n):
    x,y,z=map(int,raw_input().split())
    a+=x;b+=y;c+=z
print 'YNEOS'[(l(a) or l(b) or l(c))::2]

## version 2
print"YNEOS"[any(map(sum,zip(*[map(int,raw_input().split())for i in[0]*input()])))::2]

## version 3
f=lambda:map(int,raw_input().split())
n=f()[0];a=[f() for i in range(n)]
r=[reduce(lambda x,y:x+y,v,0) for v in zip(*a)]
print 'NO' if any(r) else 'YES'