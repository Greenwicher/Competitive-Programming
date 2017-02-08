#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 19:12:19 2017

@author: liuweizhi
"""

#%% Version 1 Invalid Solutions with O(N) space
class Solution(object): 
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]: return nums[i]
#%% Version 2 - Binary Search O(NlogN) time complexity
class Solution(object): 
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """  
        l, r = 1, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            count = sum([foo <= m for foo in nums])
            if count > m:
                r = m
            else:
                l = m + 1
        return l
        
#%% Version 3 - Tortoise and Hare algorithm, O(N) time complexity
# see http://keithschwarz.com/interesting/code/?dir=find-duplicate
class Solution(object): 
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """  
        slow, fast = 0, 0
        while 1:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break
        finder = 0
        while 1:
            slow = nums[slow]
            finder = nums[finder]
            if slow == finder: return slow