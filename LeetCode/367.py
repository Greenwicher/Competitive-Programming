#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 13:43:41 2017

@author: liuweizhi
"""


#%% Version 1 - Binary search, O(logNum)
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l, r = 1, num
        while l < r:
            m = (l + r) // 2
            if m ** 2 > num:
                r = m
            elif m ** 2 < num:
                l = m + 1
            else:
                return True
        if l ** 2 == num:
            return True
        else:
            return False