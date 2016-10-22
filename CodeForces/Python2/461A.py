# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 22:04:15 2015

@author: liuweizhi
"""

## version 1 
input();seq=sorted(map(int,raw_input().split()))
print sum([j*(i+2) for i,j in enumerate(seq)])-seq[-1]

## version 2
n,a=input(),sorted(map(int,raw_input().split()))
print sum([x[0]*x[1] for x in zip(range(2,n+2),a)])-a[-1]