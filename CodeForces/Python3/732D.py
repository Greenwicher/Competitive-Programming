# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 22:22:32 2016

@author: liuweizhi
"""

#%%
from collections import defaultdict
def ok(i):
    prep = defaultdict(lambda: False)
    need = 0
    for day in range(i+1)[::-1]:
        if d[day] and not(prep[d[day]]):
            prep[d[day]] = True
            need += a[d[day]-1]
        elif need>0:
            need -= 1
    if need or sum(list(prep.keys()))!=(1+m)*m/2:
        return False
    else:
        return True
I = lambda: list(map(int, input().split()))
n,m = I()
d = I()+[0]
a = I()
l,r = 0,n-1
while(l<=r):
    c = (l+r)//2
    if ok(c):
        r = c - 1
    else:
        l = c + 1
print([[-1,r+1][ok(r)],l+1][ok(l)])