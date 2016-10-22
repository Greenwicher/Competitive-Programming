# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 17:43:41 2016

@author: liuweizhi
"""

#%%
key = list(map(ord, 'a'+input()))
ans = 0
for i in range(1,len(key)):
    t = abs(key[i]-key[i-1])
    ans += min(t, 26-t)
print(ans)


