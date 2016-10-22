# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 20:52:07 2015

@author: liuweizhi
"""

## version 1
I=lambda:map(int,raw_input().split())
n,k=I()
f=lambda f,t: (f-t+k)*(t>k)+f*(t<=k)
print max([f(*I()) for _ in range(n)])

## version 2
R=lambda:map(int,raw_input().split())
n,k=R()
print max(x[0]-max(0,x[1]-k)for x in [R() for _ in range(n)])