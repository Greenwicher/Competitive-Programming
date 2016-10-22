# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 12:34:43 2015

@author: liuweizhi
"""

## version 1
n=input();a=map(int,raw_input().split())
x=y=0
for i in range(n):
    x+=[0,1][a[i]==i]
    y+=[0,1][a[i]!=i and a[a[i]]==i]
print x+1*(x!=n)+1*(y>0)