# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 12:01:09 2015

@author: liuweizhi
"""

## version 1
n,m=map(int,raw_input().split())
f=lambda n,m,a:a+(n-a**2)**2==m
print sum(f(n,m,a) for a in range(int(n**(.5)+1)))

## version 2
n,m=map(int,raw_input().split())
print sum([i==n-(m-i*i)**2 for i in range(n+1) if m>=i*i])