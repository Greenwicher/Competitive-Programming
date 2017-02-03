#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 20:54:41 2017

@author: liuweizhi
"""

#%% Version 1 - binary search
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1, nums2 = list(map(sorted, [nums1, nums2]))
        if len(nums1) > len(nums2): nums1, nums2 = nums2, nums1
        common = set()
        for i in nums1:
            if self.binary_search(i, nums2):
                common.add(i)
        return list(common)
        
    def binary_search(self, x, nums):
        l, r = 0, len(nums)
        while(l < r):
            m = (l + r) // 2
            if x < nums[m]:
                r = m - 1
            elif x > nums[m]:
                l = m + 1
            else:
                return True
        if x == nums[l]:
            return True
        else:
            return False
            
#%% Version 2 - two pointers
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1, nums2 = list(map(sorted, [nums1, nums2]))
        common = set()
        i, j = [0] * 2
        while(i < len(nums1) and j < len(nums2)):
            if nums1[i] == nums2[j]:
                common.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return list(common)