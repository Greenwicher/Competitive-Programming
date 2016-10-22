# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 12:34:09 2015

@author: liuweizhi
"""

## version 1
n=input();a=map(int,raw_input().split())
print len([i for i in range(1,6) if (sum(a)+i)%(n+1)!=1])

## version 2
n=1+input();f=sum(map(int,raw_input()[::2]))
print sum((f+i)%n>0for i in range(5))