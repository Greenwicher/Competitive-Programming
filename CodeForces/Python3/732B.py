# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 22:28:21 2016

@author: liuweizhi
"""

#%%
I = lambda: list(map(int, input().split()))
n,k = I()
a = I()
b = [i for i in a]
c = [i for i in a]
ans1,ans2 = 0,0
for i in range(1,n):
    additional_walk = max(k-b[i]-b[i-1],0)
    b[i] += additional_walk
    ans1 += additional_walk
ans2 += max(k-c[0],0)
c[0] += max(k-c[0],0)
for i in range(1,n):
    additional_walk = max(k-c[i]-c[i-1],0)
    c[i] += additional_walk
    ans2 += additional_walk
print([ans1, ans2][ans2<ans1])
print(' '.join(map(str, [b,c][ans2<ans1])))