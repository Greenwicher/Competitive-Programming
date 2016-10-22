# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 18:01:02 2016

@author: liuweizhi
"""

#%%
I = lambda: list(map(int, input().split()))
n, a = I()[0], I()
active_coupon = False
for i in range(n):
    #order quantity after last active coupon if exists
    q = a[i] - 1*active_coupon
    if q >= 0:
        #check whether needs second coupon
        r = q % 2
        #must use second coupon
        active_coupon = [True, False][r!=1]
    else:
        #negative order quantity
        active_coupon = True
        break
print('YNEOS'[active_coupon::2])