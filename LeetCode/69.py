#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 21:52:23 2016

@author: liuweizhi
"""

#%%
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x
        while(l < r - 1):
            m = (l + r) // 2
            if m ** 2 > x:
                r = m - 1
            elif m ** 2 < x:
                l = m 
            else:
                l, r = [m] * 2
        if r ** 2 <= x:
            return r
        else:
            return l

solver = Solution()
for i in range(2000):
    ans = solver.mySqrt(i)
    if ans**2<=i:
        print('Right')
    else:
        print('Wrong')
        
                