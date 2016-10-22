# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 20:17:11 2015

@author: liuweizhi
"""

## version 1
I=lambda:map(int,raw_input().split())
n,t=I();a=[0]+I();pos=1;flag=1
b=[i+a[i] for i in range(len(a))]
while pos<len(b):
    if b[pos]==t:
        flag=0
        break
    else:
        pos=b[pos]
print 'YNEOS'[flag::2]

## version 2 (这条while写的很漂亮，一行递推表达式)
R=lambda:map(int,raw_input().split())
n,x=R()
a=R()
i=1
while i<x:i+=a[i-1]
print ['YES','NO'][i>x]