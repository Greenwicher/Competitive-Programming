# -*- coding: utf-8 -*-
"""
Created on Sun Jan 25 13:27:02 2015

@author: liuweizhi
"""

## version 1
n=input();h=[0]+map(int,raw_input().split())
energy=0;pay=0
for i in range(n):
    k=h[i+1]-h[i]
    pay+=[0,k-energy][energy<k]
    h[i]+=[0,k-energy][energy<k]
    energy+=[-min(energy,k),-k][k<0]
print pay
    
## version 2
input()
print max(map(int, raw_input().split()))