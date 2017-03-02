#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 13:36:45 2017

@author: liuweizhi
"""
#%% Version 1 - Binary search, O(logN)
# check whether the target may fall in the first segment or the second one
# the if ... elif ... else statement can be reduced
# you may also consider find the index of smallest value first by using binary
# search, and then solve the two segments separetly 
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not(nums): return -1
        l, r = 0, len(nums) - 1
        while l != r:
            m = (l + r) // 2
            if target >= nums[0]:
                if nums[m] > target:
                    r = m
                elif nums[m] < target:
                    if nums[m] < nums[0]:
                        r = m
                    else:
                        l = m + 1
                else:
                    return m
            else:
                if nums[m] > target:
                    if nums[m] < nums[0]:
                        r = m
                    else:
                        l = m + 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    return m
        if nums[l] == target:
            return l
        else:
            return -1
