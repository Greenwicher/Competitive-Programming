# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:25:41 2015

@author: liuweizhi
"""

## version 1 (Time limit exceeded on test 14)
m=input();a=map(int,raw_input().split())
b=sorted(set(a));c=[]
for i in b:
    if a.count(i)>1 and i!=max(b):c.append(i)
print len(b+sorted(c))
print ' '.join(map(str,b+sorted(c)[::-1]))

## version 2
m=input();a=map(int,raw_input().split())
b=sorted(set(a));c=[0]*5001;d=[]
for i in a:c[i]+=1
for i in b[-2::-1]:
    if c[i]>1:d.append(i)
print len(b+d)
print ' '.join(map(str,b+d))
