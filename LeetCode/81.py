#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 13:35:37 2017

@author: liuweizhi
"""


#%% Version 1 - Reduce the duplicated nums[0] first, then use binary search, O(NlogN)
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not(nums): return False
        if nums[0] == target: return True
        l, r, k = 0, len(nums) - 1, nums[0]
        while nums[l] == k and l < r: l += 1
        while nums[r] == k and r > l: r -= 1
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
                    return True
            else:
                if nums[m] > target:
                    if nums[m] < nums[0]:
                        r = m
                    else:
                        l = m + 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    return True
        if nums[l] == target:
            return True
        else:
            return False
        