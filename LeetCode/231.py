#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 18:08:45 2016

@author: liuweizhi
"""

#%%
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return [False, True][bin(n)[2:].count('1')==1]