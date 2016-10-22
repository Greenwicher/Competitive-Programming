# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 21:49:50 2016

@author: liuweizhi
"""

#%%
I = lambda: list(map(int, input().split()))
k,r = I()
ans = 1
while(ans*k%10!=r and ans*k%10!=0):
    ans+=1
print(ans)