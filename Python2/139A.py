# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 15:11:07 2015

@author: liuweizhi
"""

## version 1
n=input();p=map(int,raw_input().split());i=0
while n>0:
    n-=p[i]
    i=[i+1,0][i==6]
print [i,7][i==0]

## version 2
n=input();a=raw_input().split();i=6
while n>0:i=-~i%7;n-=int(a[i])
print-~i

## version 3
n,i,d=input(),0,map(int,[0]+raw_input().split())*1000
while n>0: i=(i+1)%8; n-=d[i]
print i
