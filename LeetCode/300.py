#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 13:54:09 2017

@author: liuweizhi
"""

#%% Version 1 - Pure DP, O(N^2)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not(nums): return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]: dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
        
#%% Version 2 - Binary search, O(NlogN)
# tails is an array storing the smallest tail of all increasing subsequences with length i+1 in tails[i].
# size at iteration i is the length of longest invreasing subsequences given nums[:i]
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not(nums): return 0
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            import bisect
            # find i such that tails[i-1] < x <= tails[i]
            i = bisect.bisect_left(tails[:size], x)
            tails[i] = x
            size = max(size, i + 1)
        return size