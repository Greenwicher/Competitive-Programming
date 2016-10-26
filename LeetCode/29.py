#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 12:10:55 2016

@author: liuweizhi
"""

#%%
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor:
            negative = (dividend <= 0 and divisor > 0) or (dividend >= 0 and divisor < 0)
            l, r = 0, abs(dividend)
            while (l < r - 1):
                m = (l + r) >> 1
                total = sum([abs(divisor) for i in range(m)])
                if total > abs(dividend):
                    r = m - 1
                elif total < abs(dividend):
                    l = m
                else:
                    l, r = [m, m]
            total2 = sum([abs(divisor) for i in range(r)])            
            c = [l, r][total2 <= abs(dividend)]
            return [c, -c][negative]
        else:
            return -1
            
solver = Solution()
print(solver.divide(0,0), -1)
print(solver.divide(0,5), 0)
print(solver.divide(25,0), -1)
print(solver.divide(25,5), 5)
print(solver.divide(25,-5), -5)
print(solver.divide(-25,5), -5)
print(solver.divide(-25,-5), 5)
print(solver.divide(25,2), 12)
print(solver.divide(-25,2), -11)
print(solver.divide(25,-2), -11)
print(solver.divide(-25,-2), 12)

