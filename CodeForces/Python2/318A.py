# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 21:37:16 2015

@author: liuweizhi
"""

## version 1
n,k=map(int,raw_input().split())
thr=n/-2*-1
print (2*k-1)*(k<=thr)+2*(k-thr)*(k>thr)

## version 2
n,k=map(int,raw_input().split())
d=(n+1)/2
print (k*2-1,(k-d)*2)[k>d]