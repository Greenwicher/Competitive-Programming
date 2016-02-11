# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 20:47:21 2016

@author: liuweizhi
"""

#%% Version 1
from math import *
# stores counterclockwise angle between vector (1,0) and each vector in a
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
from math import *
# stores counterclockwise angle between vector (1,0) and each vector in a
a = []
n = int(input())
for i in range(n):
    x,y = map(int,input().split())
    # calculate counterclockwise angle between (1,0) and this vector
    t = acos(x/sqrt(x**2+y**2))
    a.append((i+1,[2*pi-t,t][y>=0],x,y))
cmp = lambda x:x[1]
a = sorted(a,key=cmp)
# construct pairs for adjacent vectors
b = []
for i in range(n):
    i1,i2 = a[i][0],a[(i+1)%n][0]
    x1,y1 = a[i][2:]
    x2,y2 = a[(i+1)%n][2:]
    inner_prod = x1*x2 + y1*y2
    inner_prod *= abs(inner_prod)
    norm_prod = ((x1**2+y1**2)*(x2**2+y2**2))
    b.append((i1,i2,inner_prod,norm_prod))
# find the nearest vector
better = lambda p1,p2: p1[2]*p2[3]>p2[2]*p1[3]
ans = b[-1]
for i in range(n):
    if better(b[i],ans):
        ans = b[i]
print(ans[0],ans[1])
