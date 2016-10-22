# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 22:28:30 2016

@author: liuweizhi
"""

#%%
I = lambda: list(map(int, input().split()))
a = I()
l = max(a)
maxa = [i==l for i in a]
if sum(maxa) == 1:
    ans = sum([l-1-i for i in a if i!=l])
elif sum(maxa) == 2:
    ans = l - 1 - (sum(a) - 2*l)
elif sum(maxa) == 3:
    ans = 0
print(ans)