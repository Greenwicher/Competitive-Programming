#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 20:20:49 2017

@author: liuweizhi
"""

#%% Version 1 - Binary search, O(logN)
# find the largest k such that k * (k + 1) <= 2 * n
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n
        while l != r:
            m = (l + r) // 2 + 1
            if m * (m + 1) > 2 * n:
                r = m - 1
            elif m * (m + 1) < 2 * n:
                l = m 
            else:
                return m
        return l