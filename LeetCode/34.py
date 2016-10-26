#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 18:30:09 2016

@author: liuweizhi
"""

#%%
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # find the possible index of the target
        l, r = 0, len(nums) - 1
        while(l < r):
            c = (l + r) // 2
            if target < nums[c]:
                r = c - 1
            elif nums[c] < target:
                l = c + 1
            else:
                l, r = [c] * 2
        # find the staring and end index of the target
        if nums[l] != target:
            ans = [-1, -1]
        else:
            for i in range(l+1)[::-1]:
                if nums[i] != target:
                    break
            for j in range(l, len(nums)):
                if nums[j] != target:
                    break
            ans = [i + 1 * (nums[i] != target), j - 1 * (nums[j] != target)]
        return ans
        

nums = [5, 7, 7, 8, 8, 10]
solver = Solution()
for foo in nums:
    print(foo, solver.searchRange(nums, foo))