# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 12:56:09 2015

@author: liuweizhi
"""

## version 1
I=lambda:map(int,raw_input().split())
n=input();a=I()
for i in range(input()):
    x,y=I()
    if x>1:
        a[x-2]+=y-1
    if x<n:
        a[x]+=a[x-1]-(y-1)-1
    a[x-1]=0
for i in range(n):
    print a[i]
    
## version 2 (safe boundary)
I=lambda:map(int,raw_input().split())
I()
a=[0]+I()+[0]
for _ in[0]*I()[0]:x,y=I();a[x-1]+=y-1;a[x+1]+=a[x]-y;a[x]=0
for i in a[1:-1]:print i:
    
## version 3
n, a = input(), map(int, raw_input().split())
for _ in [0]*input():
    x, y = map(int, raw_input().split())
    a[x%n] += [0, a[x-1]-y][x<n]
    a[x-2] += [0, y-1][x>1]
    a[x-1] = 0
for i in a:print i