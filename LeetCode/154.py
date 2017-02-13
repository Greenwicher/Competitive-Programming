#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 18:55:03 2017

@author: liuweizhi
"""

#%% Version 1 - Binary search, O(N)
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while r > 0 and nums[r] == nums[0]: r -= 1 
        while l <= r:
            if nums[r] < nums[l]:
                m = (l + r) // 2                
                if nums[m] > nums[l]:
                    l = m + 1
                elif nums[m] < nums[l]:
                    r = m
                elif nums[l] <= nums[r]:
                    return nums[l]
                else:
                    l = m + 1                    
            else:
                return nums[l]