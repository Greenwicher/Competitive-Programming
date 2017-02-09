#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 10:52:10 2017

@author: liuweizhi
"""

#%% Version 1 - Binary Search
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[r] < nums[l]:
                m = (l + r) // 2                
                if nums[m] >= nums[l]:
                    l = m + 1
                elif nums[m] < nums[l]:
                    r = m
            else:
                return nums[l]
    