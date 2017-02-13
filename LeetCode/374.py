#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 20:36:18 2017

@author: liuweizhi
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

#%% Version 1, Binary Search, O(logN)
# Simplest binary search to find a number 
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l != r:
            m = (l + r) // 2
            if guess(m) < 0:
                r = m
            elif guess(m) > 0:
                l = m + 1
            else:
                return m
        return l