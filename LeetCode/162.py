#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:44:57 2016

@author: liuweizhi
"""

#%% Version 1 - Naive iterative search, O(N)
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return 0
        if nums[0] > nums[1]: return 0
        if nums[-1] > nums[-2]: return len(nums) - 1
        for i in range(1, len(nums)-1):
            if nums[i-1] < nums[i] and nums[i] > nums[i+1]: return i
            
#%% Version 2 - Binary search, O(logN)
# climib the moutain based on the direction of the positive gradient
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return 0
        if nums[0] > nums[1]: return 0
        if nums[-1] > nums[-2]: return len(nums) - 1        
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > max(nums[m-1], nums[m+1]):
                return m
            elif nums[m] < nums[m-1]:
                r = m
            else:
                l = m + 1
        return l
                