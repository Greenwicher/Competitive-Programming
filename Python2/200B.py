# -*- coding: utf-8 -*-
"""
Created on Fri Jan 23 16:07:59 2015

@author: liuweizhi
"""

## version 1
n=float(input())
seq=map(int,raw_input().split())
print sum(seq)/n

## version 2
print input()**-1*sum(map(int,raw_input().split()))

## version 3
n=input()
print sum(map(float,raw_input().split()))/n