# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 20:47:21 2016

@author: liuweizhi
"""

#%% Version 1
from math import *
# stores counterclockwise angle between (1,0) and each vector in a
a = []
n = int(input())
for _ in range(n):
    x,y = map(int,input().split())
    # calculate counterclockwise angle between (1,0) and this vector
    t = acos(x/sqrt(x**2+y**2))
    a.append([2*pi-t,t][y>=0])
# sorting a     
b = sorted(a)
# calculate difference of angle between adjacent vector
c = [b[i+1]-b[i] for i in range(n-1)]
c.append(b[-1]-b[0])
c = [[2*pi-foo,foo][foo<pi] for foo in c]
# find the nearest vector
i_min = c.index(min(c))

if i_min!=n-1:
    i1 = a.index(b[i_min+1])
    i2 = a.index(b[i_min])
else:
    i1 = a.index(b[0])
    i2 = a.index(b[-1])
print(i1+1,i2+1)

#%% Version 2
cosv = lambda a,b,c,d:(a*c+b*d)/((a*a+b*b)*(c*c+d*d))**0.5